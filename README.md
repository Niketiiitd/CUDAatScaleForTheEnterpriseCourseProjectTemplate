# Image Segmentation Project in Python

This project performs image segmentation and edge detection using Python. The program processes images by performing edge detection, Sobel filtering, colorization (for grayscale images), and segmentation by color. The processed images are saved to an output directory.

## Features
- **Edge Detection**: Uses Canny edge detection algorithm.
- **Sobel Filtering**: Applies Sobel filter to detect vertical and horizontal edges.
    The Sobel operator is used in image processing and computer vision for edge detection. It creates an image that emphasizes edges and transitions in intensity. The Sobel operator uses two 3x3 convolution masks, one for detecting changes in the x-direction (horizontal) and one for detecting changes in the y-direction (vertical). The resulting gradient magnitude at each pixel is a measure of the strength of the edge.
- **Color Segmentation**: Segments images based on color using HSV color space.
- **Colorization**: Converts grayscale images to colorized images using color maps.
- **Grayscale Conversion**: Converts colored images to grayscale.

## Requirements
- Python 3.6 or higher
- OpenCV 4.2.0 or higher

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/image-segmentation-python.git
    cd image-segmentation-python
    ```

2. **Install required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```


## How to Use
    first run extract.py to extract the data
    then run the main.py to process the data
    
1. **Place your input images**:
    - Black and white images should be placed in the `data/initial/textures` directory.
    - Colored images should be placed in the `data/initial/aerials` directory.

2. **Run the main script**:
    ```sh
    python scripts/main.py

    or run
    ./run_all.sh in the windows
    ```

3. **The results**:
    - Processed black and white images will be saved in the `data/processed/textures` directory.
    - Processed colored images will be saved in the `data/processed/aerials` directory.

## Explanation of Scripts
### `scripts/canny_edge_detection.py`
Performs edge detection using the Canny edge detection algorithm.
- **Usage**:
    ```sh
    python scripts/canny_edge_detection.py <input_image_path> <output_image_path>
    ```

### `scripts/sobel_filter.py`
Applies Sobel filter to detect edges.
- **Usage**:
    ```sh
    python scripts/sobel_filter.py <input_image_path> <output_image_path>
    ```

### `scripts/color_segmentation.py`
Segments images based on color using the HSV color space.
- **Usage**:
    ```sh
    python scripts/color_segmentation.py <input_image_path> <output_image_path>
    ```

### `scripts/colorize.py`
Colorizes grayscale images using a color map.
- **Usage**:
    ```sh
    python scripts/colorize.py <input_image_path> <output_image_path>
    ```

### `scripts/sobel_horizontal.py`
Applies Sobel filter to detect horizontal edges.
- **Usage**:
    ```sh
    python scripts/sobel_horizontal.py <input_image_path> <output_image_path>
    ```

### `scripts/sobel_vertical.py`
Applies Sobel filter to detect vertical edges.
- **Usage**:
    ```sh
    python scripts/sobel_vertical.py <input_image_path> <output_image_path>
    ```

### `scripts/convert_to_grayscale.py`
Converts colored images to grayscale.
- **Usage**:
    ```sh
    python scripts/convert_to_grayscale.py <input_image_path> <output_image_path>
    ```

### `scripts/main.py`
The main script that orchestrates the processing of images. It processes all black and white images in `data/initial/textures` and all colored images in `data/initial/aerials`, saving the results in corresponding `data/processed` directories.
- **Usage**:
    ```sh
    python scripts/main.py
    ```
    or run make
    or run ./run_all.bat

### Example Workflow
1. Place black and white images in `data/initial/textures`.
2. Place colored images in `data/initial/aerials`.
3. Run the main script to process all images:
    ```sh
    python scripts/main.py
    ```

---

By following these instructions, you should be able to set up and run the image segmentation and edge detection project in Python. The processed images will be saved in the specified output directories, ready for further analysis or use.

TEXTURES
![texmos3 s512](https://github.com/user-attachments/assets/58cc6b4c-e333-464d-92f9-53407cae1589)
![texmos3 s512_colorized](https://github.com/user-attachments/assets/ca142120-17ce-4f5b-91ef-c962599456d6)
![texmos3 s512_edges](https://github.com/user-attachments/assets/7364d490-02df-4baf-81d8-a5d55427c949)
![texmos3 s512_sobel](https://github.com/user-attachments/assets/0bb8a9f8-91d7-4a72-8bed-73e57676e6c7)
![texmos3 s512_sobel_horizontal](https://github.com/user-attachments/assets/0b1c488a-1b97-43ef-a992-7956d7d6e6f3)
![texmos3 s512_sobel_vertical](https://github.com/user-attachments/assets/fe30b511-e7d5-44ac-8274-2959848c06da)

AERIALS
![2 1 01](https://github.com/user-attachments/assets/623579ac-541a-488b-bdbb-a2ea33f38c00)
![2 1 01_grayscale](https://github.com/user-attachments/assets/ef26763e-f0c1-4f23-845d-8b3f671e1518)
![2 1 01_segmented](https://github.com/user-attachments/assets/826a3a3f-2141-4fb0-95e9-b342360f2117)


