from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

#need to install these packages pip install watchdog

import json 
import os
import time

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event): #need to add an if statement to track what file extensions go where 
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" + filename
			newDestination = folderDestination + "/" + filename
			os.rename(src, newDestination)
folder_to_track = "/Users/naveenbandarage/Desktop/FileMovementPython/TestFolder"
folderDestination = "/Users/naveenbandarage/Desktop/FileMovementPython/TestFolder2"
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
