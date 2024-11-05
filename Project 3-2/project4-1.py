#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In this project, you will use functions to simulate the epidemic of a virus
within a region. 
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Section 1. set the model parameters
# =============================================================================
# 1.1 set the random seed to 380 (pseudo randomness)
np.random.seed(380)  # DO NOT CHANGE THE SEED

# 1.2 create a population vector with five areas, population in areas are:
# areaA: 18000. areaB: 22000, areaC:50100,areaD,21010, areaE:25000

n_j = np.array([18000, 22000, 50100, 21010, 25000])

# 1.3 use the random integer generation function in numpy to create a 5 x 5
# Origination-Destination flow matrix
# Set the lower limit to 1000, upper limit to 3,000 
od_matrix = np.random.randint(low=1000, high=3000, size=[5, 5])

# 1.4 same modal share across all regione (1)
alpha_vec = np.full(len(n_j), 1)

# 1.5 same transmission rate across all regions
beta_vec = np.full(len(n_j), 0.8)

# 1.6 same recover rate  across all regions
gamma_vec = np.full(len(n_j), 0.05)

# 1.7 normal o-d flow
od_flow = od_matrix.copy()  # Note look back at this

# 1.8 Have 300 iterations
days = 100

#=============================================================================
#Section 2. define the initial status table
#=============================================================================
# assume in the beginning, no recover or died yet,
# infected proportion in areas are:
# areaA: 1%; areaB: 0.5%; areaC:0.1%; arerD:0%, areaE:0%
infected = n_j * np.array([0.01, 0.05, 0.001, 0, 0])
immune = np.array([0, 0, 0, 0, 0])

sir = np.array([n_j - infected, infected, immune])

# =============================================================================
# Section 3. Define a function to simulate the epidemic in this big region
# =============================================================================
# function input should include:
# n_j:              population vector
# initial status:   the initial status of the epidemic
# od_flow:          the 5 x 5 o-d matrix
# alpha_vec:        population density in each region
# beta_vec:         transmission rate in each region
# gamma_vec:        daily recover rate in each region
# days: total       iterations

# function return:
# susceptible_pop_norm: changes in the proportion of S group (aggregated)
# infected_pop_norm: changes in the proportion of  I group (aggregated)
# recovered_pop_norm: changes in the proportion of R group (aggregated)

def epidemic_sim(n_j, initial_status,od_flow,
                 alpha_vec,beta_vec,gamma_vec,days):

    # I start by removing the identities since they can confuse calculation
    for n in range(len(od_flow)):
        od_flow[n][n] = 0


    #3.1 make copy of the initial sir table
    sir = initial_status.copy()

    #3.2 create empty list to keep tracking the changes
    susceptible_pop_norm = []
    infected_pop_norm = []
    recovered_pop_norm = []

    #3.3. use total_days as the interator
    total_days = np.linspace(1,days,days)
    for day in total_days:
        # normalize the sir table by calculating the percentage of each group
        sir_percent =  np.array([ sir[0] / n_j, sir[1] / n_j, sir[2] / n_j])

        # od_infected gives the flow of infected people. i.e., where they go
        od_infected = od_flow * sir_percent[1][:, np.newaxis]

        # "inflow infected" are those who will spread the disease to susceptible
        inflow_infected = np.sum(od_infected, axis=0) # total infected inflow in each area
        outflow_infected = np.sum(od_infected, axis=1)

        # this is the total number of people who move into each region
        inflow = np.sum(od_flow, axis=0)
        outflow = np.sum(od_flow, axis=1)

        #3.5 calculate new_infect
        new_infect = alpha_vec * (sir[0] / ( sir[0]+sir[1]+sir[2] + inflow - outflow)) * beta_vec * (sir[1] + inflow_infected - outflow_infected)


        #3.6 set upper limit of the infected group (total susceptible)
        for x in range(5):
            new_infect[n] = min(new_infect[n], sir[0][x] + sir[1][x] + sir[2][x])



        #3.7 calculate total number of people recovered
        new_recovered = sir[1] * gamma_vec


        #3.8 remove new infections from susceptible group
        sir[0] = sir[0] - new_infect

        #3.9 add new infections into infected group,
        sir[1] = sir[1] + new_infect

        # also remove recovers from the infected group
        sir[1] = sir[1] - new_recovered


        #3.10 add recovers to the recover group
        sir[2] = sir[2] + new_recovered


        #3.11 set lower limits of the groups (0 people)
        # sir_sim =


        #3.12 compute the normalized SIR matrix on aggregate level
        region_sum =  np.sum(sir, axis=1)
        sum = region_sum[0] + region_sum[1] + region_sum[2]
        s = region_sum[0] / sum
        i = region_sum[1] / sum
        r = region_sum[2] / sum

        susceptible_pop_norm.append(s)
        infected_pop_norm.append(i)
        recovered_pop_norm.append(r)


    return [ susceptible_pop_norm, infected_pop_norm,recovered_pop_norm]





