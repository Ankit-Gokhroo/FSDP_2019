# Apriori

# Importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])




# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")










"""
https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/
"""

"""
https://pbpython.com/market-basket-analysis.html
"""

"""Another Example
"""
import pandas as pd

df = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
df.head()

"""
There is a little cleanup, we need to do. 
First, some of the descriptions have spaces that 
need to be removed. We’ll also drop the rows that 
don’t have invoice numbers and remove the credit 
transactions (those with invoice numbers containing C).
"""

df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]

df.head()
"""
After the cleanup, we need to consolidate the 
items into 1 transaction per row with each
 product 1 hot encoded. For the sake of keeping
 the data set small, I’m only looking at sales 
 for France. However, in additional code below, 
 I will compare these results to sales from 
 Germany. Further country comparisons would 
 be interesting to investigate.
"""

basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

"""
There are a lot of zeros in the data but we also 
need to make sure any positive values are converted to 
a 1 and anything less the 0 is set to 0. This step will 
complete the one hot encoding of the data and remove the 
postage column (since that charge is not one we wish to 
explore):
"""
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

"""
Now that the data is structured properly, 
we can generate frequent item sets that have a 
support of at least 7% (this number was chosen so that 
I could get enough useful examples):
"""

"""
The final step is to generate the rules with their corresponding support, confidence and lift:
"""
rules = apriori(basket_sets, min_support=0.07,min_confidence = 0.25, min_lift = 3)

results = list(rules)


"""
Other examples

https://github.com/amitkaps/machine-learning/blob/master/cf_mba/notebook/2.%20Market%20Basket%20Analysis.ipynb

Get some sample data from below:
    
https://github.com/theankurkedia/market_basket/blob/master/sample_input.csv
"""

"""
https://www.kdnuggets.com/2016/04/association-rules-apriori-algorithm-tutorial.html/2
"""
"""Implemetation Papers
http://adrem.uantwerpen.be/bibrem/pubs/mampaey-thesis06.pdf
https://www-users.cs.umn.edu/~kumar001/dmbook/ch6.pdf
"""

"""removing the null values from the dataframe
transactions = dataset.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

"""