#multiprocessing.Queue as a FIFO queue

from multiprocessing import Queue

a = Queue(maxsize=3)
a.put(1)
print(a.get())
