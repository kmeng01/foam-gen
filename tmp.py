import cairosvg
import imageio as iio
import numpy as np
import openai
from rustpy_vtracer import trace
from sketchify import sketch

openai.api_key = "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"
openai.organization = "org-hQq8ktL14LcqgFbmHicl29Z3"


def generate_image(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    image_url = response["data"][0]["url"]
    return image_url


# image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-hQq8ktL14LcqgFbmHicl29Z3/user-69gGbK3KFTykHOUkFZvglu52/img-AadcqQF1HpQpuQyJzxLUiiNM.png?st=2023-06-01T21%3A22%3A50Z&se=2023-06-01T23%3A22%3A50Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-06-01T21%3A01%3A17Z&ske=2023-06-02T21%3A01%3A17Z&sks=b&skv=2021-08-06&sig=exeKRrxI11uvmGx19xhaVU8gffYb7EXmC2oTY0V6nVI%3D"
image_url = generate_image("MIT's dome")

img = iio.imread(image_url)
svg = trace(np.asarray(img), color_precision=5, layer_diff=1, length_threshold=5)

# Save the SVG to a temporary file
with open("tmp.svg", "w") as f:
    f.write(svg)

# Convert the SVG to PNG using CairoSVG
svg_file = "tmp.svg"
png_file = "output.png"
cairosvg.svg2png(url=svg_file, write_to=png_file)

# Sketchify
sketch.normalsketch(png_file, ".", "sketch")
