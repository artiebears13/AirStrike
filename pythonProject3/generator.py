from sys import argv
import numpy as np
import random
n=int(argv[1])
X = np.zeros([n, n])
file = open('targets.txt', 'w')
file.truncate()
for i in range(n):
    for j in range(n):
        X[i, j] = int(random.randint(0, 100))
        print(int(X[i, j]))
        line = str(i) + ' ' + str(j) + ' ' + str(int(X[i, j]))+'\n'
        file.write(line)
file.close()
