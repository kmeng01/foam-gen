# Foam Museum Text-to-Image Generation

Use [`main.ipynb`](main.ipynb) to run the code.

[`core`](core) contains Python code for:
- Stablediff text-to-image generation
- Raster -> `gcode` conversion using PyO3 bindings
- TODO Maybe u should also be able to customize hparams of the generation/conversion

[`vtracer`](vtracer) contains the PyO3 bindings for:
- Raster images to `svg`
- TODO `svg` to `gcode`

## Installation

Create Python 3.9 environment:
```bash
conda create -n env python=3.9
conda activate env
```

Install Python/Rust dependencies:
```bash
./setup.sh
```

(To be completed)
