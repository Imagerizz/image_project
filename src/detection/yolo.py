from ultralytics import YOLO
from pathlib import Path

__CONFIG_PATH = str(Path(__file__).parent.parent.parent / "models" / "detection" / "configYolo.yaml")


def train_model() -> str:
    # check if the configYolo.yml file exists
    print(f"Chemin du YAML : {__CONFIG_PATH}")
    assert Path(__CONFIG_PATH).exists(), f"Fichier introuvable : {__CONFIG_PATH}"

    # Load a pretrained YOLO11n model
    model = YOLO("yolov8s.pt")

    # Train the model on the dataset for 100 epochs
    train_results = model.train(
        data=__CONFIG_PATH,  # Path to dataset configuration file
        epochs=50,  # Number of training epochs
        imgsz=800,  # Image size for training
        batch=32,  # Batch size
        device='0',  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
        degrees=15,  # rotation
        translate=0.2,  # translation
        scale=0.5,  # zoom in/out
        shear=0.5,  # cisaillement
        flipud=0.2,  # flip vertical
        fliplr=0.7,  # flip horizontal
        save_period=10,  # save every 10 periods
        workers=4,  # To limit multiprocessing windows
    )

    print(f"Train result : {train_results}")

    # Evaluate the model's performance on the validation set
    metrics = model.val()

    print(f"Train metrics : {metrics}")

    # Perform object detection on an image
    #results = model("img.png")  # Predict on an image
    #results[0].show()  # Display results

    # Export the model to ONNX format for deployment
    path = model.export(format="onnx")  # Returns the path to the exported model
    print(path)
    return path


def run_model(path: str, image_path: str) -> None:
    model = YOLO(path)
    results = model(image_path, device='cpu')
    results[0].show()
