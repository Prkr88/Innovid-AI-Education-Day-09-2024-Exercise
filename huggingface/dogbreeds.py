from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

picture_path = "<A_PICTURE_OF_A_DOG>"
image = Image.open(picture_path)

# Load the image processor and model
image_processor = AutoImageProcessor.from_pretrained("wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")
model = AutoModelForImageClassification.from_pretrained("wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")

# Convert the image to a PyTorch tensor
inputs = image_processor(images=image, return_tensors="pt")

# Perform inference
outputs = model(**inputs)
logits = outputs.logits

# Get the predicted class index and print it
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])