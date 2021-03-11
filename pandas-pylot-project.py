# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:29:53 2021

@author: akshay
"""


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
# %matplotlib inline      only for jupiter notebook
sns.set(color_codes=True)

# reading csv file using pandas

car= pd.read_csv('C:\\Users\\aksha\\Documents\\car_data.csv')


#printing the datas top-bottom
car.head()

#printing the datas bottom-top
car.tail()

# data types
car.dtypes

car.columns
# car.column.values    converts pandas to numpy

# analytical summary of the dataset
car.describe(include='all')

# histogram for visualisation
car.hist(figsize=(20,30))

# relationship between 2 variables using sns.boxplot
ax= sns.boxplot(x="engine_size", y="horsepower", data=car)
#swarmplot() to show the datapoints on top of the boxes
ax=sns.swarmplot(x="engine_size", y="horsepower", data=car)

# for understanding pairwise relationships
sns.pairplot(car)

# removing some columns
car=car.drop(['aspiration','wheel_base','length','width','height','peak_rpm','curb_weight','highway_mpg','fuel_system'], axis=1)
car.head()

# rename columns()
car=car.rename(columns={"city_mpg": "mileage","make":"Brand"})
car.head()

# row which contains duplicate data
duplicate_rows_car= car[car.duplicated()]
print("Number of duplicate rows: ", duplicate_rows_car.shape)
car.count()

# removing duplicates if any (there are no duplicates here)
car=car.drop_duplicates()
car.count()

# Droping nan values if any...cleaning data
car=car.dropna()
car.count()

# Finding null values in the data
print(car.isnull().sum())

# finding the outliers
sns.boxplot(x=car['price'])
sns.boxplot(x=car['engine_size'])

#plotting a histogram for number of cars per brand
car.Brand.value_counts().nlargest(40).plot(kind='bar',figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel("Number of cars")
plt.xlabel("Brand")

# relationship between the variables
c=car.corr()
c

# Corelation using heatmap
# Set up  matplotlib figure
f, ax = plt.subplots(figsize=(20, 15))
sns.heatmap(c, cmap='BrBG', square=True,linewidth=.5,annot=True, cbar_kws={"shrink": .5}, ax=ax)

