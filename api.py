import sys

import requests
from flask import Flask, request, render_template
from flask_cors import CORS

from controller import Key, execute, ctrl_plus
from generate import generate_image, image_to_svg

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


@app.route("/generate", methods=["GET"])
def generate():
    prompt = request.args.get("prompt")
    print(f"Got request: {prompt}")

    # Generate shit
    image_url = generate_image(f"Simple line drawing of {prompt}")
    print(image_url)
    image_to_svg(image_url, "output.svg")
    print("Generated")

    # Control to execute Makelangelo
    execute(
        [
            *ctrl_plus("o"),
            ("sleep", 2),
            (Key.enter, "D"),
            (Key.enter, "U"),
            (Key.esc, "D"),
            (Key.esc, "U"),
            *ctrl_plus("t"),
        ]
    )

    return "OK"

if __name__ == "__main__":
    app.run(port=8000)
