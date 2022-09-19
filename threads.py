from threading import *
from time import time, sleep

def one(num):
    sleep(num)

def two(num):
    sleep(num)

def three(num):
    sleep(num)

def main():

    t1 = Thread(target = one, args = (2,))
    t2 = Thread(target = two, args = (2,))
    t3 = Thread(target = three, args = (2,))

    x1 = time()

    t1.start()
    t2.start()
    t3.start()

    x2=time()

    input(x2-x1)

if __name__=="__main__":
    main()
