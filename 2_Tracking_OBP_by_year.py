import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from Batting_Methods import baseball_code as bc

baseball_df = pd.read_csv('baseball_data_batting.csv')

years = list(range(1871, 2021))
no_of_col = list(range(len(baseball_df.columns)))
print(no_of_col)
pd.set_option('mode.chained_assignment', None)

#create a list of the column names of the baseball_df
column_list_baseball_df = baseball_df.columns.values.tolist()
column_list_baseball_df.append('OBP_Den')
column_list_baseball_df.append('OBP')
baseball_totals_by_year = pd.DataFrame(columns = column_list_baseball_df)

#Create a DataFrame of the baseball statistics by year
for year in years:
	baseball_year =baseball_df[baseball_df.yearID==year]
	baseball_year.loc["Total",:] = baseball_year.sum(axis = 0, numeric_only = True)

	bc.Calculating_OBP(baseball_year)
	row = int(len(baseball_year['playerID']))
	

	row_list = (baseball_year.loc['Total',:]).values.tolist()

	baseball_totals_by_year.loc[len(baseball_totals_by_year)] = row_list

	baseball_totals_by_year.iloc[len(baseball_totals_by_year)-1,[1]] = year
print(baseball_totals_by_year.describe())

#Show a plot through time of the statistics
baseball_totals_by_year.plot('yearID','OBP')
plt.show()