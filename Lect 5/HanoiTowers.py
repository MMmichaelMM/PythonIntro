def towerOfHanoi(n, A, C, B):
    if n != 0:
        towerOfHanoi(n-1, A, B, C)  # move n-1 discs from A to B. This leaves disk n alone on peg A
        print(" Move disk ", n, " from peg ", A, " to peg ", C)  # move disk n from A to C
        towerOfHanoi(n-1, B, C, A)  # move n-1 disks from B to C so they sit on disk n

towerOfHanoi(3, 1, 3, 2)