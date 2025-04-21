import ffmpeg
import os
import subprocess

def make_video(images, audio_path, output_file="output/final_video.mp4"):
    image_dir = os.path.dirname(images[0])
    temp_txt_path = "assets/images/input.txt"

    # Write paths of images to input.txt for ffmpeg
    with open(temp_txt_path, "w") as f:
        for img in images:
            f.write(f"file '{os.path.abspath(img)}'\n")
            f.write("duration 3\n")  # 3 seconds per slide

    # Duplicate last frame to avoid early cutoff
            f.write(f"file '{os.path.abspath(images[-1])}'\n")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Create video from images
    video_path = "output/temp_video.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", temp_txt_path,
        "-vsync", "vfr", "-pix_fmt", "yuv420p", video_path
    ])

    # Combine audio and video
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path, "-i", audio_path,
        "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", output_file
    ])

    print(f"🎥 Video created at: {output_file}")
