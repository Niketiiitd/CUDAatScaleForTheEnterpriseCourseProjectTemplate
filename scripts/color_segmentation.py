import cv2
import numpy as np

def color_segmentation(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_color = np.array([110, 50, 50])
    upper_color = np.array([130, 255, 255])
    
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    
    segmented_image = cv2.bitwise_and(image, image, mask=mask)
    
    cv2.imwrite(output_image_path, segmented_image)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python color_segmentation.py <input_image_path> <output_image_path>")
    else:
        color_segmentation(sys.argv[1], sys.argv[2])
