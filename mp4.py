#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:14:24 2019

@author: asukawatanabe
"""
import math 
from matplotlib import pyplot as plt
def simulate_projectile_motion(s0,v0,theta0,ax,ay):
    if ay==0:
        print("Error: vertical acceleration cannot be 0")
        return  
    
    x_vals = [] 
    y_vals = [] 
    v0x = v0*math.cos(theta0*(3.141/180)) 
    v0y = v0*math.sin(theta0*(3.141/180)) 
    
    t = 0
    x = 0
    y = s0 
    delta = 0.0001 
    
    x_vals.append(x)
    y_vals.append(y)
    
    while(True):
        t = t+delta
        x = v0x*t + (0.5)*ax*(t*t)
        y = v0y*t + (0.5)*ay*(t*t) + s0
        
        x_vals.append(x)
        y_vals.append(y)
        
        if y < delta:
            break
        
    plt.plot(x_vals,y_vals)  
    ax = plt.gca()
    ax.set_ylim([0,max(y_vals)])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Simulation of projectile motion')
    plt.grid()
    plt.show()
        
if __name__ == '__main__':
   s0 = float(input("Enter s0 in meters : "))
   v0 = float(input("Enter v0 in m/s: "))
   theta0 = float(input("Enter theta in degrees: "))
   ax = float(input("Enter Acceleration in X-axis: "))
   ay = float(input("Enter Acceleration in Y-axis: "))
   simulate_projectile_motion(s0,v0,theta0,ax,ay)  