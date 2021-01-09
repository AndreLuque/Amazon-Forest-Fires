#AmazonForestFires
#Author: André Luiz Queiroz Costa

import pandas as pd
#from googletrans import Translator
import matplotlib.pyplot as plt
from typing import List

def main ():
	amazonData = pd.read_csv('amazon.csv')
	amazonData['number'] = amazonData['number'] * 1000
	df = amazonData.groupby('state')['number'].sum()
	print(df)

	#Most affected: Mato Grosso, Paraiba, Sao Paulo
	#Least affected: Sergipe, Distrito Federal, Alagoas
	
if __name__ == '__main__': main()