
---

### Data Cleaning Steps

1. **Make**
   - Converted all entries to lowercase for consistency.
   - if not there then replaced with "missing".

2. **Model**
   - Converted all entries to lowercase for consistency.
   - if not there then replaced with "missing".

3. **Make Model Trim**
   - Created a new column that combines `make`, `model`, and `trim` into a single string.

4. **Type**
   - Converted all entries to lowercase.
   - if not there then replaced with "missing".
   - Standardized the values to categories: `sedan`, `suv`, `hatchback`, `minivan`, `coupe`, `wagon`, `convertible`, `truck` (including everything with "cab").

5. **Transmission**
   - Dropped the single entry labeled as "Sedan".
   - if not there then replaced with "missing".

6. **States**
   - Dropped the entry with a nonsensical state value.
   - if not there then replaced with "missing".

7. **Color**
   - Dropped the entry with the color value "16633".
   - if not there then replaced with "missing".

8. **Interior**
   - if not there then replaced with "missing".

9. **Odometer**
   - If missing then I set it to -100000

10. **Seller**
    - if not there then replaced with "missing".

11. **MMR**
    - If not there then set to -1

12. **Year**
    - Made missing year a 0

13. **Condition**
    - Made missing condition -1

---


## My Approach
My code is in two files, `Exploration&Cleaning.py` which creates the cleaned data (which is exported to Cleaned Data directory)

The `ML.py` file uses XGBoost to predict the price of the car based on the model created from the train data. The output is in `Predictions.csv`

I've really wanted to use XGBoost since it is a pretty powerful but easy to use model that can handle categorical data. 
As a result I used it and when I had a test train split of .8/.2 it created a RMSE of 2585

I am worried XGBoost may have overfit the data so I will need to do some more testing to see if it is a good model.

Overall I am happy with my results. 