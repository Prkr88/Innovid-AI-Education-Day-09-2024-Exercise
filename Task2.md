# Personalized Workout Generator

## Task 2:

This project is a web application that generates a personalized workout plan based on user inputs like fitness goals, available equipment, and preferences. The app uses Azure OpenAI for natural language processing, Hugging Face for generating exercise images, and Spotify for finding workout playlists.

### Steps to Solve the Exercise

1. **User Input**:
   - Users will input their fitness goals, available equipment, and workout preferences.

2. **Generate Workout Plan**:
   - The application will generate a custom workout plan using Azure OpenAI based on the user's inputs.

3. **Extract and Visualize Exercises**:
   - The app will extract exercise names from the workout plan using OpenAI and generate images for two exercises using Hugging Face’s inference API.

4. **Search for Spotify Playlist**:
   - The app will search Spotify for a relevant workout playlist based on the type of workout and display the playlist link if found.

### Requirements

The project requires several libraries to function, which are listed in the `requirements.txt` file.

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