#3.13 call the function to simulate the epidemic
outcome = epidemic_sim(n_j, sir,od_flow, alpha_vec,beta_vec,gamma_vec,days)

#=============================================================================
#Section 4. define a function to visualize the simulation result
#=============================================================================

def sir_simulation_plot(outcome,days):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1,1,1)
    days = np.linspace(1,days,num=days)
    susceptible = np.array(outcome[0])*100
    infected = np.array(outcome[1])*100
    recovered = np.array(outcome[2])*100
    ax.plot(days,susceptible,label='susceptible',color='y')
    ax.plot(days,infected,label='infected',color='r')
    ax.plot(days,recovered,label='recovered',color='g')
    ax.set_xlabel('Days')
    ax.set_ylabel('Proportion of the population')
    ax.set_title("SIR Model Simulation")
    plt.legend()
    plt.show()

# sir_simulation_plot(outcome, days)
sir_simulation_plot(epidemic_sim(n_j, sir,od_flow, alpha_vec,beta_vec,gamma_vec,days), days)

#=============================================================================
#Section 5. Policy evaluation
#=============================================================================
# Using the simulation model to evaluate the following policy targets
# Visualize the results, organize the plots in a 2x2 figure, each outcome on
# one subplot.

outcome = epidemic_sim(n_j, sir,od_flow, alpha_vec,beta_vec,gamma_vec,days)
days_list = range(1, days+1)
plt.subplot(2, 2, 1)
plt.plot(days_list, outcome[0], label="suseptible")  # First line
plt.plot(days_list, outcome[1], label="infected")  # Second line
plt.plot(days_list, outcome[2], label="recoverd")  # Third line
plt.title("SIR no change")
plt.legend()

outcome = epidemic_sim(n_j, sir,od_flow*0.5, alpha_vec,beta_vec,gamma_vec,days)
plt.subplot(2, 2, 2)
plt.plot(days_list, outcome[0], label="suseptible")  # First line
plt.plot(days_list, outcome[1], label="infected")  # Second line
plt.plot(days_list, outcome[2], label="recoverd")  # Third line
plt.title("SIR 50% less travel")
plt.legend()

outcome = epidemic_sim(n_j, sir,od_flow*0.5, alpha_vec,beta_vec,gamma_vec,days)
plt.subplot(2, 2, 3)
plt.plot(days_list, outcome[0], label="suseptible")  # First line
plt.plot(days_list, outcome[1], label="infected")  # Second line
plt.plot(days_list, outcome[2], label="recoverd")  # Third line
plt.title("SIR 80% less travel")
plt.legend()

outcome = epidemic_sim(n_j, sir,od_flow*.5, alpha_vec, beta_vec * 0.5, gamma_vec, days)
plt.subplot(2, 2, 4)
plt.plot(days_list, outcome[0], label="suseptible")  # First line
plt.plot(days_list, outcome[1], label="infected")  # Second line
plt.plot(days_list, outcome[2], label="recoverd")  # Third line
plt.title("SIR 80% less travel and 50% less beta")
plt.legend()

plt.show()