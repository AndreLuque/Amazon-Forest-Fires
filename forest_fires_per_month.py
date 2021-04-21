#forest_fires_per_month.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def forest_fires_per_month():
	amazonData = pd.read_csv('amazon.csv')
	#Creating a sub dataframe where we can show the total amount of forest fires per month
	forest_fires_per_month = amazonData.groupby('month')['number'].sum()
	forest_fires_per_month = forest_fires_per_month.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fires_per_month = forest_fires_per_month.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fires_per_month['number'] = forest_fires_per_month['number'] * 1000 #Numbers are in thousands
	forest_fires_per_month = forest_fires_per_month.reindex([4, 3, 8, 0, 7, 6, 5, 1, 11, 10, 9, 2]) #The months come out in a inccorect order so we adjust the positions

	plt.bar(forest_fires_per_month['month'], forest_fires_per_month['number'], color = 'r', zorder = 3, width = 0.5) #Create bargraph with these parameters
	plt.ticklabel_format(style = 'plain', axis = 'y') #Making the y-values not be inn scientific notation
	plt.tick_params(axis = 'x', labelrotation = -45, length = 3, pad = 4, labelsize = 'small') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'x-small') #setting the y-values paramters
	#length: length of the ticks, pad: distance between ticks and label, labelsize: size of labels, can be with str or float values, grid_alpha: transparency of grid
	#zorder: the order in which elements appear on top of eachother

	plt.suptitle('Amazon Forest Fires Over the Years', weight = 'bold') #Shows overall title of graph, paramter of boldness
	plt.title('Data from Years 1998 - 2017', size = 10) #subtitle of graph, paramter of size
	plt.ylabel('nº of Forest Fires') #sets x-axis label
	plt.xlabel('Year') #sets y-axis label

	for i, num in enumerate(forest_fires_per_month['number']):
		plt.text(i, num + 500000, str(int(num // 1000)) + 'e3' , ha = 'center', fontsize = 5)
	plt.grid(True, 'both', zorder = 0, alpha = 0.5) #grid in both x and y axis, it goes beneath the graph which is why the zorder is 0, alpha is trasnparency level

