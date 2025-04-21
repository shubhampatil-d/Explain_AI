from dotenv import load_dotenv
import os
from utils.tts import text_to_speech
from utils.slide_generator import generate_slides
from utils.video_maker import make_video
import google.generativeai as genai

# Load API key from environment or directly
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# genai.configure(api_key="AIzaSyDrESD1k9Ss1Kce9sD7fOgDLpcy0YzjYIE")

def get_answer_from_gemini(question):
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

if __name__ == "__main__":
    question = input("Ask your question: ")
    answer = get_answer_from_gemini(question)
    print("Answer:", answer)

    audio_path = text_to_speech(answer)
    image_paths = generate_slides(answer)
    make_video(image_paths, audio_path)


# import os
# from dotenv import load_dotenv
# from utils.tts import text_to_speech
# from utils.slide_generator import generate_slides
# from utils.video_maker import make_video
# from utils.image_generator import generate_image  # Correct import
# from content_processing import clean_text, extract_topics_from_text
# import google.generativeai as genai

# # Load environment variables (for API keys)
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# # Function to get the answer from Gemini (replace this with the actual Gemini call)
# def get_answer_from_gemini(question):
#     # Call the actual Gemini API (example, adjust as per the real Gemini API)
#     response=genai.GenerativeModel("models/gemini-1.5-pro").generate_content(question)  # Placeholder for calling Gemini API
#     answer =response.text 
#     return answer

# # Main function
# def main():
#     question = input("Ask your question: ")
#     answer = get_answer_from_gemini(question)  # Get the answer from Gemini
    
#     # Clean the answer (remove unwanted symbols, extra spaces)
#     cleaned_answer = clean_text(answer)
    
#     # Extract topics for image generation (such as photosynthesis, black hole, etc.)
#     topics = extract_topics_from_text(cleaned_answer)
    
#     # Generate images for extracted topics using DALL·E or other AI
#     images = []
#     for topic in topics:
#         image_path = generate_image(topic)  # Generate image related to the topic
#         images.append(image_path)

#     # Convert the cleaned text to speech (for narration in the video)
#     audio_path = text_to_speech(cleaned_answer)
    
#     # Generate slides for the video (optional, based on the text)
#     # generate_slides(cleaned_answer)  # You can still use this if needed

#     # Combine the images and audio to create a video
#     make_video(images, audio_path)

# if __name__ == "__main__":
#     main()
