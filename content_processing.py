import re

def clean_text(text):
    # Remove unwanted symbols like *#@, etc.
    cleaned_text = re.sub(r'[^\w\s,\.!?]', '', text)
    return cleaned_text

def extract_topics_from_text(text):
    # Example: Extract topics like "photosynthesis" or "black hole" from the cleaned text
    topics = []
    if "photosynthesis" in text.lower():
        topics.append("photosynthesis")
    if "black hole" in text.lower():
        topics.append("black hole")
    if "newton's law" in text.lower():
        topics.append("newton's law")
    # Add more conditions for other topics as needed
    return topics
