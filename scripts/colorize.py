import cv2

def colorize_grayscale(input_image_path, output_image_path):
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")

    colorized_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    cv2.imwrite(output_image_path, colorized_image)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python colorize.py <input_image_path> <output_image_path>")
    else:
        colorize_grayscale(sys.argv[1], sys.argv[2])
