import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('Raw Data/final_train.csv')
train['year'] = train['year'].fillna(0)
train['mmr'] = train['mmr'].fillna(-1)
train['condition'] = train['condition'].fillna(-1)
train['odometer'] = train['odometer'].fillna(-100000)
train['make'] = train['make'].fillna('missing')
train['model'] = train['model'].fillna('missing')
train['trim'] = train['trim'].fillna('missing')
train['color'] = train['color'].fillna('missing')
train['interior'] = train['interior'].fillna('missing')
train['seller'] = train['seller'].fillna('missing')
train['state'] = train['state'].fillna('missing')
train['body'] = train['body'].fillna('missing')
train['transmission'] = train['transmission'].fillna('missing')
train['saledate'] = train['saledate'].fillna('missing')


# DATA DESCRIPTION and to check the data types

# MAKE
makes = train['make'].value_counts().head(50)
print(train['make'].value_counts().head(50))
# overvation: inconsistent capitalization


# MODEL
models = train['model'].value_counts()
print(train['model'].value_counts().head(50))


# Trim
trims = train['trim'].value_counts()
print(trims.head(50))
# Observation: Trims may not be consistent across models

# Body
bodies = train['body'].value_counts()
print(train['body'].value_counts())
# Obervation : Body types are screwy

# transmission
transmissions = train['transmission'].value_counts()
print(train['transmission'].value_counts())
# Obersvation: Drop the one Sedan

# State
states = train['state'].value_counts()
print(train['state'].value_counts())
# Obervation: drop the one with 3vwd17aj5fm219943

# condition
conditions = train['condition'].value_counts()
print(train['condition'].value_counts())
plt.hist(train['condition'], bins=10)
# plt.show()
# LGTM

# Odometer
odometers = train['odometer'].value_counts()
print(train['odometer'].value_counts())
# Make odomter a histogram and graph with matplotlib
plt.hist(train['odometer'], bins=10)
# plt.show()
# LGTM


#color
colors = train['color'].value_counts()
print(train['color'].value_counts())
# Drop the color 16633

# interior
interior_colors = train['interior'].value_counts()
print(train['interior'].value_counts())
#LGTM :)

# seller
sellers = train['seller'].value_counts()
print(train['seller'].value_counts())
# lgtm

# mmr
mmrs = train['mmr'].value_counts()
# print(tr['mmr'].value_counts())
# plt.hist(tr['mmr'], bins=30)
# plt.show()



"""
Overall the data is relatively good but could use some cleaning. Check my notes to see what needs to be cleaned


CLEANING
"""
# MAKE
# Make everything in make lower case for consistency
train['make'] = train['make'].str.lower()

#day of week
def get_day_of_week(text):
    if "Mon" in text:
        return "mon"
    elif "Tue" in text:
        return "tue"
    elif "Wed" in text:
        return "wed"
    elif "Thu" in text:
        return "thu"
    elif "Fri" in text:
        return "fri"
    elif "Sat" in text:
        return "sat"
    elif "Sun" in text:
        return "sun"
    return "missing"

train['dayofweek'] = train['saledate'].apply(get_day_of_week)

# Year

def get_year(text):
    if "2014" in text:
        return "2014"
    elif "2015" in text:
        return "2015"
    return "missing"
train['saleyear'] = train['saledate'].apply(get_year)


# Sale month
def get_month(text):
    if "Jan" in text:
        return "jan"
    elif "Feb" in text:
        return "feb"
    elif "Mar" in text:
        return "mar"
    elif "Apr" in text:
        return "apr"
    elif "May" in text:
        return "may"
    elif "Jun" in text:
        return "jun"
    elif "Jul" in text:
        return "jul"
    elif "Aug" in text:
        return "aug"
    elif "Sep" in text:
        return "sep"
    elif "Oct" in text:
        return "oct"
    elif "Nov" in text:
        return "nov"
    elif "Dec" in text:
        return "dec"
    return "missing"
train['salemonth'] = train['saledate'].apply(get_month)

# TRIM and MODEL
# Instead create a new column that is the model and make and trim
train['model'] = train['model'].str.lower()
train['trim'] = train['trim'].str.lower()
train['make-model-trim'] = train['make'] + ' ' + train['model'] + ' ' + train['trim']


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
train['body'] = train['body'].astype(str)
train['body'] = train['body'].str.lower()
train['body'] = train['body'].apply(convert)

bodies = train['body'].value_counts()
# print(tr['body'].value_counts())

train = train[train['transmission'] != 'Sedan']
transmissions = train['transmission'].value_counts()
# print(tr['transmission'].value_counts())
# drop the tuple with tranmission as Sedan

#state
states = train['state'].value_counts()
print(states)


# color
# tr = tr[tr['color'] != 16633]
colors = train['color'].value_counts()
print(train['color'].value_counts())
# train = train.drop['saledate']
# save train as cleaned_train in the /Cleaned Data director
train.to_csv('Cleaned Data/cleaned_train.csv', index=False)






# Fix the Test data to fit same format
test = pd.read_csv('Raw Data/final_test.csv')
test['year'] = test['year'].fillna(0)
test['mmr'] = test['mmr'].fillna(-1)
test['odometer'] = test['odometer'].fillna(-100000)
test['make'] = test['make'].str.lower()
test['model'] = test['model'].str.lower()
test['trim'] = test['trim'].str.lower()
test['make-model-trim'] = test['make'] + ' ' + test['model'] + ' ' + test['trim']
test['body'] = test['body'].astype(str)
test['body'] = test['body'].str.lower()
test['body'] = test['body'].apply(convert)
test = test[test['transmission'] != 'Sedan']
test['color'] = test['color'].astype(str)
test['color'] = test['color'].str.lower()
test = test[test['color'] != '16633']
test['make'] = test['make'].fillna('missing')
test['model'] = test['model'].fillna('missing')
test['trim'] = test['trim'].fillna('missing')
test['condition'] = test['condition'].fillna(-1)

test['color'] = test['color'].fillna('missing')
test['interior'] = test['interior'].fillna('missing')
test['seller'] = test['seller'].fillna('missing')
test['state'] = test['state'].fillna('missing')
test['body'] = test['body'].fillna('missing')
test['transmission'] = test['transmission'].fillna('missing')
test['saledate'] = test['saledate'].fillna('missing')
test['saleyear'] = test['saledate'].apply(get_year)
test['salemonth'] = test['saledate'].apply(get_month)
test['dayofweek'] = test['saledate'].apply(get_day_of_week)
# test = test.drop['saledate']
test.to_csv('Cleaned Data/cleaned_test.csv', index=False)
# save test as cleaned_test in the /Cleaned Data director


print("count: " + str(train['year'].isna().sum()))