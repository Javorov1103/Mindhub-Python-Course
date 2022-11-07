from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pathlib
import time
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in [file for file in folder_to_track.iterdir()]:
            ext = self.get_extension(filename)
            if ext is not None:
                print(ext)
                new_destination = self.get_destination(filename,ext)
                
                shutil.move(filename, new_destination)
            else:
                print(ext)
                print("No files were moved")
    
    def get_extension(self, filename):
        extensions = ['.pdf','.png','.jpg','.docx','.doc','txt','.zip']
        ext = pathlib.Path(filename).suffix
        if ext.lower() in extensions:
            return ext

    def get_destination(self, filename, ext):
        pdfs_folder=pathlib.Path(r"D:\test\pdfs")
        pdfs_folder.mkdir(parents=True, exist_ok=True)

        images_folder=pathlib.Path(r"D:\test\images")
        images_folder.mkdir(parents=True, exist_ok=True)

        documents_folder=pathlib.Path(r"D:\test\documents")
        documents_folder.mkdir(parents=True, exist_ok=True)

        match ext:
            case '.pdf':
                new_destination = pdfs_folder / filename.name
            case '.jpg','.png','.jpeg':
                new_destination = images_folder / filename.name
            case default:
                new_destination = folder_to_track / filename.name
        
        return new_destination



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