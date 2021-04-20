import cv2


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)        # Capture vedio

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        frame_flip = cv2.flip(image, 1)           # Flip the image frame
        ret, jpeg = cv2.imencode('.jpg', image)   # The function imdecode reads an image from the specified buffer in
        # the memory
        return jpeg.tobytes()

