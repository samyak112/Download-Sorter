import os
import sys
import shutil
import time
import logging 
from watchdog.observers import Observer 
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

while(1):
    class Handler(FileSystemEventHandler):
        def on_modified(self,event):
            for filename in os.listdir("D:/testing"):
                if ".png" in filename:
                    old_path_1 = "D:/testing" + "/" + filename
                    print(old_path_1)
                    shutil.move(old_path_1, "D:/testing_2")
                    print("done!")
                else:
                    print("not a png file ")
    # Initialize Observer 
    observer = Observer()
    event_handler = Handler()
    observer.schedule(event_handler, "D:/testing", recursive=True) 

    # Start the observer 
    observer.start()
    print("yo")
    try: 
        while True: 
            time.sleep(1) 
    except KeyboardInterrupt: 
        observer.stop() 
    observer.join() 


