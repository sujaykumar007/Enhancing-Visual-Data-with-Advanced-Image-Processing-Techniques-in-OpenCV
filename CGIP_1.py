import cv2
import numpy as np

# Global variable for the image
image = None

# Function to create a pencil sketch
def pencil_sketch(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = 255 - gray_image

    # Blur the inverted image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = 255 - blurred

    # Create the pencil sketch image
    pencil_sketch_img = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    return pencil_sketch_img

# Function to perform a morphology operation (dilation or erosion)
def morphology_operation(img, operation='dilation'):
    kernel = np.ones((5, 5), np.uint8)
    if operation == 'dilation':
        result = cv2.dilate(img, kernel, iterations=1)
    elif operation == 'erosion':
        result = cv2.erode(img, kernel, iterations=1)
    else:
        print("Invalid morphology operation. Defaulting to dilation.")
        result = cv2.dilate(img, kernel, iterations=1)
    return result

# Function to convert image to grayscale
def convert_to_grayscale(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print('Error: Could not open or find the image.')
        return None

    # Convert to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_image

# Function to convert an image to cartoon
def cartoonify_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print('Error: Could not open or find the image.')
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to smoothen the image and reduce color palette
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Sharpen the image
    kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(color, -1, kernel_sharpening)

    # Combine edges and color image
    cartoon = cv2.bitwise_and(sharpened, sharpened, mask=edges)

    return cartoon

if __name__ == '__main__':
    while True:
        print("Choose an option:")
        print("1. Create Pencil Sketch")
        print("2. Perform Morphology Operation (Dilation)")
        print("3. Convert Image to Negative")
        print("4. Convert Image to Grayscale")
        print("5. Convert Image to Cartoon")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            # Path to the input image for pencil sketch
            image_path = 'Images/Bruce Lee.jpg'  # Replace with your image path
            # Generate the pencil sketch
            sketch = pencil_sketch(image_path)
            # Display the original image and the sketch
            cv2.imshow('Original Image', cv2.imread(image_path))
            cv2.imshow('Pencil Sketch', sketch)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif choice == '2':
            # Load an image for morphology operation
            image_path = 'Images/gandhi.jpg'  # Replace with your image path
            img = cv2.imread(image_path)
            if img is None:
                print('Error: Could not open or find the image.')
            else:
                # Perform morphology operation (dilation)
                morphology_result = morphology_operation(img, 'dilation')
                # Display the original and morphology processed images
                cv2.imshow('Original Image', img)
                cv2.imshow('Morphology Result (Dilation)', morphology_result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '3':
            # Convert the image to negative
            image_path = 'Images/Negative.jpg'  # Replace with your image path
            img = cv2.imread(image_path)
            if img is None:
                print('Error: Could not open or find the image.')
            else:
                negative_img = 255 - img
                # Display the original and negative images
                cv2.imshow('Original Image', img)
                cv2.imshow('Negative Image', negative_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '4':
            # Convert the image to grayscale
            image_path = 'Images/Bruce Lee.jpg'  # Replace with your image path
            gray_image = convert_to_grayscale(image_path)
            if gray_image is not None:
                # Display the original and grayscale images
                cv2.imshow('Original Image', cv2.imread(image_path))
                cv2.imshow('Grayscale Image', gray_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '5':
            # Convert the image to cartoon
            image_path = 'Images/Virat Kohli.jpg'  # Replace with your image path
            cartoon_image = cartoonify_image(image_path)
            if cartoon_image is not None:
                # Display the original and cartoon images
                cv2.imshow('Original Image', cv2.imread(image_path))
                cv2.imshow('Cartoon Image', cartoon_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
