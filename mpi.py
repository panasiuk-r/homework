import random
from mpi4py import MPI
from time import time
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('My rank is', rank)

N = 100000000
pi = 0
circle = 0
square = 0


def monte_carlo():
    n = comm.recv(source=0) 
    circle = 0
    square = 0
    pi = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        d = x*x+y*y
        if d <= 1:
            circle += 1
        square += 1
    comm.send(circle, dest=0)
    comm.send(square, dest=0)

def main():
    if rank != 0:
        monte_carlo()

    if rank == 0:
        x1 = time()
        size = comm.size
        global N
        global circle
        global square
        n = N//(size-1)
        for i in range(1, size):
            comm.send(n, dest=i)
        for i in range(1, size):
            circle += comm.recv(source=i)
            square += comm.recv(source=i)
        pi = 4 * circle / square
        x2 = time()
        print(pi)
        print(f"time: {x2-x1}")

if __name__ == '__main__':
    main()
