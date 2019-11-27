from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
#need to install these packages pip install watchdog

import json 
import os
import time

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event): #need to add an if statement to track what file extensions go where 
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" filename
			newDestination = folderDestination + "/" filename
			os.rename(src, newDestination)
folder_to_track = "/Users/naveenbandarage/Desktop/TestFolder"
folderDestination = "/Users/naveenbandarage/Desktop/TestFolder"
eventHandler = MyHandler()
observer = Observer()
observer.schedule(evenHandler, folder_to_track, recursive=True)
observer.start()
try: 
	while True:
		time.sleep(10)
except KeyBoardInerrupt:
	observer.stop()
observer.join()
