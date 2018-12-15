

import pytube
link = "https://www.youtube.com/watch?v=Kee9Et2j7DA"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()