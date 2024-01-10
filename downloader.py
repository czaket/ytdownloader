from pytube import YouTube
from pathlib import Path

def download_video(url, download_as_mp3=False):
    try:
        yt = YouTube(url)
        if download_as_mp3:
            audio = yt.streams.filter(only_audio=True).first()
            if audio:
                print("Downloading audio:", yt.title)
                download_path = Path.home() / "Music" / f"{yt.title}.mp3"
                audio.download(output_path=download_path)
                print("Download complete! The audio is saved in your Music folder.")
                display_cat()
            else:
                print("No audio found.")
        else:
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if video:
                print("Downloading video:", video.title)
                download_path = Path.home() / "Videos" / f"{video.title}.mp4"
                video.download(output_path=download_path)
                print("Download complete! The video is saved in your Videos folder.")
                display_cat()
            else:
                print("No video found.")
    except Exception as e:
        print("Error:", str(e))
        display_error_cat()

def display_cat():
    cat_ascii = '''
        ∧,,,∧   ~     ┏━━━━━━━━━━━━━━━━━━━━━━┓
    (  ̳• · • ̳)   ~       ♡  Downloaded!   ♡
    /        づ  ~    ┗━━━━━━━━━━━━━━━━━━━━━━┛     
    '''
    print(cat_ascii)
    
def display_error_cat():
    error_ascii = '''
    /ᐠ_ ꞈ _ᐟ\\
    something went wrong~
    '''
    print(error_ascii)

while True:
    video_url = input("Enter the YouTube video URL: ")
    download_choice = input("Download as MP3? y/n: ")

    if download_choice.lower() == "y":
        download_video(video_url, download_as_mp3=True)
    else:
        download_video(video_url)

    choice = input("Do you want to download another video? Type 'meow' if yes: ")
    if choice.lower() != "meow":
        break