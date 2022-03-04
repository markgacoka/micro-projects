'''
The numerical simulation calculates the approximation of the original curves from the SIR differential equations
using Euler's method
Code is adapted from:
https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/
'''
import numpy as np #numpy is used 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 305, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 #Susceptible is equal to the population less the infected and removed
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.3552, 0.1 #Infectiousness and recovery rates
# A grid of time points (in days)
t = np.linspace(0, 200, 200) #length of time in days

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N #derivative of susceptible equation
    dIdt = beta * S * I / N - gamma * I #derivative of infected equation
    dRdt = gamma * I #derivative of removed equation
    return dSdt, dIdt, dRdt #return the value of the derivatives

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, S/1000000, 'b', alpha=0.5, lw=2, label='Susceptible') #Plot the susceptible line as blue
ax.plot(t, I/1000000, 'r', alpha=0.5, lw=2, label='Infected') #plot the infected line as red
ax.plot(t, R/1000000, 'g', alpha=0.5, lw=2, label='Recovered with immunity') #plot the removed line as green
ax.set_xlabel('Time /days') #Set the label as time in days
ax.set_ylabel('Number (1000000s)') #population number is expressed in millions
ax.set_ylim(0,1.2) #the y-axis is limited to a maximum of 1.2
ax.yaxis.set_tick_params(length=0) 
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
plt.title('SIR model for the Ebola Outbreak in Liberia, 2014')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show() #Display the graph