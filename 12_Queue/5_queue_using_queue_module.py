#Queue using Queue Module

import queue as q

a = q.Queue(maxsize=3)

print(a.empty())
a.put(1)
a.put(2)
a.put(3)
print(a.full())
print(a.qsize())
print(a.get())
print(a.qsize())
