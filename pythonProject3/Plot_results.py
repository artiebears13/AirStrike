import matplotlib.pyplot as plt
import matplotlib
import Base
from sys import argv

x1 = float(argv[1])
y1 = float(argv[2])
r1 = float(argv[3])


bases = []
figure, axes=plt.subplots()
axes.set_aspect(1)
with open('targets.txt', "r") as file:
    for line in file:
        x, y, w = map(int, line.split())

        bases.append(Base.Base(x, y, w))

for i in range(len(bases)):
    axes.add_artist(plt.scatter(bases[i].x,bases[i].y))

matplotlib.patches.Circle((x1, y1), r1, color='red')


plt.xlim(0,10)
plt.ylim(0,10)
circle=plt.Circle((x1, y1), r1, color='red',fill=False)

axes.add_artist(circle)

plt.show()

