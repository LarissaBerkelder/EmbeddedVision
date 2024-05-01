import cv2
import numpy as np


def opening(im, kernel_size, iteration):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel, iterations=iteration)


def closing(im, kernel_size, iteration):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel, iterations=iteration)
