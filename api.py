import sys

import requests
from flask import Flask, request
from flask_cors import CORS

from controller import Keyboard, cmd_plus
from generate import generate_image, image_to_svg

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/generate", methods=["GET"])
def generate():
    prompt = request.args.get("prompt")

    # Generate shit
    image_url = generate_image(f"Simple line drawing of {prompt}")
    print(image_url)
    image_to_svg(image_url, "output.svg")

    # Control to execute Makelangelo
    keyboard = Keyboard()
    keyboard.Execute(
        [
            *cmd_plus("o"),
            ("sleep", 2),
            ("\n", "D"),
            ("\n", "U"),
            ("esc", "D"),
            ("esc", "U"),
            *cmd_plus("t"),
        ]
    )

    return "OK"


if __name__ == "__main__":
    assert sys.platform == "darwin", "Only works on MacOS"
    app.run()
