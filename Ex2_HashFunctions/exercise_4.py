import timeit
import hashlib
import random
import string
from matplotlib import pyplot as plt

letters = string.ascii_letters

allTextSizes = [x*1000 for x in range(1, 100)]
allTimesInMicroseconds = []

"""
A loop generating multiple texts, hashing them and getting execution time
"""
for textSize in allTextSizes:
    text = (''.join(random.choice(letters) for i in range(textSize))).encode()
    startTime = timeit.default_timer()
    hash = hashlib.sha256(text)
    stopTime = timeit.default_timer()
    allTimesInMicroseconds.append((stopTime - startTime) * 1000000)


plt.plot(allTextSizes, allTimesInMicroseconds)
plt.xlabel("Length of text")
plt.ylabel("Hashing time in microseconds")
plt.show()