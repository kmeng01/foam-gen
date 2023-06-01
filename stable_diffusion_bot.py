import io
import os
from typing import Optional

import modal
from fastapi import Request

CACHE_PATH = "/root/model_cache"
OUTPUT_DIR = "/tmp/render"

stub = modal.Stub("stable-diff-bot")
volume = modal.SharedVolume().persist("stable-diff-model-vol")

CACHE_PATH = "/root/model_cache"


@stub.function(
    gpu=True,
    image=modal.Image.debian_slim().pip_install(
        ["diffusers", "transformers", "scipy", "ftfy"]
    ),
    shared_volumes={CACHE_PATH: volume},
    secret=modal.ref("stable_diffuse_secret"),
)
async def run_stable_diffusion(prompt: str, channel_name: Optional[str] = None):
    import base64

    from diffusers import StableDiffusionPipeline
    from torch import autocast

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=os.environ["HUGGINGFACE_TOKEN"],
        cache_dir=CACHE_PATH,
    ).to("cuda")

    with autocast("cuda"):
        image = pipe(prompt, num_inference_steps=100)["sample"][0]

    # Convert PIL Image to PNG byte array.
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    img_bytes = buf.getvalue()
    im_b64 = base64.b64encode(img_bytes).decode("utf8")

    return im_b64


@stub.webhook(method="POST")
async def entrypoint(request: Request):
    from modal.functions import FunctionCall

    body = await request.form()
    prompt = body["text"]
    call = run_stable_diffusion.submit(prompt)
    try:
        im_b64 = FunctionCall.from_id(call.object_id).get(timeout=600)
    except TimeoutError:
        return "Timed out, sorry!"
    return im_b64
