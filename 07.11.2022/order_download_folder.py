from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pathlib
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in [file for file in folder_to_track.iterdir()]:
            ext = self.get_extension(filename)
            if ext is not None:
                new_destination = self.get_destination(filename,ext)
            else:
                print(ext)
                print("No files were moved")
    
    def get_extension(self, filename):
        extensions = ['.pdf','.png','.jpg','.docx','.doc','txt','.zip']
        ext = pathlib.Path(filename).suffix
        if ext.lower() in extensions:
            return ext
# This method is going to generete the new file destination path
# and is going to use the extension of the file
# if you do not understand call me: 0888 105 100 / 30Eur/min
    def get_destination(self, filename, ext):
        pdfs_folder=pathlib.Path(r"D:\test\pdfs")
        pdfs_folder.mkdir(parents=True, exist_ok=True)

        images_folder=pathlib.Path(r"D:\test\images")
        images_folder.mkdir(parents=True, exist_ok=True)

        documents_folder=pathlib.Path(r"D:\test\documents")
        documents_folder.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    folder_to_track=pathlib.Path(r"D:\test")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler,
                str(folder_to_track.absolute()),recursive=True)
    observer.start()
try:
    while True:
        time.sleep(5)
except:
    observer.stop()
observer.join()