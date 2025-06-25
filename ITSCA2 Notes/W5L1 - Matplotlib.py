# Data Visualization
import matplotlib.pyplot as plt
import numpy as np
#Basic plotting
x = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [0, 0.25, 1.0, 2.25, 4.0, 6.25, 9]

# plt.plot(x, y)
# plt.show()

x = np.random.randint(0, 16, 50)
y = np.random.randint(0, 16, 50)

# plt.scatter(x, y)
# plt.show()

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]

plt.bar(x, y)
plt.show()

data = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]

# plt.hist(data,bins = 5) # 5 different numbers
# plt.show()

# Basic Customization
x = np.arange[0, 10, 0.1]
y1 = (2*x)+3
y2 = (x**2)-(2*x)+1

plt.plot(x, y1, label = 'Linear', linestyle = '--', color = 'r')
plt.plot(x, y2, label = 'Quadratic', linestyle = 'dashdot', color = 'b')
plt.legend()
plt.xlabel('x-value')
plt.ylabel('y-value')
plt.title('Linear vs Quadratic Equation')
plt.grid(True)
# plt.xlim(0, 5)
# plt.ylim(0, 10)
plt.show()
plt.savefig('plot.png') # Can save in png or pdf

x = np.linspace(-2*np.pi, 2*np.pi, 50)

y1 = np.sin(x)
y2 = np.tan(x)
y3 = np.cos(x)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots(1, 2)

ax1.plot(x, y1)
ax2[0].plot(x, y2)
ax2[1].plot(x, y3)

x = np.linspace(0.1, 2, 50)

y1 = np.log(x)
y2 = np.exp(x)

fig3, ax3 = plt.subplots()

ax3.plot(x, y1, label = 'log(x)', linestyle = '-', linewidth = 2, color = 'r')
ax3.plot(x, y2, label = 'e^x', linestyle = '--', linewidth = 2, color = 'b')
ax3.legend(loc = 'best', prop ={'size' : 'large'})
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.grid(True)
fig3.suptitle('Natural log vs Exponential Function')
fig3.savefig('Log_exp.pdf', dpi = 125)