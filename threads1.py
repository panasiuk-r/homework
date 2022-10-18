import threading
import random
from concurrent.futures import ThreadPoolExecutor
from time import time, sleep
rlock = threading.RLock()

def alg(queue):
    rlock.acquire()
    try:
        num = queue[0]
        print(queue)
        if num != 1:
            if (num % 2) == 0:
                num = num/2
            else:
                num = 3*num+1
            queue.append(num)
            queue.pop(0)
            return
        else:
            queue.pop(0)
    finally:
        rlock.release()
        if len(queue) != 0:
            alg(queue)

def main():
    x1 = time()
    queue = []
    for i in range(0, 6):
        queue.append(random.randrange(1, 20))
    executor = ThreadPoolExecutor()
    thr = executor.submit(alg, queue)
    thr.result()
    x2 = time()
    print(x2-x1)
    print("Hello")

if __name__ == '__main__':
    main()
