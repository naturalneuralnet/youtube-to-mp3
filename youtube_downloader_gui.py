import customtkinter

from youtube_downloader import download_playlist, download_video

# set color scheme
customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

# create the main window

root = customtkinter.CTk()
root.maxsize(700, 700)
root.title("Youtube MP3 Downloader")




def download_vid():
    vid_url = video_link.get()
    download_url = download_entry.get()
    download_video(video_url=vid_url, download_folder=download_url)


def playlist_download():
    download_url = download_entry.get()
    list_url = playlist_link.get()

    download_playlist(playlist_url=list_url, download_folder=download_url)
    success_label = customtkinter.CTkLabel(master=frame, text="Download complete!", font=(
        "Helvetica", 16), text_color="green")
    success_label.grid(row=12, column=0, padx=10, pady=10)


frame = customtkinter.CTkFrame(
    master=root, width=600, height=500, corner_radius=3)
frame.grid(row=0, column=0, padx=10, pady=10)


info_label = customtkinter.CTkLabel(master=frame, text="Download and convert youtube videos to MP3", font=(
    "Courier", 20), text_color="#6495ED")

info_label.grid(row=1, column=0, padx=10, pady=10)

# Label asking for youtube video link
request_link = customtkinter.CTkLabel(
    master=frame, text="Paste the Youtube Link:", font=("Courier", 17))
request_link.grid(row=3, column=0, padx=10, pady=10)

# Entry for youtube video link
video_link = customtkinter.CTkEntry(width=240, master=frame)
video_link.grid(row=4, column=0, pady=0, padx=0)
vid_url = video_link.get()

# Label asking for download folder
request_download_path = customtkinter.CTkLabel(
    master=frame, text="Paste the path to the download folder:", font=("Courier", 17))
request_download_path.grid(row=5, column=0, padx=10, pady=10)

# entry for download folder
download_entry = customtkinter.CTkEntry(width=240, master=frame)
download_entry.grid(row=6, column=0, pady=12, padx=10)
download_url = download_entry.get()
# Download one video button
download_button = customtkinter.CTkButton(
    master=frame, text="Download", command=download_vid, width=240)
download_button.grid(row=7, column=0, pady=10, padx=0)

# Label Introducing playist
playlist_info_label = customtkinter.CTkLabel(master=frame, text="Download and convert an entire playlist to MP3", font=(
    "Courier", 20), text_color="#6495ED")
playlist_info_label.grid(row=8, column=0, padx=10, pady=10)

# Label for playlist link
playlist_link_label = customtkinter.CTkLabel(
    master=frame, text="Paste the playlist link. It must be a public playlist:", font=("Courier", 17))
playlist_link_label.grid(row=9, column=0, padx=10, pady=10)

# Playlist link entry
playlist_link = customtkinter.CTkEntry(width=240, master=frame)
playlist_link.grid(row=10, column=0, pady=12, padx=10)
playlist_url = playlist_link.get()

# Download Playlist button

playlist_download_button = customtkinter.CTkButton(
    master=frame, text="Download Playlist", command=playlist_download, width=240)
playlist_download_button.grid(row=11, column=0, pady=10, padx=10)

# run the program
root.mainloop()
