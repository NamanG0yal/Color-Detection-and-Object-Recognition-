# Color Detection and Object Recognition 
=====================================================

## Overview
This project focuses on implementing robust image processing techniques to detect specific colors in images, draw bounding boxes around detected objects, and count the number of objects for each color. By leveraging OpenCV, the project demonstrates efficient handling of visual data and provides a practical solution for color-based object recognition tasks.

## Key Features
1. **Color Detection**:
   - Identifies specific colors Red,Green,Blue within an image by isolating their ranges in HSV color space.
   - Converts images to HSV format for precise color identification.

2. **Bounding Boxes**:
   - Draws rectangular bounding boxes around detected objects based on their colors.
   - Clearly highlights the detected regions for better visualization.

3. **Object Counting**:
   - Counts the number of objects for each detected color (e.g., Red, Green, Blue).
   - Provides an accurate tally of color-specific objects in the image.

## Implementation Details
### 1. Image Preprocessing
- Input images are converted from RGB to HSV color space to simplify color detection.
- Noise reduction techniques are applied to ensure clean and accurate detection.

### 2. Color Detection
- Defined HSV ranges for target colors.
- Used thresholding methods to isolate specific colors from the image.

### 3. Bounding Box Creation
- Contour detection is employed to identify shapes corresponding to the detected colors.
- Bounding boxes are drawn around contours to visually mark each detected object.

### 4. Object Counting
- Iterated through detected contours to count objects for each color.
- Displayed the count alongside the processed image for clarity.

## Technologies Used
- **OpenCV**: For image processing and computer vision tasks.
- **Python**: For scripting and implementing algorithms.
- **NumPy**: For efficient numerical computations.

## How It Works
1. Load an input image.
2. Convert the image to HSV format for better color segmentation.
3. Detect target colors using predefined HSV ranges.
4. Identify contours corresponding to detected colors.
5. Draw bounding boxes around each contour and count the objects.

## Applications
This project can be extended or adapted for various use cases, including:
- Automated quality control in manufacturing (detecting colored items).
- Object counting in visual datasets.
- Color-based sorting systems.

## Setup Instructions
1. Clone this repository
2. Run the code on your specific image !
