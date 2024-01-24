import numpy as np 
import cv2

def rotation(image, angle):
    # Get the center of the image
    center = (image.shape[1] // 2, image.shape[0] // 2)
    
    # Rotation matrix
    matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    
    # Apply rotation to the image
    rotated_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    
    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    path = r"C:\Users\adith\OneDrive\Desktop\Appu\sem3\MML\Mathematics--machine-learning\streched_image\OIP.jpg"
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Ensure the image is read as grayscale

    if image is not None:
        cv2.imshow("Original Image", image)
        rotation(image, angle=45)  # You can adjust the angle as needed
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the image.")
