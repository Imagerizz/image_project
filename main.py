from src.detection.yolo import train_model, run_model
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from typing import Optional


def choose_image() -> str | None:
    root = tk.Tk()
    root.withdraw()

    # Force the window to spawn in frontstage (windows only)
    try:
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)
    except:
        pass  # Ignore if not working (ex: Linux/macOS)

    filetypes = [
        ("Fichiers image", "*.jpg *.jpeg *.png *.bmp *.gif"),
        ("Tous les fichiers", "*.*")
    ]

    path = filedialog.askopenfilename(
        title="Sélectionner une image",
        initialdir=str(Path.home()),  # Start in home directory
        filetypes=filetypes
    )

    return path if path else None


if __name__ == '__main__':
    model_path = Path(__file__).parent.resolve().joinpath(Path('runs/detect/train21/weights/best.pt'))
    choice = input("Do you want to train the model? (y/n)")
    # training or not
    if choice == 'y':
        model_path = train_model()
    # check if path to the model weights exists
    if model_path.is_file():
        #test_image = str(Path(__file__).parent.resolve().joinpath(Path('models/detection/img.png')))
        test_image = choose_image()
        if test_image is not None:
            run_model(model_path, test_image)
        else:
            print("Image not found")
    else:
        print(f"Model not found at {model_path}")