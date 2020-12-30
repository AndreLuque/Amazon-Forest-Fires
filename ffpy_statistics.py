#ffpy_statistics.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List
import math 

def meanFFPY(forest_fire_per_year) -> float:
	#We add all the number of fires together and divide by the total number of years to obtain an average per year
	totalFires = forest_fire_per_year['number'].sum()
	totalYears = len(forest_fire_per_year['year'])
	return totalFires / totalYears

def medianFFPY(forest_fire_per_year) -> int or float:
	#We see which number is in the center of all the data for the number of forest fires
	#First, we put the values of the number column in a list and put it in order 
	listNumbers = forest_fire_per_year['number'].values.astype(int)
	listNumbers = sorted(listNumbers)
	#If it is an even number of years than we will average out the two middle numbers. If it is an odd number of years than we will choose the middle one.
	totalYears = len(listNumbers)
	if totalYears % 2 == 0:
		year = totalYears // 2
		return int((listNumbers[year - 1] + listNumbers[year]) / 2) 
	else:
		year = totalYears // 2
		return listNumbers[year]

def rangeFFPY(forest_fire_per_year) -> int:
	#To find the range first we must obtain the highest and lowest number of forest fires in a year
	maxValue = forest_fire_per_year['number'][0]
	minValue = forest_fire_per_year['number'][0]
	for number in forest_fire_per_year['number']:
		if number > maxValue:
			maxValue = number
		if number < minValue:
			minValue = number
	return int(maxValue - minValue), int(maxValue), int(minValue)	

def IQrangeFFPY(forest_fire_per_year, median:float or int, listNumbers = [], list1 = [], list2 = []) -> int:
	#First, we put the values of the number column in a list and put it in order 
	listNumbers = forest_fire_per_year['number'].values.astype(int)
	listNumbers = sorted(listNumbers)
	#We have to change the method depending on if the amoutn of numbers is odd or even
	if len(listNumbers) % 2 == 0:
		#The numbers that are lower than the median go in one half and the others in the other half
		for number in listNumbers:
			if number < median:
				list1 += [number]
			else:
				list2 += [number]	
		#Depending if the amount of numbers is even or odd we will calculate the mean again one way or another		
		if len(list1) % 2 == 0:
			year = len(list1) // 2
			Q1 = int((list1[year - 1] + list1[year]) / 2) 
			Q3 = int((list2[year - 1] + list2[year]) / 2) 
		else:
			year = totalYears // 2
			Q1 = list1[year]
			Q3 = list2[year]
	else:
		for number in listNumbers:
			#The numbers that are in a lower position than the position of the number that is the median go in one half and the others in the other half
			if number < index(median):
				list1 += [number]
			else:
				list2 += [number]
		#Depending if the amount of numbers is even or odd we will calculate the mean again one way or another			
		if len(list1) % 2 == 0:
			year = len(list1) // 2
			Q1 = int((list1[year - 1] + list1[year]) / 2) 
			Q3 = int((list2[year - 1] + list2[year]) / 2) 
		else:
			year = totalYears // 2
			Q1 = list1[year]
			Q3 = list2[year]	
	#We return the difference between the two quartiles that is the IQR, and the values of the two quartiles (25% and 75%)		
	return Q3 - Q1, Q1, Q3				

def varianceFFPY(forest_fire_per_year, mean:float, sum_squared_diff = 0) -> float:
	#We have to find the differnce between each of the numbers and the mean and square it, and sum them all together
	for number in forest_fire_per_year['number']:
		sum_squared_diff += (mean - number) ** 2
	#Dividing that by the total amount of numbers that we have is the variance and square rooting the variance we have the standard deviation	
	return sum_squared_diff // len(forest_fire_per_year['number']),  math.sqrt(sum_squared_diff // len(forest_fire_per_year['number']))

def skewFFPY(forest_fire_per_year, mean:float, median:float, standardDeviation: float, part1 = 0, part2 = 0) -> float:	
	#Fisher-Pearson standarized moment coefficient
	for number in forest_fire_per_year['number']:
		part2 += ((number - mean) / standardDeviation) ** 3
	part1 = len(forest_fire_per_year['number']) / ((len(forest_fire_per_year['number']) - 1) * (len(forest_fire_per_year['number']) - 2))
	return part1 * part2

def yearOveryearFFPY(forest_fire_per_year, listPercentages = [], percentages = 0) -> float and List[float]:
	#First we calculate the percentage change year over year
	for i in range(len(forest_fire_per_year['number'])):
		if i < len(forest_fire_per_year['number']) - 1:
			listPercentages += [(forest_fire_per_year['number'][i + 1] - forest_fire_per_year['number'][i]) * 100 / forest_fire_per_year['number'][i]]
	#Now we average the percentages over the years
	for percentage in listPercentages:
		percentages += percentage
	return percentages / len(listPercentages), listPercentages		

def main ():
	amazonData = pd.read_csv('amazon.csv')
	#Creating a sub dataframe where we can show the total amount of forest fires per year
	forest_fire_per_year = amazonData.groupby('year')['number'].sum()
	forest_fire_per_year = forest_fire_per_year.to_frame() #it gives us a series so we covert it to a dataframe
	forest_fire_per_year = forest_fire_per_year.reset_index(level = 0) #the year now becomes the index so we set a new index as normal integers
	forest_fire_per_year['number'] = forest_fire_per_year['number'] * 1000 #Numbers are in thousands
	forest_fire_per_year['year'] = forest_fire_per_year['year'].values.astype(str) #Change the values to str so we dont get decimal years
	
	#Statistics:
	#mean, median(good to use in case of outliers), range(interquartile range), standard deviation(square root of variance), variance, skew, year over year%
	mean = meanFFPY(forest_fire_per_year)
	median = medianFFPY(forest_fire_per_year)
	Range, maxValue, minValue = rangeFFPY(forest_fire_per_year)
	IQR, Q1, Q3 = IQrangeFFPY(forest_fire_per_year, median)
	variance, standardDeviation = varianceFFPY(forest_fire_per_year, mean)
	skew = skewFFPY(forest_fire_per_year, mean, median, standardDeviation) #If it is negative value means its left-skewed, bigger values to the right
	yearOveryear, listPercentages = yearOveryearFFPY(forest_fire_per_year)

if __name__ == '__main__': main()