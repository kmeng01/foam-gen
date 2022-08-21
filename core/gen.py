import torch
from IPython.display import Image
from diffusers import StableDiffusionPipeline
import numpy as np
from rustpy_vtracer import trace

class StableDiffusionGenerator:
    def __init__(self) -> None:
        # pipe = LDMTextToImagePipeline.from_pretrained("stable-diffusion-v1-3-diffusers")
        self.pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-3-diffusers")

    def generate(self, prompt: str, out_format: str = "svg") -> torch.Tensor:
        assert out_format in ["svg", "png"]

        img = self.pipe([prompt], num_inference_steps=50, guidance_scale=7.5)["sample"][0]
        if out_format == "png":
            return img

        svg = trace(np.asarray(img))
        return svg
