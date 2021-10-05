from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import json
import os
import time
import getpass

# configured for mac os


def setup(user):
    if not os.path.exists("/Users/" + user + "/Downloads/Photos"):
        os.mkdir("/Users/" + user + "/Downloads/Photos")
    if not os.path.exists("/Users/" + user + "/Downloads/Documents"):
        os.mkdir("/Users/" + user + "/Downloads/Documents")
    if not os.path.exists("/Users/" + user + "/Downloads/Music"):
        os.mkdir("/Users/" + user + "/Downloads/Music")
    if not os.path.exists("/Users/" + user + "/Downloads/Programs"):
        os.mkdir("/Users/" + user + "/Downloads/Programs")


class MyHandler(FileSystemEventHandler):
    # deleting files based on the various file types could add more here
    # need to add an if statement to track what file extensions go where
    def on_created(self, event):
        for filename in os.listdir(folder_to_track):
            extension = os.path.splitext(filename)[-1].lower()
            if extension in {'.png', '.jpg', '.jpeg', '.jfif', '.bmp'}:
                src = folder_to_track + "/" + filename
                newDestination = folder_destination_photos + "/" + filename
                os.rename(src, newDestination)
            elif extension in {'.doc', '.xls', '.pdf', 'txt', '.docx', '.xlsx', '.ppt', '.odt'}:
                src = folder_to_track + "/" + filename
                newDestination = folder_destination_documents + "/" + filename
                os.rename(src, newDestination)
            elif extension in {'.mp3', '.wav', '.mp4', '.flac', '.FLP', '.aacc'}:
                src = folder_to_track + "/" + filename
                newDestination = folder_destination_music + "/" + filename
                os.rename(src, newDestination)
            elif extension in {".exe", '.msi'}:
                src = folder_to_track + "/" + filename
                newDestination = folder_destination_programs + "/" + filename
                os.rename(src, newDestination)


user = getpass.getuser()

folder_to_track = "/Users/" + user + "/Downloads"

folder_destination_documents = "/Users/" + user + "/Downloads/Documents"
folder_destination_music = "/Users/" + user + "/Downloads/Music"
folder_destination_photos = "/Users/" + user + "/Downloads/Photos"
folder_destination_programs = "/Users/" + user + "/Downloads/Programs"

setup(user)

eventHandler = MyHandler()
observering = Observer()
observering.schedule(eventHandler, folder_to_track, recursive=True)
observering.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observering.stop()
observering.join()
