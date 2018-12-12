

import pytube
link = "https://www.youtube.com/watch?v=6Dh-RL__uN4"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()