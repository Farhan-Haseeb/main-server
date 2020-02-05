# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:44:32 2019

@author: S.jarrar
"""
import matplotlib.pyplot as plt
import numpy as np
import random
fitness=0
min_list=[]
fit_list_o=[]
min_cost=[]
new_n=[]
new_pos=[]
iterations=15
n=10
d=20
z=0
w=0.7
c1=c2=2
v_list=[]
n_fitness=0
fit_list_n=[]
for i in range(n):
    v=[]
    for a in range(d):
        v.append(random.random())
    v_list.append(v)
velocity=np.asarray(v_list)
for i in range(n):
    p=[]
    for a in range(d):
        p.append(random.randint(1,50))
    new_pos.append(p)
positions=np.asarray(new_pos)
pbest=np.asarray(positions)
print(pbest)
#print(type(pbest))
for i in range(n):
    fitness=0
    for a in range(d):
        fitness=fitness+positions[i][a]**2
    #print(fitness)
    fit_list_o.append(fitness)
fitness_o=np.asarray(fit_list_o)
print(f"fitness_o is {fitness_o}")
index=fit_list_o.index(min(fit_list_o))
res=(positions[index])    
gbest=np.asarray(res)
print(f"this is gbest {gbest}")
min_cost.append(min(fit_list_o))
#print(min_cost)
#if z<=iterations:
while z<=iterations:
    for i in range(n):
        for a in range(d):
            velocity[i][a]=w*velocity[i][a]+c1*random.random()*(pbest[i][a]-positions[i][a])+c2*random.random()*(gbest[a]-positions[i][a])
            #print(velocity[i][a])
            positions[i][a]=positions[i][a]+velocity[i][a]
    print(f"These are new positions {positions}")
   
    for i in range(n):
        n_fitness=0
        for a in range(d):
            n_fitness=n_fitness+positions[i][a]**2
        fit_list_n.append(n_fitness)
    fitness_n=np.asarray(fit_list_n)
    print(f"fitness_n is {fitness_n}")
    for i in range(n):
        if fitness_n[i]<fitness_o[i]:
            min_list.append(fitness_n[i])
        else:
            min_list.append(fitness_o[i])
    index_n=min_list.index(min(min_list))
    res1=positions[index_n]
    gbest=np.asarray(res1)
    print(f"this is gbest {gbest}")
    min_list1=np.asarray(min_list)
    min_cost.append(min(min_list))
    fit_list_n.clear()
    min_list.clear()
    fit_list_o.clear()
    fitness_o=min_list1
    print(f"This is min list1 {min_list1}")
    print(min_cost)
    for i in range(n):
        for a in range(n):
            if min_list1[i]==fitness_n[a]:
                new_n.append(positions[a])
                break
            elif min_list1[i]==fitness_o[a]:
                new_n.append(positions[a])
                break
                
    pbest=np.asarray(new_n)
    print(f"This is new pbest {pbest}")
    #for i in range(n):
        #f=0
        #for a in range(d):
            #f=f+pbest[i][a]**2
        #fit_list_o.append(f)
    #fitness_o=np.asarray(fit_list_o)
    new_n.clear()
    #fitness_o=fitness_n
    #print(f"check with fitness_n {fitness_o}")
    z=z+1
    #while z<=iterations:
        #z=z+1
x=[]
plt.xlabel("Iteration")
plt.ylabel("Fitness")
for l in range(iterations+2):
    x.append(l)
plt.plot(x,min_cost, label='x2',color='Blue',linewidth=2,marker='.', markersize=10)
plt.title('Comparative Analysis',fontdict={'fontname': 'camberia', 'fontsize' : 20})
plt.xticks([0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])  
plt.legend()
plt.show()    
    

    


