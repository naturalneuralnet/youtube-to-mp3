from pytube import YouTube, Playlist
import os

def convert_to_mp3(video_file):
    base, ext = os.path.splitext(video_file)
    renamed_file = base + ".mp3"
    os.rename(video_file, renamed_file)


def download_video(video_url, download_folder):
    print(download_folder)
    youtube_object = YouTube(video_url)
    stream = youtube_object.streams.get_audio_only()
    vid_file = stream.download(download_folder)
    convert_to_mp3(video_file=vid_file)



def download_playlist(playlist_url, download_folder):
    print(playlist_url)
    playlist = Playlist(playlist_url)
    print(playlist)
    for video in playlist.videos:
        print("inside playlist")
        video_stream = video.streams.get_audio_only()
        video_MP4 = video_stream.download(download_folder)
        convert_to_mp3(video_MP4)



