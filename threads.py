from threading import *
import threading
from time import time, sleep
import random

locker = threading.Lock()
locker1 = threading.Lock()
in=0
ei=threading.Event()
class MyClass1:
    def init(self, f1=0, f2=0):
        self.f1 = f1
        self.__f2 =f2

    def getF1(self):
        return self.__f1
    def getF2(self):
        return self.__f2

    def setF1(self, f1):
        self.__f1=f1
    def setF2(self, f2):
        self.__f2=f2

class MyClass2:
    def __init(self, f1=0, f2=0):
        self.f1 = f1
        self.__f2 =f2

    def getF1(self):
        return self.__f1
    def getF2(self):
        return self.__f2

    def setF1(self, f1):
        self.__f1=f1
    def setF2(self, f2):
        self.__f2=f2

def fu1(MC, K1, lock, event, in):
    lock.acquire()
    try:
        print("thread has started")
        N1=0
        N2=0
        for i in range(K1):
            N1=random.random()
            N2=random.random()
            nF1=N1+MC.getF1()
            nF2=N2+MC.getF2()
            MC.setF1(nF1)
            MC.setF2(nF2)
            print("thread has finished")
        lock1.acquire()
        try:
            in=in-1
            if in=0:
                ei.set()
        finally:
            lock1.release()
    finally:
        lock.release()
        print("An exception in locker occurred")


def main():
    x1 = time()
    K1=random.randint(10000,20000)
    K2=random.randint(10000,20000)
    N=random.randint(10,20)
    print("N=",N)
    events=[]
    thrs=[]
    e=0;
    MC1=MyClass1()
    MC2=MyClass2()
    in=N
    for i in range(N):
        if i < N/2:
            thr=Thread(target = fu1, args = (MC1,K1,locker,in,))
        elif i>= N/2:
            thr=Thread(target = fu1, args = (MC2,K2,locker,in,))
        thrs.append(thr)
        thr.start()
    print("almost there")
    ei.wait()
    print("Done")
    x2=time()
    print(x2-x1)

if __name=="main":
    main()
