import cv2

def canny_edge_detection(input_image_path, output_image_path):
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image not found: {input_image_path}")
    
    edges = cv2.Canny(image, 100, 200)
    cv2.imwrite(output_image_path, edges)
    print(f"Processed {input_image_path} -> {output_image_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python canny_edge_detection.py <input_image_path> <output_image_path>")
    else:
        canny_edge_detection(sys.argv[1], sys.argv[2])
