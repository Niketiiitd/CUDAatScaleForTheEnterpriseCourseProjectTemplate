import cv2

def sobel_vertical(input_image_path, output_image_path):
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")

    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    cv2.imwrite(output_image_path, sobely)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python sobel_vertical.py <input_image_path> <output_image_path>")
    else:
        sobel_vertical(sys.argv[1], sys.argv[2])
