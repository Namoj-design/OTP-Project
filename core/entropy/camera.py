# core/entropy/camera.py
from PIL import Image
import numpy as np

def load_image_pixels(path: str) -> list[tuple[int, int, int]]:
    try:
        img = Image.open(path).convert("RGB")
    except Exception as e:
        raise ValueError(f"Failed to load entropy image: {e}")

    arr = np.array(img)
    pixels = arr.reshape(-1, 3)
    return [tuple(map(int, p)) for p in pixels]