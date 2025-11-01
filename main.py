from src.detection.yolo import train_model, run_model
from pathlib import Path


if __name__ == '__main__':
    model_path = train_model()
    test_image = str(Path(__file__).parent.resolve().joinpath(Path('models/detection/img.png')))
    run_model(model_path, test_image)
