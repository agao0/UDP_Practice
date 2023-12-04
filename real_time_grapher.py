import numpy as np
import pandas
from matplotlib import pyplot as plt
import time, random

plt.switch_backend('QtAgg') # THIS IS FASTEST (from what I've tested so far, TkAgg, Notebook, Inline, MacOsX)

# print(plt.get_backend())
# fig, ax = plt.subplots()
# print(fig.canvas.supports_blit)

dataframe = pandas.read_csv('tlm_1.csv', index_col=0) # automatically changes first col to Timestamp

# OK, updated Jupyter notebook, matplotlib, etc. Things have changed and gotten slower unfortunately. Going to write blit explicitly.

from matplotlib import animation
import time
# zstuff = dataframe.iloc[:,[2,5,44,50, 53]]
# x = zstuff["Force_Z"].axes[0]
# x = list(x)
# y = zstuff["Force_Z"].array

# # FILTER, ONE DATA POINT IS NOW EVERY 0.02 SECONDS = 50HZ
# x = [x[i] for i in range(len(x)) if i%10==0]
# y = [y[i] for i in range(len(y)) if i%10==0]


fig, ax = plt.subplots(figsize=(10,5))
xdata, ydata = [], []
ln, = ax.plot([], [], 'r')

def init():
    ax.set_xlim(8,20)
    ax.set_ylim(-100, 400)
    return ln,

def update(i):
    global xdata
    global ydata
    xdata.append(10+i*0.02)
    ydata.append(random.random()*500-100)
    if len(xdata) > 500:
        xdata = xdata[-500:]
        ydata = ydata[-500:]
    ln.set_data(xdata, ydata)
    return ln,

start_time = time.time()
ani = animation.FuncAnimation(fig, update, frames=1000, interval=8,
                    init_func=init, blit=True) 
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))


# OBSERVATIONS: For full length test (2890 items - 50Hz)
# Using MacOsX Backend, when blit set to False, uses 71.67s, when True, uses 69.2s...not much difference 
# Using TkAgg Backend, blit=True, 56.67s

# CRUDE VERSION, TOO SLOW
# plt.ion()
# plt.ioff()
# fig = plt.figure(figsize=(10,5))
# ax = fig.add_subplot(111)
# plt.xlim([0,70])
# plt.ylim([-100,400])

# xdata = []
# ydata = []
# line, = ax.plot(ydata)

# ax.set_xlabel('Time')
# ax.set_ylabel('Y-Axis')
# ax.set_title('Real Time Plot')
# ax.legend(['Data'], loc="upper right")

# start = time.time()
# for i in range(2890):
#     xdata.append(x[i])
#     ydata.append(y[i])

#     line.set_ydata(ydata)
#     line.set_xdata(xdata)
#     plt.draw()
#     plt.pause(0.01)

# print("Elapsed: " +str(time.time()-start))
# plt.show()