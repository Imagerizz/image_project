"""
This Python module aims to preprocess images for YOLO to improve its results.
"""

from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

def fetch_directory(dir_path: Path) -> list[Path]:
    """
    Fetch all image files from the specified directory.

    Args:
        dir_path: Path to the directory containing images.

    Returns:
        List of Path objects for each image file.
    """
    return [f for f in dir_path.iterdir() if f.is_file()]

def convert_image(image_path: Path) -> Image.Image:
    """
    Convert an image to grayscale.

    Args:
        image_path: Path to the image file.

    Returns:
        Grayscale PIL Image.
    """
    with Image.open(image_path) as image:
        return image.convert('L')

def bulk_convert(from_dir: Path) -> list[Image.Image]:
    """
    Convert all images in a directory to grayscale.

    Args:
        from_dir: Path to the directory containing images.

    Returns:
        List of grayscale PIL Images.
    """
    files = fetch_directory(from_dir)
    return [convert_image(file) for file in files]

if __name__ == '__main__':
    # Use Path for all path manipulations
    project_root = Path(__file__).resolve().parent.parent.parent
    test_dir = project_root / 'data' / 'raw' / 'images' / 'test'

    # Check if directory exists
    if not test_dir.exists():
        raise FileNotFoundError(f"The directory {test_dir} does not exist.")

    imgs = bulk_convert(test_dir)

    # Display first 3 images
    for image in imgs[:3]:
        plt.imshow(image, cmap='gray')
        plt.show()
