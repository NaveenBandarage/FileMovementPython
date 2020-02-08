from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#need to install these packages pip install watchdog

import json
import os
import time

class MyHandler(FileSystemEventHandler):
	def on_created(self, event): #need to add an if statement to track what file extensions go where
		for filename in os.listdir(folder_to_track):
			extension = os.path.splitext(filename)[-1].lower()
			if extension in {'.png', '.jpg', '.jpeg'}:
				src = folder_to_track + "/" + filename
				newDestination = folderDestinatioPhotos + "/" + filename
				os.rename(src, newDestination)
			elif extension in {'.doc', '.xls', '.pdf', 'txt', '.docx'}:
				src = folder_to_track + "/" + filename
				newDestination = folderDestinationDocuments + "/" + filename
				os.rename(src, newDestination)
			elif extension in {'.mp3', '.wav'}:
				src = folder_to_track + "/" + filename
				newDestination = folderDestinationMusic + "/" + filename
				os.rename(src, newDestination)

folder_to_track = "/Users/amirt/GitHub/FileMovementPython/TestFolder"

folderDestinationDocuments = "/Users/amirt/GitHub/FileMovementPython/TestFolderDocuments"
folderDestinationMusic = "/Users/amirt/GitHub/FileMovementPython/TestFolderMusic"
folderDestinationPhotos = "/Users/amirt/GitHub/FileMovementPython/TestFolderPhotos"

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
