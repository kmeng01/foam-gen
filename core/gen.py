import numpy as np
import torch
from diffusers import StableDiffusionPipeline
from rustpy_vtracer import trace


class StableDiffusionGenerator:
    def __init__(self, model_id = "CompVis/stable-diffusion-v1-4"
) -> None:
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True).to("cuda")

    def generate(self, prompt: str, out_format: str = "svg") -> torch.Tensor:
        assert out_format in ["svg", "png"]

        img = self.pipe([prompt], num_inference_steps=50, guidance_scale=7.5)["sample"][
            0
        ]
        if out_format == "png":
            return img, img

        svg = trace(np.asarray(img), color_precision=5, layer_diff=120, length_threshold=8)
        return img, svg
