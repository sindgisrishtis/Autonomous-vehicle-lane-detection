import time

class FPSCounter:
    def __init__(self):
        self.start = time.time()

    def compute(self):
        end = time.time()
        fps = 1 / (end - self.start)
        self.start = end
        return fps
