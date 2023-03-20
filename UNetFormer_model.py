import torch
import torch.nn as nn

class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ConvBlock, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
        )
        
    def forward(self, x):
        x = self.conv(x)
        return x

class EncoderBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(EncoderBlock, self).__init__()
        self.conv_block = ConvBlock(in_channels, out_channels)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        
    def forward(self, x):
        x = self.conv_block(x)
        pool = self.pool(x)
        return x, pool

class DecoderBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(DecoderBlock, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels, in_channels//2, kernel_size=2, stride=2)
        self.conv_block = ConvBlock(in_channels, out_channels)
        
    def forward(self, x, skip):
        x = self.conv_transpose(x)
        x = torch.cat([x, skip], axis=1)
        x = self.conv_block(x)
        return x

class UNetFormer(nn.Module):
    def __init__(self, in_channels=3, out_channels=1, init_features=64):
        super(UNetFormer, self).__init__()
        self.downs = nn.ModuleList()
        self.ups = nn.ModuleList()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.center = ConvBlock(init_features*8, init_features*16)
        
        # downsampling path
        features = init_features
        for i in range(3):
            self.downs.append(EncoderBlock(in_channels, features))
            in_channels = features
            features *= 2
        
        # upsampling path
        for i in range(3):
            self.ups.append(DecoderBlock(in_channels, features//2))
            in_channels = features
            features //= 2
        
        self.conv_out = nn.Conv2d(init_features, out_channels, kernel_size=1)
        
    def forward(self, x):
        skips = []
        
        # downsampling path
        for down in self.downs:
            x, skip = down(x)
            skips.append(skip)
        
        x = self.center(x)
        
        # upsampling path
        for i, up in enumerate(self.ups):
            skip = skips[-i-1]
            x = up(x, skip)
        
        out = self.conv_out(x)
        return out