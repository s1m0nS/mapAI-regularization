# mapAI-regularization

The repository stores the code for our work presented at Foss4G 2023 with the title: **AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION,
BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS.**

## Introduction

The purpose of our research is to develop and end-to-end workflow for accurate segmentation of building footprints including three major steps: 
 - (1) binary semantic segmentation with a CNN,
 - (2) applying building boundary regularization and 
 - (3) vectorization. 

The dataset used for building segmentation is the NORA MapAI: Precision in Building Segmentation dataset. We have developed an implementation for building footprint segmentation. Our approach extends the segmentation by implementing projectRegularization from (Zorzi and Fraundorfer, 2019, Zorzi et al., 2021) on a semantic segmentation task. The link to the official repository can be accessed here: https://github.com/zorzi-s/projectRegularization. Note that this is already included in our repository.

## MapAI dataset

The original MapAI: Precision in Building Segmentation dataset can be downloaded manually from Huggingface: https://huggingface.co/datasets/sjyhne/mapai_training_data

or by running our first notebook.

## Installation

```
git clone https://github.com/s1m0nS/mapAI-regularization.git
cd mapAI-regularization
conda create --name mapai python=3.10
conda activate mapai
pip install -r requirements.txt
```
Installing GDAL inside a conda environment can be tricky. Follow the steps below according to your OS.

**Linux:**

```
sudo apt-get update && sudo apt upgrade -y && sudo apt autoremove 
sudo apt-get install -y cdo nco gdal-bin libgdal-dev-
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade gdal
conda install -c conda forge libgdal
conda install -c conda-forge libgdal
conda install -c conda-forge gdal
conda install tiledb=2.2
conda install poppler
```

**Windows:**

Get the appropriate .whl file for your Python version from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
For Python 3.10 use either: 
- GDAL‑3.4.3‑cp310‑cp310‑win_amd64.whl or
- GDAL‑3.4.3‑cp310‑cp310‑win32.whl.

then install the appropriate one as:
```
conda activate mapai
python -m pip install C:\Users\...\GDAL‑3.4.3‑cp310‑cp310‑win_amd64.whl
```

Run our Jupyter Notebooks and enjoy the process. If you encounter errors post an issue.





