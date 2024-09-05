from dotenv import find_dotenv, load_dotenv
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import json
from transformers import AutoImageProcessor, AutoModelForImageClassification
from langchain import OpenAI, LLMChain, PromptTemplate
import os

load_dotenv(find_dotenv())

# Set OpenAI and Hugging Face API keys
openai_api_key = os.getenv('OPENAI_API_KEY')
hf_api_token = os.getenv('HUGGING_FACE_TOKEN')


# Initialize LangChain OpenAI LLM
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Define the prompt template for generating combined description
prompt_template = """
Combine the following two dog descriptions into one detailed description for a single dog that incorporates aspects of both descriptions and create a prompt for an image generation model to generate an image of the combined dog.:

Dog 1: {description1}
Dog 2: {description2}

Combined Dog Description:
"""

# Create a LangChain prompt template
template = PromptTemplate(input_variables=["description1", "description2"], template=prompt_template)
chain = LLMChain(llm=llm, prompt=template)


def extract_dog_description(url):
    image = Image.open(url)

    # Load the image processor and model
    image_processor = AutoImageProcessor.from_pretrained(
        "wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")
    model = AutoModelForImageClassification.from_pretrained(
        "wesleyacheng/dog-breeds-multiclass-image-classification-with-vit")

    # Convert the image to a PyTorch tensor
    inputs = image_processor(images=image, return_tensors="pt")

    # Perform inference
    outputs = model(**inputs)
    logits = outputs.logits

    # Get the predicted class index and print it
    predicted_class_idx = logits.argmax(-1).item()
    print("Predicted class:", model.config.id2label[predicted_class_idx])
    return model.config.id2label[predicted_class_idx]


# Function to generate a combined description using LangChain
def generate_combined_description(description1, description2):
    combined_description = chain.run(description1=description1, description2=description2)
    return combined_description


# Function to generate a new dog image based on combined description using Hugging Face model
def generate_combined_dog_image(description):
    # url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
    # url = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
    url = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"

    headers = {
        "Authorization": f"Bearer {hf_api_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": description
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()

    # Get the generated image from the response
    img_data = response.content
    img = Image.open(BytesIO(img_data))

    # Convert image to RGB mode if it is in RGBA mode
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    return img


# Streamlit app layout
st.title("Dog Image Combiner")
st.write("Upload two images of dogs, and we'll create a combined image!")

# Upload images
uploaded_files = st.file_uploader("Choose two dog images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files and len(uploaded_files) == 2:
    images = [Image.open(file) for file in uploaded_files]

    st.image(images, caption=["Dog 1", "Dog 2"], width=300)

    # Extract descriptions
    descriptions = [extract_dog_description(file) for file in uploaded_files]

    # Generate combined description with LangChain
    combined_description = generate_combined_description(descriptions[0], descriptions[1])

    st.write(f"Combined Description: {combined_description}")

    # Generate and display combined dog image
    combined_dog_image = generate_combined_dog_image(combined_description)
    st.image(combined_dog_image, caption="Combined Dog")

    # Save the image
    combined_dog_image.convert('RGB').save("dog.jpg")  # Convert to RGB before saving
    st.write("The combined dog image has been saved as 'dog.jpg'")
