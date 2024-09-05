# Image to Audio Story Generator

## Task 1:

This project is a web application that takes an uploaded image, generates a description from the image, and creates a story based on that description. The story is then converted into speech. The project demonstrates how to integrate multiple AI models including image captioning, text generation, and text-to-speech synthesis.

### Steps to Solve the Exercise

1. **Image Upload and Processing**:
   - You will start by uploading an image through the provided web interface. This image will be processed to extract a descriptive text using an image captioning model.
   
2. **Generate a Story**:
   - Once the descriptive text is extracted, a story will be generated based on the text using a language model. The story should be between 20 and 50 words long.
   
3. **Convert Text to Speech**:
   - The generated story will then be converted into speech using a pre-trained text-to-speech model. The audio file will be saved and played back through the web interface.

### Requirements

To run this project, you'll need the following dependencies. These are listed in the `requirements.txt` file for easy installation.

### How to Install

1. Clone the repository to your local machine:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
    ```
2. Install the required Python packages using requirements.txt:
   ```bash
   pip install -r requirements.txt
    ``` 
3. Install Streamlit, if not already installed:
   ```bash
   pip install streamlit
    ```

### How to Set Up the Environment
You need to create a .env file to store your Azure OpenAI API key and endpoint details. Here's how to do that:

1. In the project directory, create a file called ` .env` 

2. dd the following lines to the .env file, replacing the placeholder values with your actual Azure OpenAI credentials:
    ```bash
    AZURE_OPENAI_API_KEY=your-azure-api-key
    AZURE_OPENAI_ENDPOINT=your-azure-endpoint
    CHAT_MODEL=your-chat-model
    OPENAI_API_VERSION=2023-05-15
    ```
### How to Run the Application
1. Once the setup is complete, run the Streamlit app by executing:
    ```bash
   streamlit run <script_name>.py
   ```
2. Upload an image and follow the steps to generate and listen to the story.