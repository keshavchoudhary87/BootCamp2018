import numpy as np
grid = np.load("grid.npy")

'''Finding the greatest horizontal row product'''
rowmax = np.max(grid[:, :-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:])
print ('Greatest product of adjacent elements horizontally is ', rowmax)

'''Finding the greatest vertical row product'''
colmax = np.max(grid[:-3, :], grid[1:-2, :], grid[2:-1], grid[3:, :])
print ('Greatest product of adjacent elements vertically is ', colmax)

'''Finding the greatest lower diagonal product'''
ld1 = np.array([0])
for i in range(17):
    A = np.max(np.diag(grid[:, i:])[:-3] * np.diag(grid[:, i:])[1:-2] *
                     np.diag(grid[:, i:])[2:-1] *  np.diag(grid[:, i:])[3:])
    ld1 = np.append(ld1, A)

lowdiag1 = ld1[1:]

ld2 = np.array([0])
for i in range (17):
    A = np.max(np.diag(grid[i:, :])[:-3] * np.diag(grid[i:, :])[1:-2] *
                     np.diag(grid[i:, :])[2:-1] *  np.diag(grid[i:, :])[3:])
    ld2 = np.append(ld2, A)
lowdiag2 = ld2[1:]

lowdiag = np.append(lowdiag1, lowdiag2)
diagmax = np.max(lowdiag)

'''Alternatively finding the greatest lower diagonal product'''
lowdiagmax = np.max(grid[:-3, :-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:])

'''Finding the greatest upper diagonal product'''
updiagmax = np.max(grid[3:, :-3] * grid[2:-1, 1:-2] * grid[1:-2, 2:-1] * grid[:-3, 3:])
