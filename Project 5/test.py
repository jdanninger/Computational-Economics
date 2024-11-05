import numpy as np


class Econ_agent:
    def __init__(self, id_number, budget):
        self.id_number = id_number
        self.budget = budget

    def introduce_me(self):
        print("My id is " + str(self.id_number) + " and my budget is " + str(self.budget))

class Consumer(Econ_agent):

    def __init__(self, id_number, budget, preference):
        super().__init__(id_number, budget)
        self.preference = preference
        self.wtp = self.budget * self.preference

    def buying(self, price):
        # I made this method return the amount of purchases a consumer will make up to 5
        buy = 0
        for i in range(5):
            if self.wtp >= price and self.budget > price:
                buy += 1
                self.budget -= price
                self.wtp = self.budget * self.preference
        return buy
class Producer(Econ_agent):
    def __init__(self, id_number, budget, opp_cost):
        super().__init__(id_number, budget)
        self.opp_cost = opp_cost

    def selling(self, price):
        if (price >= self.opp_cost):
            return int(self.budget / self.opp_cost)
        else:
            return 0

print( np.random.normal(500,100))