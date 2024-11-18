# -*- coding: utf-8 -*-
"""4_day.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pgJZ__v86Dlx8-vmTKIprCne9FYYSmRH

# **Data** **Visualization**
"""

#import libraies
import seaborn as sns
import numpy
import scipy
import pandas
import matplotlib.pyplot as plt

# load dataset
df = seaborn.load_dataset("iris")
df

#draw a line plot
sns.lineplot(x='sepal_length',y='sepal_width',data=df)
plt.title('Line Plot')
plt.show()

# Adding limits
sns.lineplot(x='sepal_length',y='sepal_width',data=df)
plt.title('Line Plot')
plt.xlim(4,8)
plt.ylim(2,4)
plt.show()

#change figure
plt.figure(figsize=(10,5))

sns.lineplot(x='sepal_length',y='sepal_width',data=df)
plt.title('Line Plot')
plt.show()

#setting style
sns.set_style("dark")

sns.lineplot(x='sepal_length',y='sepal_width',data=df)
plt.title('Line Plot')
plt.show()

#barplot
sns.barplot(x='species',y='petal_length',data=df)
plt.title('Bar Plot')
plt.show()