#ffpm_statistics.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List
import math
from ffpy_statistics import *	

def ffpm_statistics():
	amazonData = pd.read_csv('amazon.csv')
	#Creating a sub dataframe where we can show the total amount of forest fires per month
	forest_fires_per_month = amazonData.groupby('month')['number'].sum()
	forest_fires_per_month = forest_fires_per_month.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fires_per_month = forest_fires_per_month.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fires_per_month['number'] = forest_fires_per_month['number'] * 1000 #Numbers are in thousands
	forest_fires_per_month = forest_fires_per_month.reindex([4, 3, 8, 0, 7, 6, 5, 1, 11, 10, 9, 2]) #The months come out in a inccorect order so we adjust the positions
	
	#Statistics:
	#mean, median(good to use in case of outliers), range(interquartile range), standard deviation(square root of variance), variance, skew, year over year%
	mean = meanFFPY(forest_fires_per_month, 'month')
	median = medianFFPY(forest_fires_per_month)
	Range, maxValue, minValue = rangeFFPY(forest_fires_per_month)
	IQR, Q1, Q3 = IQrangeFFPY(forest_fires_per_month, median)
	variance, standardDeviation = varianceFFPY(forest_fires_per_month, mean)
	skew = skewFFPY(forest_fires_per_month, mean, median, standardDeviation) #If it is negative value means its left-skewed, bigger values to the right
	monthOverMonth, listPercentages = yearOveryearFFPY(forest_fires_per_month)
	#Comment on outliers how have very high percentages , differ vastly from the rest ,see change in average percentage without them
	#Show the amount we will have in 5 years or 10 years at the pace we are at and then in normal conditions(no catastrophes)

	return {int(mean): 'mean', median: 'median', Range: 'Range', maxValue: 'Maximum Value', minValue: 'Minimum Value', IQR: 'Interquartile Range', Q1: 'Quartile 1', Q3: 'Quatile 3', variance: 'Variance', int(standardDeviation): 'Standard Deviation', skew: 'Skew', (str(monthOverMonth) + '%'): 'Average monthOverMonth Growth'}