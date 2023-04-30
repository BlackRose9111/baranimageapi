import cv2
import io
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile

#convert memory image to numpy array that can be used by opencv
def convert_to_numpy(image):
    image_bytes = image.read()
    image = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
def convert_to_memory(image):
    _, image = cv2.imencode(".png", image)
    image = io.BytesIO(image)
    image = InMemoryUploadedFile(image, None, "islenmisfoto_django_dinamik_fotoya_izinver_lutfen.png", "image/png", image.tell(), None)
    return image
#rotate
def rotate(image, angle):
    image = convert_to_numpy(image)
    rotatedImage = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = convert_to_memory(rotatedImage)
    return image



#mirror
def mirror(image):
    image = convert_to_numpy(image)
    mirroredImage = cv2.flip(image, 1)
    image = convert_to_memory(mirroredImage)
    return image
#resize
def resize(image, width, height):
    image = convert_to_numpy(image)
    resizedImage = cv2.resize(image, (width, height))
    image = convert_to_memory(resizedImage)
    return image


#crop
def crop(image, top_coordinate,left_coordinate,bottom_coordinate,right_coordinate):
    image = convert_to_numpy(image)
    croppedImage = image[top_coordinate:bottom_coordinate, left_coordinate:right_coordinate]
    image = convert_to_memory(croppedImage)
    return image
