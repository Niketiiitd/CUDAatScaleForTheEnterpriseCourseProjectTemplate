/* Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *  * Neither the name of NVIDIA CORPORATION nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
#define WINDOWS_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#pragma warning(disable : 4819)
#endif

#include <Exceptions.h>
#include <ImageIO.h>
#include <ImagesCPU.h>
#include <ImagesNPP.h>

#include <string.h>
#include <fstream>
#include <iostream>

#include <cuda_runtime.h>
#include <npp.h>

#include <helper_cuda.h>
#include <helper_string.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>
#include <FreeImage.h>
#include "npp.h"

// Namespace for filesystem library
namespace fs = std::filesystem;

void MedianFilter(const std::string &inputPath, const std::string &outputPath)
{
  try
  {
    // Load input image
    npp::ImageCPU_8u_C1 oHostSrc;
    npp::loadImage(inputPath, oHostSrc);

    // Create device image and copy from host to device
    npp::ImageNPP_8u_C1 oDeviceSrc(oHostSrc);

    // Define median filter parameters
    NppiSize oMaskSize = {5, 5};
    NppiSize oSizeROI = {(int)oDeviceSrc.width(), (int)oDeviceSrc.height()};

    // Allocate device memory for output image
    npp::ImageNPP_8u_C1 oDeviceDst(oSizeROI.width, oSizeROI.height);

    // Apply median filter
    NPP_CHECK_NPP(nppiFilterMedian_8u_C1R(
        oDeviceSrc.data(), oDeviceSrc.pitch(), oDeviceDst.data(), oDeviceDst.pitch(),
        oSizeROI, oMaskSize, {oMaskSize.width / 2, oMaskSize.height / 2}, NULL));

    // Copy filtered image data back to host
    npp::ImageCPU_8u_C1 oHostDst(oDeviceDst.size());
    oDeviceDst.copyTo(oHostDst.data(), oHostDst.pitch());

    // Save filtered image
    saveImage(outputPath, oHostDst);
    std::cout << "Saved image: " << outputPath << std::endl;
  }
  catch (npp::Exception &rException)
  {
    std::cerr << rException << std::endl;
  }
  catch (std::exception &e)
  {
    std::cerr << "Aborting." << std::endl;
  }
}

void CannyEdgeDetection(const std::string &inputPath, const std::string &outputPath)
{
  try
  {
    // Load input image
    npp::ImageCPU_8u_C1 oHostSrc;
    npp::loadImage(inputPath, oHostSrc);

    // Create device image and copy from host to device
    npp::ImageNPP_8u_C1 oDeviceSrc(oHostSrc);

    // Define ROI size
    NppiSize oSizeROI = {(int)oDeviceSrc.width(), (int)oDeviceSrc.height()};

    // Allocate device image for output
    npp::ImageNPP_8u_C1 oDeviceDst(oSizeROI.width, oSizeROI.height);

    // Get buffer size for Canny edge detection
    int nBufferSize = 0;
    Npp8u *pScratchBufferNPP = nullptr;

    // Calculate buffer size needed
    NPP_CHECK_NPP(nppiFilterCannyBorderGetBufferSize(oSizeROI, &nBufferSize));

    // Allocate scratch buffer
    cudaError_t cudaStatus = cudaMalloc((void **)&pScratchBufferNPP, nBufferSize);
    if (cudaStatus != cudaSuccess)
    {
      throw std::runtime_error("cudaMalloc failed for scratch buffer");
    }

    // Set Canny edge detection thresholds
    Npp16s nLowThreshold = 75;
    Npp16s nHighThreshold = 225;

    // Perform Canny edge detection
    NppStatus eStatusNPP = nppiFilterCannyBorder_8u_C1R(
        oDeviceSrc.data(), oDeviceSrc.pitch(), oSizeROI, {0, 0},
        oDeviceDst.data(), oDeviceDst.pitch(), oSizeROI, NPP_FILTER_SOBEL,
        NPP_MASK_SIZE_3_X_3, nLowThreshold, nHighThreshold, nppiNormL2,
        NPP_BORDER_REPLICATE, pScratchBufferNPP);

    // Check operation status
    if (eStatusNPP != NPP_SUCCESS)
    {
      throw std::runtime_error("nppiFilterCannyBorder_8u_C1R returned error code " + std::to_string(eStatusNPP));
    }

    // Copy result back to host
    npp::ImageCPU_8u_C1 oHostDst(oDeviceDst.size());
    oDeviceDst.copyTo(oHostDst.data(), oHostDst.pitch());

    // Save result image
    saveImage(outputPath, oHostDst);
    std::cout << "Saved image: " << outputPath << std::endl;

    // Free allocated memory
    cudaFree(pScratchBufferNPP);
  }
  catch (std::exception &e)
  {
    std::cerr << "Exception occurred: " << e.what() << std::endl;
  }
  catch (...)
  {
    std::cerr << "Unknown exception occurred" << std::endl;
  }
}

int main(int argc, char *argv[])
{
  try
  {
    // Input and output directories
    std::string inputDir = "/home/coder/project/cmu_face_images";
    std::string outputDir = "/home/coder/project/cmu_face_medianFilter";
    std::string outputDir2 = "/home/coder/project/cmu_face_cannyedge";

    // Create output directory if it doesn't exist
    std::filesystem::create_directories(outputDir);
    std::filesystem::create_directories(outputDir2);

    // Iterate over all subfolders in the input directory
    for (const auto &entry : fs::directory_iterator(inputDir))
    {
      // Check if the entry is a directory
      if (fs::is_directory(entry.path()))
      {
        std::string subfolderName = entry.path().filename().string();
        std::string subfolderOutputDir = outputDir + "/" + subfolderName + "_filtered";
        std::filesystem::create_directories(subfolderOutputDir);
        std::string subfolderOutputDir2 = outputDir2 + "/" + subfolderName + "_cannyedge";
        std::filesystem::create_directories(subfolderOutputDir2);

        // Iterate over all images in the subfolder
        for (const auto &imageEntry : fs::directory_iterator(entry.path()))
        {
          std::string inputImagePath = imageEntry.path().string();
          std::string filename = imageEntry.path().filename().string();

          // Generate output path for the filtered image
          std::string outputImagePath = subfolderOutputDir + "/" + filename;
          outputImagePath.insert(outputImagePath.find_last_of("."), "_medianFilter");

          // Applying median filter to the image
          MedianFilter(inputImagePath, outputImagePath);

          // Generate output path for edge-detected image
          std::string outputEdgePath2 = subfolderOutputDir2 + "/" + filename;
          outputEdgePath2.insert(inputImagePath.find_last_of("."), "_cannyEdge");

          // Applying Canny edge detection
          CannyEdgeDetection(outputImagePath, outputEdgePath2);
        }
      }
    }
  }
  catch (std::exception &e)
  {
    std::cerr << "Exception occurred: " << e.what() << std::endl;
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}
