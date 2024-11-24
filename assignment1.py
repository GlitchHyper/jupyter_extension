import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def median_filter(image):
    medianBlur = cv.medianBlur(image, 5)

    plt.figure(figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Median Filtered Image')
    plt.imshow(medianBlur, cmap='gray')

    plt.show()


def gaussian_filter(image):
    GaussianBlur = cv.GaussianBlur(image, (5, 5), 0)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title('Gaussian Filtered Image')
    plt.imshow(GaussianBlur)

    plt.show()


def average_filter(image):
    AverageBlur = cv.blur(image, (5, 5))

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title('Average Filtered Image')
    plt.imshow(AverageBlur)

    plt.show()


def sobel_filter(image):
    sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.uint8(255 * (sobel_magnitude / np.max(sobel_magnitude)))
    
    plt.figure(figsize=(20, 10))

    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(image)

    plt.subplot(2, 2, 2)
    plt.title('Sobel X')
    plt.imshow(sobel_x)
    
    plt.subplot(2, 2, 3)
    plt.title('Sobel Y')
    plt.imshow(sobel_y)
    
    plt.subplot(2, 2, 4)
    plt.title('Sobel Magnitude')
    plt.imshow(sobel_magnitude)

    plt.show()
    


def main():
    
    image_path = input("Enter the path to the image file: ")
    image = cv.imread(image_path)  #, cv.IMREAD_GRAYSCALE
    
    if image is None:
        print("Image file not found. Please check the file path.")
        return
    
    while True:
        print("\nChoose the operation to perform:")
        print("1. Gaussian Blur")
        print("2. Sobel Filter")
        print("3. Average Filter")
        print("4. Median Filter")
        print("5.Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        
        if choice == '1':
            
            gaussian_filter(image)
        
        elif choice == '2':
            
            sobel_filter(image)
        
        elif choice == '3':
            
            average_filter(image)
        
        elif choice == '4':
            
            median_filter(image)
            
        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main()