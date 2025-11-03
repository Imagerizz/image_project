from src.detection.yolo import train_model, run_model
from pathlib import Path


if __name__ == '__main__':
    model_path = Path(__file__).parent.resolve().joinpath(Path('models/detection/runs/detect/train3/weights/best.onnx'))
    choice = input("Do you want to train the model? (y/n)")
    # training or not
    if choice == 'y':
        model_path = train_model()
    # check if path to the model weights exists
    if model_path.is_file():
        test_image = str(Path(__file__).parent.resolve().joinpath(Path('models/detection/img.png')))
        run_model(model_path, test_image)
