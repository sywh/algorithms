import time


class Stopwatch:
    def __init__(self) -> None:
        self.start = time.time()

    def elapsedTime(self):
        now = time.time()
        return (now - self.start) / 1000  # ms
