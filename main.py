
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

STEPS = 5 # the number of previous steps to display
AGENTS = 150  # the number of agents
EPSILON = .3 # The degree to which two agents will move their opinion. For instance epislon = .3 means that an agent will retain 70% of its opinion and take on 30% of the opionion of the agent it is communicating with
DRIFT = 1 #defines how much the opinions should drift away from the center

#########################################
# Opinion Changing Functions
#########################################

def generate_agreement_matrix(x, ep=EPSILON):
    """Simulates communication between the agents.
    
    Takes the current opinions of the agents along one dimension, uniformly
    selects two agents to communicate and then updates their values according to the
    global EPSILON value, or one given by the user."""
    A = np.identity(AGENTS)

    a = random.randint(0,AGENTS-1)
    b = random.randint(0,AGENTS-1)
    if a==b: return A # if an agent communicates only with itself, then no one communicates
    

    A[a,a] = 1-ep
    A[b,b] = 1-ep
    A[a,b] = ep
    A[b,a] = ep
    
    return A
    
def drift(x, d=.1):
    """Generates the drift term. Each agent's opinion will move away from the average."""
    av = np.mean(x)
    
    dr = np.zeros(AGENTS)
    for i in range(0,AGENTS):
        dr[i] = x[i]<av and -d or d
    
    return dr
    
def generate_lines(total_steps = 1000):
    """Starts all of the opinions at zero and then steps through the agent's communications."""
    opinions = [np.zeros((STEPS,AGENTS))] # everyone's opinion begins at 0
    
    for i in range(0,total_steps):
        current_step = opinions[i]
        
        x = current_step[0]
        A = generate_agreement_matrix(x)
        omega = np.random.normal(size=(1,AGENTS))
        
        new_opinion = np.dot(x, A)+drift(x)+omega
        
        new_step = np.concatenate((new_opinion,current_step))
        opinions.append(new_step[:STEPS])
    
    return opinions




    
#########################################
# Animation Functions
#########################################

x_opinions = generate_lines()
y_opinions = generate_lines()

fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
lines = [ax.plot([], [])[0] for i in range(0,AGENTS)]

def animate(i,j,lines):
    """Cycles through the opinions and displays them."""
    x = x_opinions[i]
    y = y_opinions[i]
    
    for j in range(0,AGENTS):
        lines[j].set_data(x[:,j], y[:,j])
    
    return lines

anim = animation.FuncAnimation(fig, animate, fargs=(1,lines), frames=2000, interval=20)
plt.show()