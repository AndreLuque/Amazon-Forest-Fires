#description.py
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List


def main ():
	amazonData = pd.read_csv('amazon.csv')
	print(f'The amazon Dataset has (rows, columns) : {amazonData.shape}') #size of dataframe (rows, columns)
	print()
	print(f'The Data is structured like this:')
	print(amazonData.head()) #shows us first rows
	print()
	print()
	print('Brief description of the Dataset:')
	print(amazonData.describe(include = 'all')) #Brief description of dataframe
	print()
	print()
	print('Number of missing values:')
	print(amazonData.isna().sum()) #Shows us if their are any mising values

	#If we wanted to take out all the info with 0 forest fires
	#amazonData = amazonData.replace(0, np.nan)
	#amazonData = amazonData.dropna(subset=['number'])

if __name__ == '__main__': main()