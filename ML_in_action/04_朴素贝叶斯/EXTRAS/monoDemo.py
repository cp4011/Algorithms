from numpy import *
import matplotlib.pyplot as plt

t = arange(0.0, 0.5, 0.01)      # numpy.arange()函数双精度浮点数，间隔为0.01
s = sin(2*pi*t)
logS = log(s)

fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(t, s)
ax.set_ylabel('f(x)')
ax.set_xlabel('x')

ax = fig.add_subplot(212)
ax.plot(t, logS)
ax.set_ylabel('ln(f(x))')
ax.set_xlabel('x')
plt.show()

# plt.plot(t, s)        # 两条线画在一张图上
# plt.plot(t, logS)
# plt.show()
