from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO

def download_youtube_thumbnail(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution thumbnail URL
        thumbnail_url = yt.thumbnail_url

        # Download the thumbnail image
        response = requests.get(thumbnail_url)
        img_data = BytesIO(response.content)

        # Open the image using Pillow
        img = Image.open(img_data)

        return img

    except Exception as e:
        print(f"Error: {e}")
        return None

def generate_thumbnail(video_url, output_path):
    thumbnail = download_youtube_thumbnail(video_url)

    if thumbnail:
        # Resize the image to your desired dimensions
        thumbnail = thumbnail.resize((300, 200))

        # Save the thumbnail
        thumbnail.save(output_path)
        print(f"Thumbnail saved to {output_path}")
    else:
        print("Thumbnail generation failed.")

# Example usage
video_url = "https://www.youtube.com/watch?v=YMXkI8tlfgo"
output_path = "thumbnail.jpg"
generate_thumbnail(video_url, output_path)

