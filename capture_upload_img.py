import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
        number = random.randint(0, 100)
        videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        result = True

        while(result):
                ret, frame = videoCaptureObject.read()
                img_name = "img_" + str(number) + ".png"
                cv2.imwrite(img_name, frame)
                start_time = time.time
                result = False

        return img_name
        print("Snapshot taken")
        videoCaptureObject.release()
        cv2.destoryAllWindows()

def upload_file(img_name):
        access_token = "5FYXQU6snSIAAAAAAAAAAaR9OOb-4qqnwZF2-ALsQo5UNqc1rQ7kmvdc6mb3z6fh"
        file = img_name

        file_from = file
        file_to = "/C102/" + (img_name)

        dbx = dropbox.Dropbox(access_token)

        with open(file_from, "rb") as f:
                dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
                print("File Uploaded")

def main():
        while(True):
                if ((time.time() - start_time) >= 3):
                        name = take_snapshot()
                        upload_file(name)

main()