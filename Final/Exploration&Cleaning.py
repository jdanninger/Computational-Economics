import pandas as pd
import matplotlib.pyplot as plt

tr = pd.read_csv('Raw Data/final_train.csv')

# DATA DESCRIPTION and to check the data types

# MAKE
makes = tr['make'].value_counts().head(50)
print(tr['make'].value_counts().head(50))
# overvation: inconsistent capitalization


# MODEL
models = tr['model'].value_counts()
print(tr['model'].value_counts().head(50))


# Trim
trims = tr['trim'].value_counts()
print(trims.head(50))
# Observation: Trims may not be consistent across models

# Body
bodies = tr['body'].value_counts()
print(tr['body'].value_counts())
# Obervation : Body types are screwy

# transmission
transmissions = tr['transmission'].value_counts()
print(tr['transmission'].value_counts())
# Obersvation: Drop the one Sedan

# State
states = tr['state'].value_counts()
print(tr['state'].value_counts())
# Obervation: drop the one with 3vwd17aj5fm219943

# condition
conditions = tr['condition'].value_counts()
print(tr['condition'].value_counts())
plt.hist(tr['condition'], bins=10)
plt.show()
# LGTM

# Odometer
odometers = tr['odometer'].value_counts()
print(tr['odometer'].value_counts())
# Make odomter a histogram and graph with matplotlib
plt.hist(tr['odometer'], bins=10)
plt.show()
# LGTM


#color
colors = tr['color'].value_counts()
print(tr['color'].value_counts())
# Drop the color 16633

# interior
interior_colors = tr['interior'].value_counts()
print(tr['interior'].value_counts())
#LGTM :)

# seller
sellers = tr['seller'].value_counts()
print(tr['seller'].value_counts())
# lgtm

# mmr
mmrs = tr['mmr'].value_counts()
# print(tr['mmr'].value_counts())
# plt.hist(tr['mmr'], bins=30)
# plt.show()

"""
Overall the data is relatively good but could use some cleaning. Check my notes to see what needs to be cleaned


CLEANING
"""
# MAKE
# Make everything in make lower case for consistency
tr['make'] = tr['make'].str.lower()


# TRIM and MODEL
# Instead create a new column that is the model and make and trim
tr['model'] = tr['model'].str.lower()
tr['trim'] = tr['trim'].str.lower()
tr['make-model-trim'] = tr['make'] + ' ' + tr['model'] + ' ' + tr['trim']


# BODY
def convert(text):
    if 'cab' in text or 'crew' in text:
        return 'truck'
    if text == 'nan':
        return 'missing'
    if 'sedan' in text:
        return 'sedan'
    if 'coupe' in text:
        return 'coupe'
    if 'convertible' in text:
        return 'convertible'
    if 'van' in text:
        return 'van'
    if text == 'koup':
        return 'coupe'
    if 'wagon' in text:
        return 'wagon'
    if 'navitgation' in text:
        return 'sedan'
    else:
        return text
tr['body'] = tr['body'].astype(str)
tr['body'] = tr['body'].str.lower()
tr['body'] = tr['body'].apply(convert)

bodies = tr['body'].value_counts()
# print(tr['body'].value_counts())

tr = tr[tr['transmission'] != 'Sedan']
transmissions = tr['transmission'].value_counts()
# print(tr['transmission'].value_counts())
# drop the tuple with tranmission as Sedan

#state
states = tr['state'].value_counts()
print(states)


# color
# tr = tr[tr['color'] != 16633]
colors = tr['color'].value_counts()
print(tr['color'].value_counts())

