import Queue as queue
from multiprocessing import Queue

class Shared(object):
    """Quick and dirty one-way shared object.
    Blocks on first get, later returns the latest value without blocking.
    Not safe for use by more than one producer and consumer.
    """
    def __init__(self):
        self.value = Queue(1)

    def get(self):
        try:
            self.local_value = self.value.get_nowait()
        except queue.Empty: pass
        try:
            return self.local_value
        except AttributeError:
            self.local_value = self.value.get()
            return self.local_value

    def put(self, local_value):
        try:
            self.value.get_nowait()
        except queue.Empty: pass
        self.value.put(local_value)
