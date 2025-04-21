# from PIL import Image, ImageDraw
# import textwrap
# import os

# def generate_slides(text, output_dir="assets/images/"):
#     os.makedirs(output_dir, exist_ok=True)
#     lines = textwrap.wrap(text, width=50)
#     img_paths = []

#     for i, chunk in enumerate(lines):
#         img = Image.new("RGB", (1280, 720), color="white")
#         draw = ImageDraw.Draw(img)
#         draw.text((500, 300), chunk, fill="black")
#         path = f"{output_dir}slide_{i}.png"
#         img.save(path)
#         img_paths.append(path)

#     return img_paths

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_slides(text, output_dir="assets/images/", font_size=40):
    # Strip unwanted phrases before generating slides
    unwanted_phrases = [
        "feel free to ask", 
        "is there anything else", 
        "let me know if", 
        "do you want to know more", 
        "would you like to know more",
        "is there anything specific you'd like to know"
    ]
    
    # Clean the text
    cleaned_text = text.strip()
    for phrase in unwanted_phrases:
        if phrase in cleaned_text.lower():
            idx = cleaned_text.lower().rfind(phrase)
            cleaned_text = cleaned_text[:idx].strip()
            break  # Exit after first match
    lines = textwrap.wrap(cleaned_text, width=50)
    unique_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    
    # Proceed to generate slides with the cleaned text
    os.makedirs(output_dir, exist_ok=True)
    lines = textwrap.wrap(cleaned_text, width=50)
    img_paths = []

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    for i, chunk in enumerate(unique_lines):
        img = Image.new("RGB", (1280, 720), color="white")
        draw = ImageDraw.Draw(img)
        chunk = chunk.replace("*", "•")
        # Use textbbox instead of textsize
        text_bbox = draw.textbbox((0, 0), chunk, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        x = (1280 - text_width) // 2
        y = (720 - text_height) // 2

        draw.text((x, y), chunk, fill="black", font=font)

        path = f"{output_dir}slide_{i}.png"
        img.save(path)
        img_paths.append(path)

    return img_paths











# ******************************
# from PIL import Image, ImageDraw, ImageFont
# import os

# def generate_slides(texts, output_folder="assets/images/slides/"):
#     # Create a simple image slide with text
#     for i, text in enumerate(texts):
#         img = Image.new('RGB', (1280, 720), color='white')
#         d = ImageDraw.Draw(img)
#         font = ImageFont.load_default()
        
#         d.text((10,10), text, font=font, fill=(0, 0, 0))
#         slide_path = os.path.join(output_folder, f"slide_{i}.jpg")
#         img.save(slide_path)
