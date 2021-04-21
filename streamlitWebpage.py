import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from forest_fires_per_year import *
from rain_temp_per_year import *
from ffpy_statistics import *
from ffpy_probabilities import *
from forest_fires_per_month import *
from ffpm_pie import *
from ffpm_statistics import *
from ffpy_states import *
from ffps_pie import *

def main ():
	#getting the data form excel file
	amazonData = pd.read_csv('amazon.csv')

	#Introduce the title of the webpage
	st.title('AMAZON FOREST FIRES (1998-2017)')

	#show a brief intro of the data that we will be working with
	st.header('Introduction:')
	st.text(f'The amazon dataset has (rows, columns) {amazonData.shape}') #size of dataframe (rows, columns)
	st.text(f'Basic dataset structure')
	st.table(amazonData.head()) #shows us first rows
	st.text('Brief description of the dataset')
	st.table(amazonData.describe(include = 'all')) #Brief description of dataframe

	#st.text(f'Number of missing values: ')
	#st.table(amazonData.isna().sum()) #Shows us if their are any mising values
	#If we wanted to take out all the info with 0 forest fires
	#amazonData = amazonData.replace(0, np.nan)
	#amazonData = amazonData.dropna(subset=['number'])

	#Forest fires throughout the years. Main Factors. Statistics and Probability analysis.
	st.text('')
	st.header('Forest fires per year. Factors. Statistics and Probability.')
	#we have to define fig, ax subplots because of security threading reasons
	st.text('')
	st.text('The following is a graph of the number of forest fires')
	st.text('per year from 1998 to 2017.')
	fig1, ax1 = plt.subplots()
	ax1 = forest_fires_per_year()
	st.pyplot(fig1)

	st.text('Now we observe two graphs that show how temperature and rainfall has varied')
	st.text('throughout the same years.')
	fig2, ax2 = plt.subplots()
	ax2 = temp_per_year()
	st.pyplot(fig2)

	fig3, ax3 = plt.subplots()
	ax3 = rain_per_year()
	st.pyplot(fig3)
	st.text('There is a strong correlation between the data, as the temperature increases and rainfall') 
	st.text('decreases, the number of forest fires per year go up.')

	st.text('')
	st.text('Below we have completed a statistical analysis of the data and created a table')
	st.text('to better understand in detail the numbers and define the information in a more precise way')
	dictStatistics1 = ffpy_statistics()
	dfStatistics1 = pd.DataFrame(list(dictStatistics1.items()), columns = ['Values', 'Parameters'])
	st.table(dfStatistics1)


	st.text('')
	st.text('The probabilities of the quantity of forest fires that happen over')
	st.text('one year follow a normal distribution as seen by the Gaussian Bell.')
	fig4, ax4 = plt.subplots()
	ax4 = ffpy_probabilities()
	st.pyplot(fig4)

	st.text('')
	st.header('Forest fires per month. Pie Charts. Statistics.')
	st.text('')
	st.text('The following is a graph of the total number of forest fires')
	st.text('in each month from 1998 to 2017.')
	fig5, ax5 = plt.subplots()
	ax5 = forest_fires_per_month()
	st.pyplot(fig5)

	st.text('')
	st.text('We can see the percentage of the total forest fires each month takes up with the pie chart.')
	fig6, ax6 = plt.subplots()
	ax6 = pie1()
	st.pyplot(fig6)

	st.text('')
	st.text('This can be represented better if we are to compare most affected months with all others.')
	fig7, ax7 = plt.subplots()
	ax7 = pie2()
	st.pyplot(fig7)

	st.text('')
	st.text('Below we have completed a statistical analysis of the data and created a table')
	st.text('to better understand in detail the numbers and define the information in a more precise way')
	dictStatistics2 = ffpm_statistics()
	dfStatistics2 = pd.DataFrame(list(dictStatistics2.items()), columns = ['Values', 'Parameters'])
	st.table(dfStatistics2)

	st.text('')
	st.header('Forest fires in each State. Pie charts.')
	st.text('')
	st.text('The following is a graph of the number of forest fires')
	st.text('per year in each state from 1998 to 2017.')
	fig8, ax8 = plt.subplots()
	ax8 = ffpy_states()
	st.pyplot(fig8)
	st.text('When can see how a few states have the grand majority of total forest fires.')

	st.text('')
	st.text('This can be illustrated very clearly using pie charts as seen below.')
	fig9, ax9 = plt.subplots()
	ax9 = pie3()
	st.pyplot(fig9)

	st.text('')
	fig10, ax10 = plt.subplots()
	ax10 = pie4()
	st.pyplot(fig10)

if __name__ == '__main__': main()	
