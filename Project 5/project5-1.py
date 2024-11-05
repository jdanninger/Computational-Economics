
"""
Project 5. In this project, you will apply Object Oriented Programming to
simulate the market demand/supply model.

"""
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(380)
#=============================================================================
# Section 1. Define classes
#=============================================================================
class Econ_agent:
    def __init__(self, id_number, budget):
        self.id_number = id_number
        self.budget = budget

    def introduce_me(self):
        print("My id is " + str(self.id_number) + " and my budget is " +  str(self.budget))

class Consumer(Econ_agent):

    def __init__(self, id_number, budget, preference):
        super().__init__(id_number, budget)
        self.preference = preference
        self.wtp = budget * preference

    def buying(self, price):
        # I made this method return the amount of purchases a consumer will make up to 5
        buy = 0
        restore_budget = self.budget
        for i in range(5):
            if self.wtp >= price and self.budget > price:
                buy += 1
                self.budget -= price
                self.wtp = self.budget * self.preference
        self.budget = restore_budget
        self.wtp = restore_budget * self.preference
        return buy


class Producer(Econ_agent):
    def __init__(self, id_number, budget, opp_cost):
        super().__init__(id_number, budget)
        self.opp_cost = opp_cost

    def selling(self, price):
        restore_budget = self.budget
        if (price >= self.opp_cost):
            return self.budget /self.opp_cost
        else:
            return 0

#=============================================================================
# Section2. generate objects
#=============================================================================


consumers = []
for n in range(200):
    consumers.append(Consumer(n, np.random.normal(500,100), np.random.uniform(0,1)))

producers = []
for n in range(50):
    producers.append(Producer(n, np.random.uniform(1000,8000), np.random.uniform(100, 200)))


#=============================================================================
# Section 3. Simulate the market mechanism, and find the equilibrium
#=============================================================================


def demand_at_price(price, consumers):
    return_me = 0
    for consumer in consumers:
        return_me += consumer.buying(price)
    return return_me


def supply_at_price(price, producers):
    return_me = 0
    for producer in producers:
        return_me += producer.selling(price)
    return return_me

def equilibrium_price(consumers, producers):
    price = 0
    total_demand = demand_at_price(price, consumers)
    total_supply = supply_at_price(price, producers)
    while abs(total_demand - total_supply > 5 and total_supply < total_demand):
        price += 0.01
        total_demand = demand_at_price(price, consumers)
        total_supply = supply_at_price(price, producers)
    return price

print("the equilibrium price is " + str(equilibrium_price(consumers, producers)))


#=============================================================================
# Section4. Define the demand curve and supply curve
#=============================================================================


# was not 100% sure what this method should do
# this method takes a list of prices and returns the demand at those prices
# this makes graphing demand pretty easy
def demand(prices, consumers):
    return_me = []
    for price in prices:
        return_me.append(demand_at_price(price, consumers))
    return return_me

# was not 100% sure what this method should do
# this method takes a list of prices and returns the supply at those prices
# this makes graphing supply pretty easy
def supply(prices, producers):
    return_me = []
    for price in prices:
        return_me.append(supply_at_price(price, producers))
    return return_me

def graph_100_200(producers, consumers):
    prices = range(100, 201)
    supply_100_200 = supply(prices, producers)
    demand_100_200 = demand(prices, consumers)
    plt.plot(prices, supply_100_200, label='supply curve', color='blue')
    plt.plot(prices, demand_100_200, label='demand curve', color='red')
    plt.xlabel('Price')
    plt.ylabel('Quantity')
    plt.title('Supply Demand')
    plt.legend()
    plt.show()

graph_100_200(producers, consumers)

#=============================================================================
# Section 5. Changes in supply
#=============================================================================

for producer in producers:
    producer.opp_cost = producer.opp_cost * .95
graph_100_200(producers, consumers)

print("the equilibrium price after a 5% opportunity cost reduction is " + str(equilibrium_price(consumers, producers)))



#=============================================================================
# Section 6 (optional). Estimate the demand and supply function
# Estimate the demand function and supply function you simulated in Section 4,
# and then use the two function to figure out the market equilibrium,
# see if the calculated equilibrium coincide with the simulation result.
#=============================================================================
