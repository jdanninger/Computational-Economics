import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score


# ============================================================================
# Step 6. replicate EVERYTHING we have done to the train set on the test set
# ============================================================================

# Load the data
train = pd.read_csv("Data/train_set_allnum.csv")
test = pd.read_csv("Data/test_set_allnum.csv")

# Task 6.1. check how many missing values are there for each variable.
# use both total count and percentage together to report the result
# let's drop columns that have more than 10% missing







# Task 6.2. drop variables that have 10% or above missing variables.


# Task 6.3. repeat 6.1 to check missing values again


# to fill missings, we need to first separate numerical and categorical values

# Task 6.4. split the test_set into two dataframes:
# # test_num that only include numerical variables
# # test_cat that only include non-numerical variables


# among the still-missings, let's first fill in the numerical values
# Task 6.5. use mean replacement to impute missing values for "MasVnrArea"
x


# Task 6.6. use knn algorithm to impute missing values for "GarageYrBlt"
# let's drop the variable id, as it does not provide any information


# Task 6.7. use the most frequent value to fill all missing categorical vars
# other fancy algorithms (on your own, domain knowledge)


# Task 6.8 combine test_num and test_cat back together as test_set


# Task 6.9. repeat Task 6.1 to check missing value again


# Task 6.10. Create two new features that might be useful for prediction
# Task 6.10.1. add Total Square feet = TotalBsmtSF + 1stFlrSF + 2ndFlrSF
test_num['TotalSF']

# task 6.10.2 add bedroom to total room ratio as a new feature
test_num['Bed_ratio']

# Task 6.11.. in this task, we will deal with skewed numeric features
# Task 6.11.1 check for variable skewness


# Task 6.11.2 get a list of highly skewed variables


# Task 6.11.3 Split the df test_num into two parts, based on if the features
# are highly skewed.


# Task 6.11.4 use log-transform to adjust the highly skewed data


# Task 6.11.5 merge the unskewed_num_data and skewed_num_data back to test_num



# Task 6.12. In this task, we will deal with categorical variables
# Task 6.12.1. convert all "object" dtype to "category" dtype


# Task 6.12.2 check the data description file to see if any catagorical features
# has ordinal relationship.

# in particular, any categorical variables that have numerical meanings,
# we need to perform ordinal encoding for them
# the sklearn library has a ordicalEncoder class designed for this purpose,
# here, let's just do it mannually.


# check codebook and we find:
# # ExterQual     (Ex, Gd, Ta, Fa, Po),
# # ExterCond     (Ex, Gd, Ta, Fa, Po),
# # HeatingQC     (Ex, Gd, Ta, Fa, Po),
# # KitchenQual   (Ex, Gd, Ta, Fa, Po),
# # BsmtQual      (Ex, Gd, Ta, Fa, Po, NA)
# # BsmtCond      (Ex, Gd, Ta, Fa, Po, NA)
# # GarageQual    (Ex, Gd, Ta, Fa, Po, NA)
# # GarageCond    (Ex, Gd, Ta, Fa, Po, NA)
# # BsmtExposure  (Gd, Av, Mn, No, NA)
# # BsmtFinType1  (GLQ, ALQ, BLQ, Rec, LwQ, Unf, NA)
# # BsmtFinType2  (GLQ, ALQ, BLQ, Rec, LwQ, Unf, NA)
# # Functional: (Typ, Min1, Min2, Mod, Maj1, Maj2, Sev, Sal)
# # GarageFinish: (Fin, RFn, Unf, NA)

# Task 6.12.3. encoding categorical features with ordinal relationship
# Encoding rules:
# for ExterQual, ExterCond, HeatingQC BsmtQual, BsmtCond,
# KitchenQual, GarageQual, GarageCond
# NA = 0, Po = 1, Fa = 2, TA = 3, Gd = 4, Ex = 5


# Encoding rules for BsmtExposure:
# NA = 0, No = 1, Mn = 2, Av = 3, Gd = 4



# Encoding rules for BsmtFinType1 and BsmtFinType2:
# GLQ = 6, ALQ = 5, BLQ = 4, Rec = 3, LwQ = 2, Unf = 1, NA = 0


# Encoding rules for Functional:
# Typ=7, Min1=6, Min2=5, Mod=4, Maj1=3, Maj2=2, Sev=1, Sal=0


# Encoding rules for GarageFinish
# Fin=3, RFn=2, Unf=1, NA=0


# Task 6.12.3.combine the above features toghether,
# put them in a df, name it as "num_from_cat"


# Task 6.12.4. double check if all features in num_from_cat are numeric


# Next, we will deal with all the rest categorical features that doesn't have
# ordinal relationships

# Task 6.12.5. drop the num_from_cat part from test_cat, so that
# the df #test_cat only contain categorial variables


# Taks 6.12.6. Use OneHotEncoder in sklearn to convert them into dummies,
# ignore unknwon values when transform

# encoding. here, do not create new object for OneHotEncoder, instead,
# you should use oht.transform() to do the job.


# reforming the dataframe


#  Task 6.12.7. combine num_from_cat and dum_from_cat back to test_cat_to_num


# Task 5.4 lastly, combine test_num and test_cat_to_num back,
# name the new test set as "test_set_allnum"


# Task 6.14 double check if all variables are numeric


# Task 6.15. check if train set and test set have the same number of features
