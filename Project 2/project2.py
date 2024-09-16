"""
Weekly project 2. The Gale-Shapley algorithm
Due on: September 13, 11:59 PM
"""

# Section 1. Preparation
# 1-1. import all the necessary python modules
import json
import copy


# 1-2. import the datasets
with open('project2_data.json') as f:
    pref = json.load(f)



# Section 2 Extract information from the dataset, 
# 2-1. create a dictionary 'guyprefer' contains mens' preferences
guyprefers = pref['men_preference']

# 2-2. create a dictionary 'galprefer' contains women's preferences
galprefers = pref['women_preference']
    
# 2-3. create a list contains guys who are currently not engaged, 
# sort alphabetically
free_guy = list(guyprefers.keys())
free_guy.sort()

# 2-4. generate an empty dictionary 'engage_book' to store result
engage_book = {}
for gal in list(galprefers.keys()):
    engage_book[gal] = ''


# 2-5. make copies of guyprefers and gal refers
m_prefs = guyprefers.copy()
w_prefs = galprefers.copy()


# Section 3. Impletement the Gale-Shapley algorithm 
# Follow the algorithm flowchart, it should be very helpful

while free_guy:
    curr_guy = free_guy.pop()
    curr_guy_prefs = m_prefs[curr_guy]
    has_match = False
    while not has_match and curr_guy_prefs:
        curr_gal = curr_guy_prefs.pop(0)
        curr_gal_match = engage_book[curr_gal]
        if curr_gal_match == '':
            engage_book[curr_gal] = curr_guy
            has_match = True
        else:
            curr_gal_prefs = w_prefs[curr_gal]
            if curr_gal_prefs.index(curr_guy) < curr_gal_prefs.index(curr_gal_match):
                engage_book[curr_gal] = curr_guy
                free_guy.append(curr_gal_match)
                has_match = True

print(engage_book)




