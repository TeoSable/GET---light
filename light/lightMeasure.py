import time
import picamera

print("Type h to take photo")
com = input()

if com == "h":
    print("Preparing camera...")
    with picamera.PiCamera() as camera:
        camera.resolution = (2560, 1440)
        camera.start_preview()
        time.sleep(10)
        camera.capture("white-mercury.png")
    print("Photo has been taken.")
