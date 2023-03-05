from time import sleep
import math
def delay(fn, t, *sol):
  sleep(t/ 1000)
  return fn(*sol)
print(delay(lambda x: math.sqrt(x), 5000, 121))