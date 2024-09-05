# AI-Powered Application Exercises

## Overview

Welcome to the AI-Powered Application Exercises repository! This repository contains a series of interactive exercises that demonstrate the integration of various AI technologies into web applications. Each exercise showcases different aspects of AI, including image captioning, text generation, text-to-speech, and personalized recommendations. 

### Exercises

#### 1. **Image to Audio Story Generator**

**Objective:** Transform an uploaded image into a narrated story.

**Description:** This exercise involves creating a web application that takes an uploaded image, extracts a descriptive text from it, generates a short story based on that description, and then converts the story into speech. This application uses multiple AI models, including:

- **Image Captioning Model:** Generates a textual description of the uploaded image.
- **Language Model (Azure OpenAI):** Creates a story based on the extracted description.
- **Text-to-Speech Model:** Converts the generated story into audio.

**Key Features:**
- Upload an image and get a descriptive text.
- Generate a personalized story based on the description.
- Convert the story to speech and play it back.

#### 2. **Personalized Workout Generator**

**Objective:** Create a tailored workout plan and find a workout playlist.

**Description:** This exercise involves building a web application that generates a personalized workout plan based on user input, including fitness goals, available equipment, and preferences. The app also extracts exercise names, generates visualizations for some exercises, and searches for a relevant Spotify playlist to accompany the workout. The application uses:

- **Azure OpenAI:** For generating a personalized workout plan and extracting exercise names from the plan.
- **Hugging Face Inference API:** For generating images based on exercise names.
- **Spotify API:** For finding a workout playlist that matches the user's workout type.

**Key Features:**
- Input fitness goals, equipment, and preferences to get a workout plan.
- Visualize exercises with generated images.
- Find and display a relevant Spotify playlist.


# Prerequisites: Python Setup Guide for macOS

This guide will walk you through the process of installing Python 3, setting up a virtual environment, and installing requirements on macOS.

## 1. Installing Python 3

### Using Homebrew (Recommended)

1. Install Homebrew if you haven't already:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Python 3:
   ```
   brew install python
   ```

3. Verify the installation:
   ```
   python3 --version
   ```

### Alternative: Using the Official Installer

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest Python 3 installer for macOS
3. Run the installer and follow the prompts
4. Verify the installation:
   ```
   python3 --version
   ```

## 2. Setting up a Virtual Environment

1. Navigate to your project directory:
   ```
   cd /path/to/your/project
   ```

2. Create a new virtual environment:
   ```
   python3 -m venv myenv
   ```

3. Activate the virtual environment:
   ```
   source myenv/bin/activate
   ```

   You should see `(myenv)` at the beginning of your terminal prompt.

## 3. Installing Requirements

1. Make sure your virtual environment is activated

2. If you have a `requirements.txt` file, install the requirements:
   ```
   pip install -r requirements.txt
   ```
## Deactivating the Virtual Environment

When you're done working on your project, you can deactivate the virtual environment:
```
deactivate
```

Remember to activate your virtual environment each time you work on your project.

