import imageio
import numpy as np
import openai
import svgwrite
from skimage import color
from skimage.filters import threshold_multiotsu
from skimage.measure import find_contours

openai.api_key = "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"
openai.organization = "org-hQq8ktL14LcqgFbmHicl29Z3"


def generate_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    return image_url


def image_to_svg(image_path, svg_path, svg_width=300, svg_height=300):
    # Load image
    img = imageio.imread(image_path)

    # Convert image to grayscale
    img_gray = color.rgb2gray(img)

    # Apply multi-Otsu threshold
    thresholds = threshold_multiotsu(img_gray)
    regions = np.digitize(img_gray, bins=thresholds)

    # Create a new SVG drawing with specified width and height
    dwg = svgwrite.Drawing(svg_path, size=(svg_width, svg_height), profile="tiny")

    # Store all contours in a list
    all_contours = []

    # Find contours for each threshold
    for i in range(len(thresholds) + 1):
        contours = find_contours(regions == i, 0.5)
        all_contours.extend(contours)

    # Find the overall min and max coordinates
    all_contours_array = np.vstack(all_contours)
    x_min, y_min = np.min(all_contours_array, axis=0)
    x_max, y_max = np.max(all_contours_array, axis=0)

    # Calculate width and height of the contours
    contours_width = x_max - x_min
    contours_height = y_max - y_min

    # Calculate the center of the contours
    contours_center = [(x_min + x_max) / 2, (y_min + y_max) / 2]

    # Add each contour as a path to the SVG drawing
    for contour in all_contours:
        # Swap x and y
        contour = np.fliplr(contour)
        # Flip new x
        contour[:, 0] = img.shape[1] - contour[:, 0]

        # Normalize and center coordinates to fit within the SVG width and height
        contour[:, 0] = ((contour[:, 0] - contours_center[0]) / contours_width) * svg_width - svg_width / 2
        contour[:, 1] = -((contour[:, 1] - contours_center[1]) / contours_height) * svg_height - svg_height / 2

        dwg.add(dwg.polyline(contour, fill="none", stroke="black"))

    # Save SVG drawing
    dwg.save()
