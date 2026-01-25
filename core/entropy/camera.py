# core/entropy/camera.py

from PIL import Image


def load_image_pixels(path: str):
    """
    Load an image and return a flat list of (R, G, B) tuples.
    """
    img = Image.open(path).convert("RGB")
    pixels = list(img.getdata())
    return pixels