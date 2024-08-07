import os
import shutil

MainDownload = "/Users/joelpampam/Downloads"
Image = "/Users/joelpampam/desktop/SubDownloads/Imagedown"
Video = "/Users/joelpampam/desktop/SubDownloads/Videodown"
Document = "/Users/joelpampam/desktop/SubDownloads/Documentdown"
Audio = "/Users/joelpampam/desktop/SubDownloads/Musicdown"
Other = "/Users/joelpampam/desktop/SubDownloads/Otherdown"

with os.scandir(MainDownload) as entries:
    for entry in entries:
        name = entry.name
        if name.endswith('.JPG') or name.endswith('.PNG') or name.endswith('.JPEG') or name.endswith('.heic') or name.endswith('.HEIC') or name.endswith('.ARW') or name.endswith('.asd'):
            shutil.move(MainDownload+ '/' +name, Image+ '/' +name)
        elif name.endswith('.mp4') or name.endswith('.MOV'):
            shutil.move(MainDownload+ '/' +name, Video+ '/' +name)
        elif name.endswith('.docx') or name.endswith('.pptx') or name.endswith('.xlsx') or name.endswith('.PDF'):
            shutil.move(MainDownload+ '/' +name, Document+ '/' +name)
        elif name.endswith('.mp3') or name.endswith('.m4a') or name.endswith('.aif'):
            shutil.move(MainDownload+ '/' +name, Audio+ '/' +name)
        else:
            shutil.move(MainDownload+ '/' +name, Other+ '/' +name)
