from matplotlib import pyplot as plt 

x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y = []
for x_in in x:
    y.append(x_in*x_in)

plt.plot(x,y)
plt.grid()
plt.show()