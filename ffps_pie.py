#ffpy_pie.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def percentagesNlabels1(forest_fire_per_year_per_state, totalFires:int, listPercentages = [], listLabels = []) -> List[float] and List[str]:
	for i in range(len(forest_fire_per_year_per_state['number'])):
		listPercentages += [(forest_fire_per_year_per_state['number'][i] * 100) / totalFires]
		listLabels += [forest_fire_per_year_per_state['state'][i]]
	return listPercentages, listLabels	

def percentagesNlabels2(forest_fire_per_year_per_state, totalFires:int, listPercentages = [], listLabels = []) -> List[float] and List[str]:
	for i in range(len(forest_fire_per_year_per_state['number'])):
		if i == 10 or i == 20 or i == 12:
			listPercentages += [(forest_fire_per_year_per_state['number'][i] * 100) / totalFires]
			listLabels += [forest_fire_per_year_per_state['state'][i]]	
	listPercentages += [100 - sum(listPercentages)]	
	listLabels += ['Other']
	return listPercentages, listLabels	


def pie3():
	#Total Forest fires per state
	amazonData = pd.read_csv('amazon.csv')
	amazonData['number'] = amazonData['number'] * 1000 #The numbers are in thousands
	#Creating a sub dataframe where we can show the total amount of forest fires per state throughut the years
	forest_fire_per_year_per_state = amazonData.groupby('state')['number'].sum()
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	totalFires = int(forest_fire_per_year_per_state['number'].sum()) #total number of fires from all the years and regions
	
	#First we show pie chart of the whole distribution
	listPercentages, listLabels = percentagesNlabels1(forest_fire_per_year_per_state, totalFires)
	listPercentages = listPercentages[:23]
	listLabels = listLabels[:23]
	plt.pie(listPercentages, labels = listLabels, autopct = "%.2f%%", pctdistance = 0.8, shadow = True, radius = 1.3, 
			textprops = {'fontsize' : 8}, startangle = -50, explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)) 
			#We rotate, create a bigger distance and reduce the font so that the percentages dont overlap
	plt.legend(loc = 'lower right', bbox_to_anchor = (1.7, 0))		

def pie4():
	#Total Forest fires per state
	amazonData = pd.read_csv('amazon.csv')
	amazonData['number'] = amazonData['number'] * 1000 #The numbers are in thousands
	#Creating a sub dataframe where we can show the total amount of forest fires per state throughut the years
	forest_fire_per_year_per_state = amazonData.groupby('state')['number'].sum()
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year_per_state = forest_fire_per_year_per_state.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	totalFires = int(forest_fire_per_year_per_state['number'].sum()) #total number of fires from all the years and regions

	#Now we show the three most at risk regions and the percentage of forest fires that they have
	listPercentages, listLabels = percentagesNlabels2(forest_fire_per_year_per_state, totalFires)
	listPercentages = listPercentages[:4]
	listLabels = listLabels[:4]
	plt.pie(listPercentages, labels = listLabels, explode = (0.15, 0, 0, 0), shadow = True, autopct = "%.2f%%", pctdistance = 0.8, radius = 1)
	plt.legend(loc = 'lower right')	
