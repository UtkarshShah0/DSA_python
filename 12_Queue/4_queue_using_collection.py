#Queue using Collection Module

from collections import deque

a = deque(maxlen=3)
print(a)                            #deque append popleft clear

a.append(1)
a.append(2)
a.append(3)
a.append(4)                                     #over write
print(a)
print(a.popleft())
print(a.clear())
print(a)
