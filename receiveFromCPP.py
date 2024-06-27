import socket
import sys
import threading
import time, random

import numpy as np
import pandas
from matplotlib import pyplot as plt
from matplotlib import animation
from collections import deque

RENDEZVOUS_ADDRESS = ('128.97.3.196', 55555)

MY_SOURCE_PORT = 50002
mySourceSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySourceSocket.bind(('0.0.0.0', MY_SOURCE_PORT))

# LISTENING
xvals = deque()
Fx_vals = deque()
Fy_vals = deque()
Fz_vals = deque()
move = False
def listen(): 
    global xvals
    global Fx_vals
    global Fy_vals
    global Fz_vals
    global move
    while True:
        data = mySourceSocket.recv(2048)
        string = data.decode()
        line = string.split(' ')
        if len(xvals) > 300:
            xvals.popleft()
            Fx_vals.popleft()
            Fy_vals.popleft()
            Fz_vals.popleft()
            move = True
        xvals.append(float(line[0]))
        Fx_vals.append(float(line[1]))
        Fy_vals.append(float(line[2]))
        Fz_vals.append(float(line[3]))

listener = threading.Thread(target=listen, daemon=True)
listener.start()

# MAIN QUESTION: SHOULD YOU UPDATE CIRCULAR BUFFER IN LISTEN OR IN DRAWING? Going with listen for now.

plt.switch_backend('QtAgg') 

fig, ax = plt.subplots(figsize=(5,10))
ln1, = ax.plot([], [], 'r', label="Force X")
ln2, = ax.plot([], [], 'b', label="Force Y")
ln3, = ax.plot([], [], 'g', label="Force Z")
lines = [ln1, ln2, ln3]

def init():
    ax.set_xlim(0,300)
    ax.set_ylim(-50, 50)
    plt.title("Incoming Stream")
    plt.legend(loc="upper right")
    return lines

def update(i):
    global move
    # if len(xdata) > 500:
    #     xdata = xdata[-500:]
    #     ydata = ydata[-500:]
    if move:
        ax.set_xlim(xvals[0],xvals[-1])
    ln1.set_data(xvals, Fx_vals)
    ln2.set_data(xvals, Fy_vals)
    ln3.set_data(xvals, Fz_vals)

    return lines

start_time = time.time()
ani = animation.FuncAnimation(fig, update, frames=10000, interval=10,
                    init_func=init, blit=False) 
plt.show()
