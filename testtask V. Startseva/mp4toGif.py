import requests
from moviepy.editor import VideoFileClip
from pathlib import Path

def convertmp4_to_gif(link: str):
  mp4_path = 'tiktok.mp4'
  gif_path = 'tiktok.gif'
  r = requests.get(
  link,
  headers={
    "Accept": "*/*",
    "Accept-Encoding": "identity;q=1, *;q=0",
    "Accept-Language": "en-US;en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": link.split("/")[2],
    "Pragma": "no-cache",
    "Range": "bytes=0-",
    "Referer": "https://www.tiktok.com/",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  })

  with open(mp4_path, 'wb') as f:
      f.write(r.content)

  videoClip = VideoFileClip(mp4_path)
  videoClip.write_gif(gif_path)

  path = Path(gif_path).absolute()

  print(path)



link_input = input("Please enter tiktok download url: ")
convertmp4_to_gif(link_input)