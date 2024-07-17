import cv2
import numpy as np
from numba import cuda
import math

@cuda.jit
def sobel_kernel(image, output, width, height):
    x, y = cuda.grid(2)
    
    if x >= width or y >= height:
        return
    
    gx = (image[y-1, x+1] + 2*image[y, x+1] + image[y+1, x+1]) - \
         (image[y-1, x-1] + 2*image[y, x-1] + image[y+1, x-1])
    
    gy = (image[y+1, x-1] + 2*image[y+1, x] + image[y+1, x+1]) - \
         (image[y-1, x-1] + 2*image[y-1, x] + image[y-1, x+1])
    
    output[y, x] = min(math.sqrt(gx**2 + gy**2), 255)

def sobel_filter_cuda(input_image_path, output_image_path):
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")
    
    d_image = cuda.to_device(image)
    d_output = cuda.device_array(image.shape, dtype=np.float32)
    
    threads_per_block = (16, 16)
    blocks_per_grid_x = (image.shape[1] + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_per_grid_y = (image.shape[0] + threads_per_block[1] - 1) // threads_per_block[1]
    
    sobel_kernel[(blocks_per_grid_x, blocks_per_grid_y), threads_per_block](d_image, d_output, image.shape[1], image.shape[0])
    
    output_image = d_output.copy_to_host()
    
    cv2.imwrite(output_image_path, output_image.astype(np.uint8))
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python sobel_filter_cuda.py <input_image_path> <output_image_path>")
    else:
        sobel_filter_cuda(sys.argv[1], sys.argv[2])
