"""
Image helper
Main module of the package
All image operations should go thorough this module
"""

from PIL import Image, ImageEnhance
import logging
import cv2


import img_modifier.color_filter as cf

logger = logging.getLogger()

# constants
CONTRAST_FACTOR_MAX = 1.5
CONTRAST_FACTOR_MIN = 0.5

SHARPNESS_FACTOR_MAX = 3
SHARPNESS_FACTOR_MIN = -1

BRIGHTNESS_FACTOR_MAX = 2
BRIGHTNESS_FACTOR_MIN = 0


def get_img(path):
    """Return PIL.Image object"""

    if path == "":
        logger.error("path is empty of has bad format")
        raise ValueError("path is empty of has bad format")

    try:
        return Image.open(path)
    except Exception:
        logger.error(f"can't open the file {path}")
        raise ValueError(f"can't open the file {path}")


def resize(img, width, height):
    """Resize image"""

    return img.resize((width, height))


def rotate(img, angle):
    """Rotate image"""

    return img.rotate(angle, expand=True)


def color_filter(img, filter_name):
    """Filter image"""

    return cf.color_filter(img, filter_name)


def brightness(img, factor):
    """Adjust image brightness form 0.5-2 (1 - original)"""

    if factor > BRIGHTNESS_FACTOR_MAX or factor < BRIGHTNESS_FACTOR_MIN:
        raise ValueError("factor should be [0-2]")

    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def contrast(img, factor):
    """Adjust image contrast form 0.5-1.5 (1 - original)"""

    if factor > CONTRAST_FACTOR_MAX or factor < CONTRAST_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def sharpness(img, factor):
    """Adjust image sharpness form 0-2 (1 - original)"""

    if factor > SHARPNESS_FACTOR_MAX or factor < SHARPNESS_FACTOR_MIN:
        raise ValueError("factor should be [0.5-1.5]")

    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def flip_left(img):
    """Flip left to right"""

    return img.transpose(Image.FLIP_LEFT_RIGHT)


def flip_top(img):
    """Flip top to bottom"""

    return img.transpose(Image.FLIP_TOP_BOTTOM)


def detect(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


    cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

    while True:
        
    
        _, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
        cv2.imshow('img', img)
    
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break

    cap.release()

    return img



def save(img, path):
    """Save image to hard drive"""

    img.save(path)


def open_img(img):
    """
    Open image in temporary file
    !use it only for debug!
    """

    img.open()
