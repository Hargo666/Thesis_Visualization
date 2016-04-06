

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import random

STEPS = 10000
AGENTS = 10
EPSILON = .3

def communicate(x):
    
    
    a = random.randint(0,9)
    b = random.randint(0,9)
    if a==b: return x
    
    A = np.identity(AGENTS)
    
    A[a,a] = 1-EPSILON
    A[b,b] = 1-EPSILON
    A[a,b] = EPSILON
    A[b,a] = EPSILON
    
    print A
    
    return np.dot(x,A)



def init():
    line.set_data([], [])
    return line,

x_opinion = np.zeros((STEPS,AGENTS))
y_opinion = np.zeros((STEPS,AGENTS))

x_opinion[0] = np.random.randint(-100,100,(1,AGENTS))
y_opinion[0] = np.random.randint(-100,100,(1,AGENTS))

print x_opinion

def animate(i):
    if i>0:
        x_opinion[i] = communicate(x_opinion[i-1])+np.random.normal(size=(1,AGENTS))
        y_opinion[i] = communicate(y_opinion[i-1])+np.random.normal(size=(1,AGENTS))
    
    
    
    
    x = x_opinion[i]
    y = y_opinion[i]
    line.set_data(x, y)
    return line,
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 # First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1000, 1000), ylim=(-1000, 1000))
line, = ax.plot([], [], 'bo')  
    

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=2000, interval=20)


plt.show()