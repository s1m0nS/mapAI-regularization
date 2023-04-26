# mapAI-regularization

The repository stores the code for our work presented at Foss4G 2023 with the title: **AN END-TO-END DEEP LEARNING WORKFLOW FOR BUILDING SEGMENTATION,
BOUNDARY REGULARIZATION AND VECTORIZATION OF BUILDING FOOTPRINTS.**

## Introduction

The purpose of our research is to develop and end-to-end workflow for accurate segmentation of building footprints including three major steps: 
 - (1) binary semantic segmentation with a CNN,
 - (2) applying building boundary regularization and 
 - (3) vectorization. 

The dataset used for building segmentation is the NORA MapAI: Precision in Building Segmentation dataset. We have developed an implementation for building footprint segmentation. Our approach extends the segmentation by implementing projectRegularization from (Zorzi and Fraundorfer, 2019, Zorzi et al., 2021) on a semantic segmentation task. The link to the official repository can be accessed here: https://github.com/zorzi-s/projectRegularization.

## MapAI dataset

The original MapAI: Precision in Building Segmentation dataset can be downloaded manually from Huggingface: https://huggingface.co/datasets/sjyhne/mapai_training_data

or by running our first notebook.

## Installation

'''
pip 
'''






