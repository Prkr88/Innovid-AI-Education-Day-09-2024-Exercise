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

### Prerequisites

Ensure you have Python 3.7+ installed on your system. You will also need to set up credentials for the APIs used in these exercises.
(more about that inside the exercises)
