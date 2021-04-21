#ffpy_probabilities.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List
from ffpy_statistics import *
import numpy as np
import scipy.stats

def ffpy_probabilities():
	amazonData = pd.read_csv('amazon.csv')
	#Creating a sub dataframe where we can show the total amount of forest fires per year
	forest_fire_per_year = amazonData.groupby('year')['number'].sum()
	forest_fire_per_year = forest_fire_per_year.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year = forest_fire_per_year.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fire_per_year['number'] = forest_fire_per_year['number'] * 1000 #Numbers are in thousands
	forest_fire_per_year['year'] = forest_fire_per_year['year'].values.astype(str) #Change the values to str so we dont get decimal years
	
	mean = meanFFPY(forest_fire_per_year, 'year')
	variance, standardDeviation = varianceFFPY(forest_fire_per_year, mean)
	x = mean + standardDeviation * np.random.randn(10000) #np.random.rand() generates a certain amount of values of a normal distribution
	plt.hist(x, 100, density = True, facecolor = 'y')
	#Plotting a line that shows the perfect normal distribution
	y = np.linspace(0, 60000000, 100)
	plt.plot(y, scipy.stats.norm.pdf(y, mean, standardDeviation), color = 'b')

	plt.ticklabel_format(style = 'plain', axis = 'y') #Making the y-values not be inn scientific notation
	plt.ticklabel_format(style = 'plain', axis = 'x') #Making the x-values not be inn scientific notation
	plt.tick_params(axis = 'x', length = 3, pad = 4, labelsize = 'small') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'x-small') #setting the y-values paramters

	plt.suptitle('Probability of Forest Fires Throughout One Year', weight = 'bold') #Shows overall title of graph, paramter of boldness
	plt.title(f'mu = {mean}   std = {standardDeviation}', size = 8) #subtitle of graph, paramter of size
	plt.ylabel('Probabilities') #sets x-axis label
	plt.xlabel('nº of Forest Fires') #sets y-axis label

	#Add line graph following normal distribution
