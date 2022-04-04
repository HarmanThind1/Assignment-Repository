# Introduction

This repository makes use of **Salaries.csv** file which contains information about various professors, their ranks, salaries, discipline, sex and years of service.

The objective of the python file is to explain some simple codes of python and eventually plot graph of the salaries of the professors.

# Plot Graphs of Salary

## Import the important libraries
Some importatnt libraries like pandas, numpy and seaborn have been included to execute inbuilt python functions.

## Read the file
Firstly we use `pd.read()` function to read the csv file **Salaries.csv**

## Load Data
Next we use `.head()` function to display the data of first 20 rows for better understanding of the data.

## Data type
Then `.info()` function is used to print information about dataframe.

## Funndamental Statistics
Here we also used `.describe()` function for calculating statistical data like mean, percentile, standard deviation 

## Select Data for female professors
For displaying data just for female professors we used following code `df[ df['sex'] == 'Female']` and renamed it as df_female and then used `.head()` function to display information about first five female professors.

## Mean Salary of Discipline A
To calculate mean salary of discipline A we made use of code `df[ df['discipline'] =='A']` to reach discipine A thereafter we applied `.salary.mean()` to take out the output which is 98331.11

## Plot Graphs 

### Histogram of Salary Data
To plot the histogram of the Salary column `.hist()` function is used along with the code `plt.hist(df['salary'],bins=10, density= True)`

### Barplot of Rank vs Salary
1. First we used `.groupby()` for Rank and Salary and `.count()` function then we used `.plot()` to plot the bar chart.
2. We also used seaborn package to display the bar chart using the following code and defining x and y variable `ax = sns.barplot(x='rank',y ='salary', data=df, estimator=len)`
3. To visualize the chart with more details we split the bar graph on the basis of sex of professors using `ax = sns.barplot(x='rank',y ='salary', hue='sex', data=df, estimator=len)` and got the output.
