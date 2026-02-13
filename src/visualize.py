import cv2

def draw_lanes(frame, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 3)
    return frame
