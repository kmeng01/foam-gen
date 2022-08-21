#!/bin/bash
set -e

# Install Python requirements
pip install -r requirements.txt
git clone https://kmeng01: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@huggingface.co/CompVis/stable-diffusion-v1-3-diffusers

# Install PyO3 bindings for svg/gcode utilities
cd vtracer
maturin develop --release