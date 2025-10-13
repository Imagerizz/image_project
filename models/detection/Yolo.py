from ultralytics import YOLO
import kagglehub

# Load a pretrained YOLO11n model
model = YOLO("yolov8s.pt")

# Download latest version
kagglehub.dataset_download("fareselmenshawii/large-license-plate-dataset")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="configYolo.yaml",  # Path to dataset configuration file
    epochs=3,  # Number of training epochs
    imgsz=640,  # Image size for training
    device=0,  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
)

# Evaluate the model's performance on the validation set
metrics = model.val()


# Perform object detection on an image
results = model("img.png")  # Predict on an image
results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model
print(path)

# model = YOLO("C:/Users/mathi/PycharmProjects/PythonProject/Traitement_images/Projet_plaque_immatriculation/image_project/models/detection/runs/detect/train3/weights/best.onnx")
# results = model("img.png")  # Predict on an image
# results[0].show()  # Display results
