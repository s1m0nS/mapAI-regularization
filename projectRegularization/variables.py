# CONFIGURE THE PATHS HERE: 

# TRAINING 
DATASET_RGB = "/home/shymon/datasets/mapai_full/train/images/*.tif"
DATASET_GTI = "/home/shymon/datasets/mapai_full/train/masks/*.tif"
DATASET_SEG = "/home/shymon/Documents/mapAI-regularization/predictions/*.tif"

DEBUG_DIR = "./debug/"

# INFERENCE 
INF_RGB = "/home/shymon/datasets/mapai_full/task1_test/images/*.tif"
INF_SEG = "/home/shymon/Documents/mapAI-regularization/predictions/*.tif"
INF_OUT = "/home/shymon/Documents/mapAI-regularization/regularizations/"

MODEL_ENCODER = "/home/shymon/Documents/mapAI-regularization/projectRegularization/pretrained_weights/E140000_e1"
MODEL_GENERATOR = "/home/shymon/Documents/mapAI-regularization/projectRegularization/pretrained_weights/E140000_net"
