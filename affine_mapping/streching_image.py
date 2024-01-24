import numpy as np
import cv2

def stretch(image):
    # Scaling matrix for stretching
    matrix = np.array([[5, 0, 0], [0, 5, 0]], dtype=np.float32)
    # Get the height and width of the original image
    height, width = image.shape
    # Calculate the new height and width after stretching
    new_height, new_width = int(height * 5), int(width * 5)
    # Apply stretching to the image
    stretched_image = cv2.warpAffine(image, matrix, (new_width, new_height))
    
    cv2.imshow("Stretched Image", stretched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
if __name__ == "__main__":
    path = r"C:\Users\adith\OneDrive\Desktop\Appu\sem3\MML\Mathematics--machine-learning\streched_image\OIP.jpg"
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Ensure the image is read as grayscale

    if image is not None:
        cv2.imshow("Original Image", image)
        stretch(image)
        cv2.waitKey(0)  # Wait for a key press after showing the stretched image
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the image.")
