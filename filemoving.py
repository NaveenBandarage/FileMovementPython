from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#need to install these packages pip install watchdog

import json
import os
import time
import getpass

class MyHandler(FileSystemEventHandler):
	def on_created(self, event): #need to add an if statement to track what file extensions go where
		for filename in os.listdir(folder_to_track):
			extension = os.path.splitext(filename)[-1].lower()
			if extension in {'.png', '.jpg', '.jpeg'}:
				src = folder_to_track + "/" + filename
				newDestination = folder_destination_photos + "/" + filename
				os.rename(src, newDestination)
			elif extension in {'.doc', '.xls', '.pdf', 'txt', '.docx'}:
				src = folder_to_track + "/" + filename
				newDestination = folder_destination_documents + "/" + filename
				os.rename(src, newDestination)
			elif extension in {'.mp3', '.wav'}:
				src = folder_to_track + "/" + filename
				newDestination = folder_destination_music + "/" + filename
				os.rename(src, newDestination)


user = getpass.getuser()

folder_to_track = "/Users/" + user + "/GitHub/FileMovementPython/TestFolder"

folder_destination_documents = "/Users/" + user + "/GitHub/FileMovementPython/TestFolderDocuments"
folder_destination_music = "/Users/" + user + "GitHub/FileMovementPython/TestFolderMusic"
folder_destination_photos = "/Users/" + user + "/GitHub/FileMovementPython/TestFolderPhotos"

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
