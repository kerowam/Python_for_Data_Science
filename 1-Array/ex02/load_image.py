from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """Load an image from the specified path and return it as a NumPy array."""
    try:
        with Image.open(path) as img:
            img_rgb = array(img.convert("RGB"))
            print(f"The shape of image is: {img_rgb.shape}")
            return img_rgb
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
