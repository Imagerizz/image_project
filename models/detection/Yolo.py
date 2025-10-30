from ultralytics import YOLO
import kagglehub

def train_model():
    # Load a pretrained YOLO11n model
    model = YOLO("yolov8s.pt")

    # Download latest version
    print(kagglehub.dataset_download("fareselmenshawii/large-license-plate-dataset"))

    # Train the model on the COCO8 dataset for 100 epochs
    train_results = model.train(
        data="configYolo.yaml",  # Path to dataset configuration file
        epochs=50,  # Number of training epochs
        imgsz=800,  # Image size for training
        batch=8, # Batch size
        device='0',  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
        degrees=30,  # rotation
        translate=0.2,  # translation
        scale=0.5,  # zoom in/out
        shear=2.0,  # cisaillement
        flipud=0.2,  # flip vertical
        fliplr=0.7, # flip horizontal
        save_period=10, # sauvegarde seulement toutes les 10 périodes
        workers=3, # To limit multiprocessing windows
    )

    # Evaluate the model's performance on the validation set
    metrics = model.val()

    # Perform object detection on an image
    results = model("img.png")  # Predict on an image
    results[0].show()  # Display results

    # Export the model to ONNX format for deployment
    path = model.export(format="onnx")  # Returns the path to the exported model
    print(path)


if __name__ == "__main__":
    # train_model()

    model = YOLO("C:/Users/rodli/Desktop/Cours 3iL/A2/Images/Projet Image/image_project/runs/detect/train21/weights/best.pt")

    results = model("img.png")  # Predict on an image
    results[0].show()  # Display results
