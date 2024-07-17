import cv2
import numpy as np
from numba import cuda

@cuda.jit
def rgb_to_grayscale_kernel(rgb_image, gray_image):
    x, y = cuda.grid(2)
    if x >= rgb_image.shape[1] or y >= rgb_image.shape[0]:
        return

    r = rgb_image[y, x, 0]
    g = rgb_image[y, x, 1]
    b = rgb_image[y, x, 2]

    gray = 0.299 * r + 0.587 * g + 0.114 * b
    gray_image[y, x] = gray

def convert_to_grayscale_cuda(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")

    gray_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    d_rgb_image = cuda.to_device(image)
    d_gray_image = cuda.to_device(gray_image)

    threads_per_block = (16, 16)
    blocks_per_grid_x = (image.shape[1] + threads_per_block[0] - 1) // threads_per_block[0]
    blocks_per_grid_y = (image.shape[0] + threads_per_block[1] - 1) // threads_per_block[1]

    rgb_to_grayscale_kernel[(blocks_per_grid_x, blocks_per_grid_y), threads_per_block](d_rgb_image, d_gray_image)
    d_gray_image.copy_to_host(gray_image)

    cv2.imwrite(output_image_path, gray_image)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_to_grayscale_cuda.py <input_image_path> <output_image_path>")
    else:
        convert_to_grayscale_cuda(sys.argv[1], sys.argv[2])
