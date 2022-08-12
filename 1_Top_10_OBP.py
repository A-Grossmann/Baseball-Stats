
#The Project here is to:
#				 1. See what players had the highest OBP Average throughout their carreer (Top 10)
#				 2. See the effect of On Base Percentage Over Time(OBP)
#				 3. See what players with high OBP type of hits tend to average more of than the all
#
import pandas as pd
import numpy as np
from Batting_Methods import baseball_code as bc


pd.set_option('mode.chained_assignment', None)

#First obtain the data
baseball_df = pd.read_csv('baseball_data_batting.csv')



# #Create a list of all players
list_of_players = bc.unique_playerID_list(baseball_df)

# #Fill all NaN enteries with zeros
bc.fill_with_zero(baseball_df)

# #Only look at players with more than 100 AB in an entry
bc.remove_low_AB(baseball_df)

# #Calculate the OBP and add it as a column in DataFrame
bc.Calculating_OBP(baseball_df)

# #Create a player sum of states DataFrame
career_df = bc.sum_similar(list_of_players,baseball_df)
bc.Calculating_OBP(career_df)
print(career_df.head())

#Send the top 10 to a csv file
sort_df_by_OBP = career_df.sort_values(by = 'OBP',ascending = False)
sort_df_by_OBP = sort_df_by_OBP.head(10)



#Writing it to a csv files for use in answering other questions
sort_df_by_OBP.to_csv('Top_10_players.csv')
baseball_df.to_csv('baseball_data_with_OBP.csv')
career_df.to_csv('Career_baseball.csv')

print(baseball_df.describe())
