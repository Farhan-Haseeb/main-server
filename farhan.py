# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:04:51 2020

@author: Farhan Haseeb

"""

import random
from uuid import uuid4

def optimization_function(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total


class Particle():
    def __init__(self, x0):
        self.id = x0['address']
        self.position_i = []
        self.velocity_i = []
        self.pos_best_i = []
        self.err_best_i = -1
        self.err_i = -1

        for i in range(0, num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0['initials'][i])
        print(f"{self.id}, {self.position_i} particle id and location")

        # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i = costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self,pos_best_g):
        w = 0.5; c1 = 1; c2 = 2 

        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = round(self.position_i[i] + self.velocity_i[i])

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = round(bounds[i][1])

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = round(bounds[i][0])
        return self.position_i , self.id


class PSO():
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):
        global num_dimensions

        num_dimensions = len(x0[0])
        self.err_best_g =- 1
        self.pos_best_g = []
        self.num_particles = num_particles
        self.maxiter = maxiter
        self.x0 = x0
        self.bounds = bounds
        self.costFunc = costFunc

    def run(self):
        swarm = []
        for i in range(0, self.num_particles):
            swarm.append(Particle(self.x0[i]))

        i = 0

        while i < self.maxiter:
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, self.num_particles):
                swarm[j].evaluate(self.costFunc)
                # determine if current particle is the best (globally)
                if swarm[j].err_i < self.err_best_g or self.err_best_g == -1:
                    self.pos_best_g = list(swarm[j].position_i)
                    self.err_best_g = float(swarm[j].err_i)
            # cycle through swarm and update velocities and position
            for j in range(0, self.num_particles):
                swarm[j].update_velocity(self.pos_best_g)
                swarm[j].update_position(self.bounds)
            i += 1

        # print final results
        # print(self.err_best_g)
        return self.pos_best_g


# initials = [[16, 12], [0, 5], [2, 10], [5, 9]]
initials = [{'address': '192.168.8.111:52608', 'initials': [16, 12]},{'address': '192.168.8.114:52610', 'initials': [6, 4]}, {'address': '192.168.8.131:50608', 'initials': [6, 8]},{'address': '192.168.8.124:52410', 'initials': [16, 4]}]
bounds = [(0, 2), (10, 16)]

pso = PSO(optimization_function, initials, bounds, num_particles = 4, maxiter=30)
print(f"{pso.run()}, the final value")
