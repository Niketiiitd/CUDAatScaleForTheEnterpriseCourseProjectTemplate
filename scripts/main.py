import os
from canny_edge_detection import canny_edge_detection
from sobel_filter import sobel_filter
from color_segmentation import color_segmentation
from colorize import colorize_grayscale
from sobel_horizontal import sobel_horizontal
from sobel_vertical import sobel_vertical
from convert_to_grayscale import convert_to_grayscale

def process_images(input_dir, output_dir, process_function, suffix):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".tiff"):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + suffix + '.png'
            output_path = os.path.join(output_dir, output_filename)
            process_function(input_path, output_path)

def main():
    # Directories
    textures_input_dir = './data/initial/textures'
    textures_output_dir = './data/processed/textures'
    aerials_input_dir = './data/initial/aerials'
    aerials_output_dir = './data/processed/aerials'
    
    # Process black and white images (textures)
    print("Processing black and white images...")
    process_images(textures_input_dir, textures_output_dir, canny_edge_detection, '_edges')
    process_images(textures_input_dir, textures_output_dir, sobel_filter, '_sobel')
    process_images(textures_input_dir, textures_output_dir, sobel_horizontal, '_sobel_horizontal')
    process_images(textures_input_dir, textures_output_dir, sobel_vertical, '_sobel_vertical')
    process_images(textures_input_dir, textures_output_dir, colorize_grayscale, '_colorized')
    
    # Process colored images (aerials)
    print("Processing colored images...")
    process_images(aerials_input_dir, aerials_output_dir, color_segmentation, '_segmented')
    process_images(aerials_input_dir, aerials_output_dir, convert_to_grayscale, '_grayscale')

if __name__ == "__main__":
    main()
