import pandas as pd
import numpy as np
from Batting_Methods import baseball_code as bc


# What type of hits do the players with the top ten get compared to the general population of players

Career_df = pd.read_csv('Career_baseball.csv')
#print(Career_df.mean())
Top_10 = pd.read_csv('Top_10_players.csv')

#print(Top_10.mean())


Top_10.rename(columns = {'2B':'Dub', '3B':'Trip'}, inplace = True)
Career_df.rename(columns = {'2B':'Dub', '3B':'Trip'}, inplace = True)
#Top_10['2B'] =Top_10.apply(lambda x: (x.Dub)/(x.H), axis = 1)

#use a lambda function to calculate percent of Hits 2B 3B HR for each top 10 and general population

def calc_hittype(df):
	df['Single'] = df.apply(lambda x: ((x.H-(x.Dub+x.Trip+x.HR))/x.H), axis = 1)
	df['Dub'] = df.apply(lambda x: ((x.Dub/x.H)), axis = 1)
	df['Trip'] = df.apply(lambda x: ((x.Trip/x.H)), axis = 1)
	df['HR'] = df.apply(lambda x: (x.HR/x.H), axis = 1)
 	
	return df


new_hit_percentage_top_10 = calc_hittype(Top_10)
new_hit_percentage_career = calc_hittype(Career_df)
pd.set_option('display.max_columns', None)
mean_Top_10 = new_hit_percentage_top_10[['Single','Dub', 'Trip','HR']].mean()
mean_career = new_hit_percentage_career[['Single','Dub', 'Trip','HR']].mean()
print(mean_Top_10)
print(mean_career)

