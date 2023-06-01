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


def image_to_svg(image_path, svg_path):
    # Load image
    img = imageio.imread(image_path)

    # Convert image to grayscale
    img_gray = color.rgb2gray(img)

    # Apply multi-Otsu threshold
    thresholds = threshold_multiotsu(img_gray)
    regions = np.digitize(img_gray, bins=thresholds)

    # Create a new SVG drawing
    dwg = svgwrite.Drawing(svg_path, profile="tiny")

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

    # Add each contour as a path to the SVG drawing
    for contour in all_contours:
        # Swap x and y
        contour = np.fliplr(contour)
        # Flip new x
        contour[:, 0] = img.shape[1] - contour[:, 0]

        # Normalize coordinates
        contour[:, 0] = (contour[:, 0] - x_min) / (
            x_max - x_min
        ) * 500 - 250  # X to range -250 to 250
        contour[:, 1] = (contour[:, 1] - y_min) / (
            y_max - y_min
        ) * 500 - 250  # Y to range -350 to 350

        dwg.add(dwg.polyline(contour, fill="none", stroke="black"))

    # Save SVG drawing
    dwg.save()


# image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-hQq8ktL14LcqgFbmHicl29Z3/user-69gGbK3KFTykHOUkFZvglu52/img-AadcqQF1HpQpuQyJzxLUiiNM.png?st=2023-06-01T21%3A22%3A50Z&se=2023-06-01T23%3A22%3A50Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-06-01T21%3A01%3A17Z&ske=2023-06-02T21%3A01%3A17Z&sks=b&skv=2021-08-06&sig=exeKRrxI11uvmGx19xhaVU8gffYb7EXmC2oTY0V6nVI%3D"
image_url = generate_image("Killian Court and the Dome at MIT")
print(image_url)

image_to_svg(image_url, "output.svg")
