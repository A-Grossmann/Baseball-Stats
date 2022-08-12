#Calculating the OBP is the sum of H, BB, HBP divided by the sum of AB, BB, HBP, SF
import pandas as pd
import numpy as np 

class baseball_code():

	def fill_with_zero(df):
		df = df.fillna(0, inplace = True)
		return df

	def remove_low_AB(df):
		df.drop(df[df['AB'] <=100].index, inplace = True)
		return df

	def Calculating_OBP(df):
		def Calculating_OBP_Denominator(df):
			df['OBP_Den'] = df.apply(lambda x: (x.AB + x.BB + x.HBP + x.SF), axis = 1)
			df = df.drop(df[df['OBP_Den'] == 0].index,inplace=True)
			return df
		Calculating_OBP_Denominator(df)
		df['OBP'] = df.apply(lambda x: (x.H + x.BB + x.HBP)/(x.OBP_Den), axis = 1)
		return df

	def unique_playerID_list(df):
		player_enteries = df['playerID']
		list_of_players = pd.unique(player_enteries).tolist()
		return list_of_players

	def sum_similar(list_of_players,df):
		career_df = pd.DataFrame(
		{'playerID':[0],'G':[0],'AB':[0],'R':[0],'H':[0],'2B':[0],'3B':[0],
		'HR':[0],'RBI':[0],'SB':[0],'CS':[0],'BB':[0],'SO':[0],
		'IBB':[0],'HBP':[0],'SH':[0],'SF':[0],'GIDP':[0],'OBP':[0],},index = [0])
		headers = ['G','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP','OBP']

		for player in list_of_players:
			player_entry = df[df.playerID == player]
			player_entry.loc['Total']= player_entry.sum(numeric_only =True)
			player_entry.loc['Total','playerID'] = player
			career_df.loc[len(career_df.index)] = player_entry.loc['Total']
		return career_df

