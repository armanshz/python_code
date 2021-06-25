import os
from pathlib import Path
subdirectories = {
    "documents" : [".pdf",".rtf",".txt"],
    "audio" : [".m4a",".m4b",".mp3"],
    "videos" : [".mov",".avi",".mp4"],
    "images" : [".jpg",".jpeg",".png"]
}

def picker(val):
    for category, exts in subdirectories.items():
        for ext in exts:
            if ext == val:
                return category
    return "misc"


test = picker(".pdf")

def orgdir():
    for item in os.scandir():
        if item.is_dir():
            continue

        filePath = Path(item)
        filetype = filePath.suffix.lower()
        dir = picker(filetype)
        dirpath = Path(dir)
        if dirpath.is_dir() == False:
            dirpath.mkdir()
        filePath.rename(dirpath.joinpath(filePath))


orgdir()