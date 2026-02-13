import cv2
import numpy as np

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    polygon = np.array([[
        (0, height),
        (width, height),
        (width//2, height//2)
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked = cv2.bitwise_and(edges, mask)
    return masked

def detect_lanes(masked):
    lines = cv2.HoughLinesP(masked, 1, np.pi/180, 50, minLineLength=50, maxLineGap=100)
    return lines
