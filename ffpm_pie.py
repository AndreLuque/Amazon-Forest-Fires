#ffpm_pie.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def percentagesNlabels1(forest_fires_per_month, totalFires:int, listPercentages = [], listLabels = []) -> List[float] and List[str]:
	for i in range(len(forest_fires_per_month['number'])):
		print(forest_fires_per_month['month'][i])
		listPercentages += [(forest_fires_per_month['number'][i] * 100) / totalFires]
		listLabels += [forest_fires_per_month['month'][i]]
	return listPercentages, listLabels	

def percentagesNlabels2(forest_fires_per_month, totalFires:int, listPercentages = [], listLabels = []) -> List[float] and List[str]:
	for i in range(len(forest_fires_per_month['number'])):
		if i == 5 or i == 1 or i == 11:
			listPercentages += [(forest_fires_per_month['number'][i] * 100) / totalFires]
			listLabels += [forest_fires_per_month['month'][i]]	
	listPercentages += [100 - sum(listPercentages)]	
	listLabels += ['Other']
	return listPercentages, listLabels	


def main ():
	#Total Forest fires per state
	amazonData = pd.read_csv('amazon.csv')
	#Creating a sub dataframe where we can show the total amount of forest fires per month
	forest_fires_per_month = amazonData.groupby('month')['number'].sum()
	forest_fires_per_month = forest_fires_per_month.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fires_per_month = forest_fires_per_month.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fires_per_month['number'] = forest_fires_per_month['number'] * 1000 #Numbers are in thousands
	totalFires = int(forest_fires_per_month['number'].sum()) #total number of fires from all the months
	
	#First we show pie chart of the whole distribution
	listPercentages, listLabels = percentagesNlabels1(forest_fires_per_month, totalFires)
	plt.pie(listPercentages, labels = listLabels, autopct = "%.2f%%", pctdistance = 0.8, shadow = True, radius = 1.3, 
			textprops = {'fontsize' : 8}, startangle = 80, explode = (0, 0, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0)) 
			#We rotate, create a bigger distance and reduce the font so that the percentages dont overlap
	plt.legend(loc = 'lower right', bbox_to_anchor = (1.6, 0.2))		
	plt.show()

	#Now we show the three most at risk regions and the percentage of forest fires that they have
	listPercentages, listLabels = percentagesNlabels2(forest_fires_per_month, totalFires)
	plt.pie(listPercentages, labels = listLabels, explode = (0.15, 0, 0, 0), shadow = True, autopct = "%.2f%%", pctdistance = 0.8, radius = 1)
	plt.legend(loc = 'lower right')	
	plt.show()

if __name__ == '__main__': main()