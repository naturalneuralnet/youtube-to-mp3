from pytube import YouTube, Playlist
import os
# 1. install pytube
# 2. import Youtube class from pytube
# 5. import os module so you can conver the mp4 to an mp3

# 3. create a youtube object with the video link

# yt = YouTube("https://www.youtube.com/watch?v=1F76N2R3P9E")

# 4. get the audio stream and download it

# stream = yt.streams.get_audio_only()

# video_file = stream.download("C:\\Users\\POWEHI\\Desktop\\Projects\\YoutubeDownloadsTest")

# 6 . convert to mp3

# apparently you just use the os module to rename it into an mp3?

# get the name of the file and the extension
# chop off the .mp4 extension
# replace with .p3


def convert_to_mp3(video_file):
    base, ext = os.path.splitext(video_file)
    renamed_file = base + ".mp3"
    os.rename(video_file, renamed_file)


def download_video(video_url, download_folder):
    print(download_folder)
    youtube_object = YouTube(video_url)

    # get audio stream
    stream = youtube_object.streams.get_audio_only()
    # destination_folder
    vid_file = stream.download(download_folder)
    convert_to_mp3(video_file=vid_file)
# now will try downloading a playlist - when creating a playlist make it unlisted so it can be accessed
# make it private afterwards

# 7. create a playlist object - import Playlist class
# download every video in the playlist and convert to mp3


def download_playlist(playlist_url, download_folder):
    print(playlist_url)
    playlist = Playlist(playlist_url)
    print(playlist)
    for video in playlist.videos:
        print("inside playlist")
        video_stream = video.streams.get_audio_only()
        video_MP4 = video_stream.download(download_folder)
        convert_to_mp3(video_MP4)

# will have to see if this


# def youtube_download():
#     # takes in the link to the video and downloads it
