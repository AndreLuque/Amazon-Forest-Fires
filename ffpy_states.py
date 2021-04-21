#ffpy_states.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def ffpy_states():	
	#Total Forest fires per state
	amazonData = pd.read_csv('amazon.csv')
	amazonData['number'] = amazonData['number'] * 1000
	df = amazonData.groupby('state')['number'].sum()
	print(df)
	#Creating a sub dataframe where we can show the total amount of forest fires per state throughut the years
	forest_fire_per_year_per_state = amazonData.groupby(['state','year'])['number'].sum()
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	for state in forest_fire_per_year_per_state['state'].unique()[[10, 12, 20, 1, 6, 21]]:
		df = forest_fire_per_year_per_state.loc[forest_fire_per_year_per_state['state'] == state] 
		df = df.reset_index(level = 0) #Changes the index from year to normal numbers so that we can acces the years column
		df['number'] = df['number'] * 1000 #The values are in thousands
		df['year'] = df['year'].values.astype(str) #Changes the years to value type str so that it will not show decimals
		plt.plot(df['year'], df['number'], label = state)

	plt.ticklabel_format(style = 'plain', axis = 'y') #Making the y-values not be inn scientific notation
	plt.tick_params(axis = 'x', labelrotation = -45, length = 3, pad = 4, labelsize = 'small') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'x-small') #setting the y-values paramters
	#length: length of the ticks, pad: distance between ticks and label, labelsize: size of labels, can be with str or float values, grid_alpha: transparency of grid
	#zorder: the order in which elements appear on top of eachother
	
	plt.suptitle('Comparison in NºForest Fires between Most at Risk and Least at Risk States', weight = 'bold', fontsize = '10') #Shows overall title of graph, paramter of boldness
	plt.title('Data from Years 1998 - 2017', fontsize = 10) #subtitle of graph, paramter of size
	plt.xlabel('nº of Forest Fires') #sets x-axis label
	plt.ylabel('Year') #sets y-axis label	
	plt.legend()