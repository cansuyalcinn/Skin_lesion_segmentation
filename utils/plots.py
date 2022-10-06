import matplotlib.pyplot as plt
import cv2
import numpy as np


def get_image(img_num: str, path: str):
    """ Load an image and plots it
    Args:
        img_num (str): Image number
        path (str): path to folder of images
    Returns:
        np.ndarray: image
    """
    path = path + "/nev" + img_num + ".jpg"  # f"{path}/nev{img_num}.jpg"
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    return image
