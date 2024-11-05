"""
project 7. the Solow-Swan growth model
"""
# Section 1. Preparation. Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import copy


# Section 2. Define the Growth model as a class

# ==================
# attributes:
# -a: factor productivity
# -s
# -alpha
# -delta
# -n

# -k
# -K
# -y
# -Y
# -i
# -I
# -L
# -d
# -be
# -steady_state


# methods:
# check_model: print the attribute of the instance
# grwoth: take one argument "year", and drive the economic growth
# get parameters: get the model parameters
# get states: get the states variables
# plot_growth: visualize how the income per capita, investment per capita, and
# plot_income_growth
# find_steady_state: solve for the steady state in this model

# arguments:
# ----------------------------------------------------------------------------
# para_dict:

# ----------------------------------------------------------------------------#\
# state_dict
    
    

class Growth_Model:
    """
    This class will create an instance of the Solow-Swan growth model
    
    arguments:
    ------------------
    para_dict: dict
        a dictionary of parameters
    state_dict: dict
        a dictionary of model state
        
    attributes
    --------------
    
    methods:
    -------------
    
    """
    
    def __init__(self, para_dict, state_dict):
    # para has --> n (pop growth rate), s (saving rate), alpha (share of capital), delta (depreciation rate), a (factor productivity)
    # state has --> k (default capital/capita), L (default population)

        self.para_dict = para_dict
        self.state_dict = state_dict
        
        # calculate lower case y
        self.state_dict['y'] = (self.para_dict['a']
                                * self.state_dict['k']**self.para_dict['alpha'])
        # calculate upper case K (i.e., aggregate capital)
        self.state_dict['K'] = self.state_dict['k'] * self.state_dict['L']
        # calculate upper case Y
        self.state_dict['Y'] =  self.state_dict['y'] * self.state_dict['L']
        # calculate lower case i
        self.state_dict['i'] = self.para_dict['s'] * self.state_dict['y']
        # calculate upper case I
        self.state_dict['I'] = self.state_dict['i'] * self.state_dict['L']
        
        self.steady_state = {}
        

    
    def growth(self, years):
        
        # step 1. define the timeline
        time_line = np.linspace(0, years, num=years+1, dtype=int)
        
        # step 2. examine growth
        for t in time_line: 
            
            # 2.1. load parameters
            n = self.para_dict.get('n')[0]
            s = self.para_dict.get('s')[0]
            alpha = self.para_dict.get('alpha')[0]
            delta = self.para_dict.get('delta')[0]
            a = self.para_dict.get('a')[0]
            
            # 2.2. load all current states
            y_t = self.state_dict.get('y')[t]
            k_t = self.state_dict.get('k')[t]
            Y_t = self.state_dict.get('Y')[t]
            L_t = self.state_dict.get('L')[t]
            K_t = self.state_dict.get('K')[t]
            i_t = self.state_dict.get('i')[t]
            I_t = self.state_dict.get('I')[t]

            # 2.3 calculate new states i.e., the dynamic
            dk = s * y_t - (n + delta) * k_t
            k_next = k_t + dk
            L_next = L_t * (1 + n)
            y_next = a * k_next**alpha
            K_next = (1 - delta) * K_t + s * Y_t
            Y_next = a * K_next**alpha * L_next ** (1 - alpha)
            i_next = s * y_next
            I_next = i_next * L_next

            # 2.4. update the state_dict
            k_t = k_next
            y_t = y_next
            Y_t = Y_next
            K_t = K_next
            L_t = L_next
            i_t = i_next
            I_t = I_next

            # update the attributes
            self.state_dict['k'] = np.append(self.state_dict['k'], [k_t])
            self.state_dict['y'] = np.append(self.state_dict['y'], [y_t])
            self.state_dict['Y'] = np.append(self.state_dict['Y'], [Y_t])
            self.state_dict['K'] = np.append(self.state_dict['K'], [K_t])
            self.state_dict['L'] = np.append(self.state_dict['L'], [L_t])
            self.state_dict['i'] = np.append(self.state_dict['i'], [i_t])
            self.state_dict['I'] = np.append(self.state_dict['I'], [I_t])

    def find_steady_state(self):
        # step 1. load paramters
        n = self.para_dict.get('n')[0]
        s = self.para_dict.get('s')[0]
        alpha = self.para_dict.get('alpha')[0]
        delta = self.para_dict.get('delta')[0]
        a = self.para_dict.get('a')[0]
        k_t = np.linspace(0, 35, len(self.state_dict['k']))  # create the k_t domain

        # step 2. calculate the steady state
        # 2.1. calculate the break-even investment
        be = (n + delta) * k_t
        # 2.2. calculate the investment
        i = s * a * k_t**alpha
        itera = 0
        for n in range (1, len(k_t)):
            if be[n] >= i[n]:
                k_star = k_t[n]
                itera = n
                break

        y_star = a * k_star**alpha
        i_star = s * a * k_star**alpha
        c_star = (1 - s) * a * k_star**alpha

        steady_state = {}
        steady_state["k_star"] = k_star
        steady_state["y_star"] = y_star
        steady_state["c_star"] = c_star
        steady_state["i_star"] = i_star


        self.steady_state = steady_state
        print(k_star)
        return [y_star, i_star, c_star], itera

    def graph_a(self):
        n = self.para_dict.get('n')[0]
        s = self.para_dict.get('s')[0]
        alpha = self.para_dict.get('alpha')[0]
        delta = self.para_dict.get('delta')[0]
        a = self.para_dict.get('a')[0]
        k_t = np.linspace(0, 30, len(self.state_dict['k']))
        i = s * a * k_t ** alpha
        y = a * k_t ** alpha
        be = (n + delta) * k_t
        plt.plot(k_t, be, label='Break-even investment')
        plt.plot(k_t, i, label='Investment')
        plt.plot(k_t, y, label='Income')
        plt.xlabel('Capital per worker')
        plt.ylabel('Investment per worker')
        plt.legend()
        plt.show()



    def plot_income_growth(self, ax):
        income = self.state_dict['y']
        time = np.linspace(0, len(income), len(income))
        ax.plot(time, income)
        # ax.set_xlabel('Display X-axis Label',
        #               fontweight='bold')
        # # ax.set_ylabel('Income per capita')
        # # ax.set_title('Income per capita over time')

    
    def plot_growth(self, ax):
        capital = self.state_dict['k']
        income = self.state_dict['y']
        investment = self.state_dict['i']
        ax.plot(capital, income, label='Income per capita')
        ax.plot(capital, investment, label='Investment per capita')
        # plot_growth(): visualize the relationship between 
        #    income per capita, investment per capita, and capital accumulate. 
        # (i.e., income per capita & investment per capita against capital )



