#rain_temp_per_year.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def averageTrend_Temp(avTemp_per_year, listChange = [], changes = 0, listAverageTrend = []) -> List[float]:
	#First we calculate the amount change year over year
	for i in range(len(avTemp_per_year['Temperature'])):
		if i < len(avTemp_per_year['Temperature']) - 1:
			listChange += [(avTemp_per_year.iloc[i + 1]['Temperature'] - avTemp_per_year.iloc[i]['Temperature'])]
	#Now we average the amount of change over the years
	for change in listChange:
		changes += change
	mean = changes / len(listChange)
	
	#Now we group the y values for the average trend line
	for i in range(len(avTemp_per_year['Temperature'])):
		listAverageTrend += [avTemp_per_year['Temperature'][0] - 0.1 + mean * (i) ]
	return listAverageTrend	

def averageTrend_Rain(avRain_per_year, listChange = [], changes = 0, listAverageTrend = []) -> List[float]:
	#First we calculate the amount change year over year
	for i in range(len(avRain_per_year['Rainfall'])):
		if i < len(avRain_per_year['Rainfall']) - 1:
			listChange += [(avRain_per_year.iloc[i + 1]['Rainfall'] - avRain_per_year.iloc[i]['Rainfall'])]
	#Now we average the amount of change over the years
	for change in listChange:
		changes += change
	mean = changes / len(listChange)
	
	#Now we group the y values for the average trend line
	for i in range(len(avRain_per_year['Rainfall'])):
		listAverageTrend += [avRain_per_year['Rainfall'][0] + 50 + mean * (i) ]
	return listAverageTrend		


def main ():
	#Get the info from the two csv files
	amazonRainfall = pd.read_csv('average_rainfall_monthly.csv')
	amazonTemp = pd.read_csv('average_temperature_monthly.csv')
	
	#Creating a sub dataframe where we can show the average temperature per year
	avTemp_per_year = amazonTemp.groupby('Year')['Temperature'].mean()
	avTemp_per_year = avTemp_per_year.to_frame() #it gives us a series so we covert it to a dataframe
	avTemp_per_year = avTemp_per_year.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	avTemp_per_year['Year'] = avTemp_per_year['Year'].values.astype(str)
	
	#Creating a sub dataframe where we can show the average rainfall(mm, milimeters) per year
	avRain_per_year = amazonRainfall.groupby('Year')['Rainfall'].sum()
	avRain_per_year = avRain_per_year.to_frame() #it gives us a series so we covert it to a dataframe
	avRain_per_year = avRain_per_year.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	avRain_per_year['Year'] = avRain_per_year['Year'].values.astype(str)

	#Create the trends lines for rain and temperature
	listAverageTrend_temp = averageTrend_Temp(avTemp_per_year)
	listAverageTrend_rain = averageTrend_Rain(avRain_per_year)
	
	#Temp
	plt.plot(avTemp_per_year['Year'], avTemp_per_year['Temperature'], label = 'Average Temperature per Year') #Create bargraph with these parameters
	plt.plot(avTemp_per_year['Year'], listAverageTrend_temp, label = 'Trend Line')
	plt.tick_params(axis = 'x', labelrotation = -45, length = 3, pad = 4, labelsize = 'medium') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'medium') #setting the y-values paramters
	#length: length of the ticks, pad: distance between ticks and label, labelsize: size of labels, can be with str or float values, grid_alpha: transparency of grid
	#zorder: the order in which elements appear on top of eachotherç
	plt.suptitle('Evolution of Temperature in Brazil', weight = 'bold') #Shows overall title of graph, paramter of boldness
	plt.title('Data from Years 1998 - 2016', size = 10) ##subtitle of graph, paramter of size
	plt.ylabel('Temperature(Cº)') #sets x-axis label
	plt.xlabel('Year') #sets y-axis label
	plt.legend()
	plt.grid(True, 'both', zorder = 0, alpha = 0.5) #grid in both x and y axis, it goes beneath the graph which is why the zorder is 0, alpha is trasnparency level
	plt.show() #Show graph

	#Rainfall
	plt.plot(avRain_per_year['Year'], avRain_per_year['Rainfall'], label = 'Rainfall per Year') #Create bargraph with these parameters
	plt.plot(avRain_per_year['Year'], listAverageTrend_rain, label = 'Trend Line')
	plt.tick_params(axis = 'x', labelrotation = -45, length = 3, pad = 4, labelsize = 'medium') #setting the x-values parameters
	plt.tick_params(axis = 'y', length = 3, pad = 4, labelsize = 'medium') #setting the y-values paramters
	plt.suptitle('Evolution of Rainfall in Brazil', weight = 'bold') #Shows overall title of graph, paramter of boldness
	plt.title('Data from Years 1998 - 2016', size = 10) ##subtitle of graph, paramter of size
	plt.ylabel('Rainfall(mm)') #sets x-axis label
	plt.xlabel('Year') #sets y-axis label
	plt.legend()
	plt.grid(True, 'both', zorder = 0, alpha = 0.5) #grid in both x and y axis, it goes beneath the graph which is why the zorder is 0, alpha is trasnparency level
	plt.show() #Show graph

if __name__ == '__main__': main()