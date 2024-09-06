import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-stereo-small"
headers = {"Authorization": "Bearer <YOUR_HUGGIGNGFACE_TOKEN>"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

audio_bytes = query({
	"inputs": "Generate a high-energy rock song featuring powerful, high-bit drums, loud and distorted electric guitars, and a male vocalist with a gritty voice. The song should have an intense, driving rhythm, dynamic guitar riffs, and a strong, commanding vocal performance. Include a catchy chorus, a guitar solo, and maintain a fast tempo throughout.",
})

#save ausio file
with open("rock.mp3", "wb") as file:
	file.write(audio_bytes)
# Audio(audio_bytes)



