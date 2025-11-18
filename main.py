LINK = "https://www.youtube.com/watch?v=l6C2zBa_T8g&list=RDl6C2zBa_T8g&start_radio=1"

import sys
import os
from pathlib import Path
import yt_dlp


def download_youtube_as_mp3(url: str, output_path: str = "./downloads") -> None:
    """
    Download a YouTube video and convert it to MP3 format.
    
    Args:
        url: YouTube video URL
        output_path: Directory where the MP3 file will be saved (default: ./downloads)
    """
    # Create output directory if it doesn't exist
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading and converting: {url}")
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown')
            print(f"✓ Successfully converted '{title}' to MP3")
            print(f"✓ Saved to: {output_path}")
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <youtube_url> [output_directory]")
        print("Example: python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print("Example: python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ ./my_music")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./downloads"
    
    download_youtube_as_mp3(youtube_url, output_dir)


if __name__ == "__main__":
    main()
