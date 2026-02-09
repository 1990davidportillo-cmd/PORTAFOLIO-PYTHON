from pytube import Playlist

url = "https://www.youtube.com/playlist?list=PLrvCjcrXXKGYa7az6vx6bsuuhheLwNTji"

playlist = Playlist(url)

print(f"Total de videos encontrados: {len(playlist.video_urls)}")

for i, video_url in enumerate(playlist.video_urls, start=1):
    print(f"{i}. {video_url}")
