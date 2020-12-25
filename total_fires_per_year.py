#AmazonForestFires
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def main ():
	amazonData = pd.read_csv('amazon.csv')
	amazonData.shape #size of dataframe (rows, columns)
	amazonData.head() #shows us first rows
	print(amazonData.describe(include = 'all')) #Brief description of dataframe
	print()
	print('Number of missing values:')
	print(amazonData.isna().sum()) #Shows us if their are any mising values
	
	#If we wanted to take out all the info with 0 forest fires
	#amazonData = amazonData.replace(0, np.nan)
	#amazonData = amazonData.dropna(subset=['number'])

	#Creating a sub dataframe where we can show the total amount of forest fires per year
	forest_fire_per_year = amazonData.groupby('year')['number'].sum()
	forest_fire_per_year = forest_fire_per_year.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year = forest_fire_per_year.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fire_per_year['number'] = forest_fire_per_year['number'] * 1000 #Numbers are in thousands
	forest_fire_per_year['year'] = forest_fire_per_year['year'].values.astype(str) #Change the values to str so we dont get decimal years
	
	plt.bar(forest_fire_per_year['year'], forest_fire_per_year['number'], color = 'b', zorder = 3, width = 0.5) #Create bargraph with these parameters
	plt.ticklabel_format(style = 'plain', axis = 'y') #Making the y-values not be inn scientific notation
	plt.tick_params(axis = 'x', labelrotation = -45, length = 3, pad = 4, labelsize = 'small') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'x-small') #setting the y-values paramters
	#length: length of the ticks, pad: distance between ticks and label, labelsize: size of labels, can be with str or float values, grid_alpha: transparency of grid
	#zorder: the order in which elements appear on top of eachother

	plt.suptitle('Amazon Forest Fires Over the Years', weight = 'bold') #Shows overall title of graph, paramter of boldness
	plt.title('Data from Years 1998 - 2017', size = 10) #subtitle of graph, paramter of size
	plt.xlabel('nº of Forest Fires') #sets x-axis label
	plt.ylabel('Year') #sets y-axis label

	plt.grid(True, 'both', zorder = 0, alpha = 0.5) #grid in both x and y axis, it goes beneath the graph which is why the zorder is 0, alpha is trasnparency level

	plt.show()

if __name__ == '__main__': main()