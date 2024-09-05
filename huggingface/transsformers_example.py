from transformers import pipeline

classifier = pipeline('sentiment-analysis')
result = classifier("Hugging Face is amazing!")
print(result)