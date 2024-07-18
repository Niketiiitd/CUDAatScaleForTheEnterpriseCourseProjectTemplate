# Canny Edge Detection Assignment

## Overview

This assignment is based on Image Processing. It demonstrates the application of Median Filtering and Canny Edge Detection using NVIDIA's NPP (NVIDIA Performance Primitives) library. These image processing techniques are implemented to leverage GPU acceleration for efficient processing of images.
medianFilterCannyEdgeNPP is the main folder containing medianFilterCannyEdgeNPP.cpp , which has the code for both the algorithms and the Makefile.
cmu_face_images is the folder containing the original CMU FACE IMAGES. This dataset has 20 subfolders having 32 images in each folder. These images are images of 20 different people.
cmu_face_medianFilter is the output folder containing all the images after applying the Median Filter.
cmu_face_cannyedge is the output folder containing all the images after applying Canny Edge Detection.
run.sh is also included in the folder and is useful for running the code.

## Dataset
For the assignment I have used the CMU FACE IMAGES Dataset(https://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-8/faceimages/faces/). This is one of the datasets mentioned in the Instructions. The images in this dataset are in PGM format, which is similar to the format given in the NPP Box Filtering Laboratory.
## Techniques Used

1. **Median Filter**: Reduces noise in images by replacing each pixel with the median value from a surrounding window of pixels. I have used this algorithm as it is one of the altenative methods to box filtering.
2. **Canny Edge Detection**: It identifies edges in images using a multi-stage algorithm involving noise reduction, gradient calculation, non-maximum suppression, and edge tracking by hysteresis. I have used this algorithm for finding edge detection in the input images.

## Requirements

- CUDA Toolkit
- NPP Library
- C++ Compiler
- Makefile

## Code Flow
I have followed the Nvidia Documentation.
First I have written the function for Median Filter, which basically blurs the images.
Then I have written the function for Canny Edge Detection, which helps in finding the edges of the faces and the surrounding area.
Both the functions are called in the main function for creating the output folders.
medianFilterCannyEdgeNPP.cpp has been commented for code explanation.
For changing the dataset the path of the input and output folders in the file medianFilterCannyEdgeNPP.cpp should be changed for getting the results.

## How to Run
Change the directory till medianFilterCannyEdgeNPP Folder.
cd GPUCoure3-main
After that run
1. make clean build
2. make run

## Purpose
1. Median Filtering:
   The primary purpose for choosing Median Filtering was for reducing the noise in the images.   It helps in smoothening of images by reducing the noise.
2. Canny Edge Detection:
   The purpose of choosing Canny Edge Detection was to identify the edges in the images. Edges represent the change in intesity. This could be furhter used for tasks like object detection, object recognition and many other computer vision related tasks.

## How to View the Results
You can view the output images by either install an application like Bitberry File Opener or simply viewing on some PGM file viewer website.
