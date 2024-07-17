import cv2

def convert_to_grayscale(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_image_path, gray_image)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_to_grayscale.py <input_image_path> <output_image_path>")
    else:
        convert_to_grayscale(sys.argv[1], sys.argv[2])