# Section 3. Specify model parameters and examine economic grwoth
# set parameters (exgoneousely given):
parameters = {'n': np.array([0.002]),                 # population growth rate
              's': np.array([0.15]),                  # saving rate
              'alpha': np.array([1/3]),               # share of capital
              'delta': np.array([0.05]),              # depreciation rate
              'a': np.array([1])                      # technology 
              }

states = {              # factor productivity
          'k': np.array([1]),
          'L': np.array([100])}


# instantiate a growth model
model = Growth_Model(parameters, states)

# simulate the growth
model.growth(100)

# 3.2  visualize the growth by
# (a). plotting income per worker (y), investment per worker (i),
#   and break-even investment against capital per worker (k).
model.graph_a()



# (b) plotting aggregate income (Y) against time.
output = model.state_dict
n = len(output['Y'])
income = output['Y']
time = np.linspace(0, n, n)
plt.plot(time, income)
plt.xlabel('Time')
plt.ylabel('Income')
plt.show()



# 3.2  find the steady state of the model
result, itera = model.find_steady_state()
print("y_star i_star c_star :")
print(result)

# 3-4. how many iterations it take to converge to the steady state?
print("iteration: ")
print(itera)


# Section 4. Use the growth model class to perform "what-if" analysis.
# see canvas for detailed requirements

# 4.1
parameters = {'n': np.array([0.002]),                 # population growth rate
              's': np.array([0.33]),                  # saving rate
              'alpha': np.array([1/3]),               # share of capital
              'delta': np.array([0.05]),              # depreciation rate
              'a': np.array([1])                      # technology
              }

states = {              # factor productivity
          'k': np.array([1]),
          'L': np.array([100])}


model = Growth_Model(parameters, states)
model.growth(250)

result, itera = model.find_steady_state()
print("y_star i_star c_star :")
print(result)

# 4.2
parameters = {'n': np.array([0.002]),                 # population growth rate
              's': np.array([0.50]),                  # saving rate
              'alpha': np.array([1/3]),               # share of capital
              'delta': np.array([0.05]),              # depreciation rate
              'a': np.array([1])                      # technology
              }

states = {              # factor productivity
          'k': np.array([1]),
          'L': np.array([100])}



model = Growth_Model(parameters, states)
model.growth(10000)
result, itera = model.find_steady_state()
print("y_star i_star c_star :")
print(result)
"""
Answers to 4.1 and 4.2

4.1 the c* of 30% savings is 1.689

4.2 the c* of 50% savings is 1.550

I find it interesting more savings leads to a lower c* . . . I think there must be an optical c* and 50% saving is too much

"""

