#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:44:07 2021

@author: kierapond
"""

import pandas as pd 
import matplotlib.pyplot as plt

############################# Read files #############################

df = pd.read_csv('alpha55phi0.CSV',low_memory=False)
df2 = pd.read_csv('alpha45phi0.CSV',low_memory=False)
df3 = pd.read_csv('alpha50phi0.CSV',low_memory=False)

#df_final = pd.merge(df2, df3, how = 'inner', on = 'TIME')

#print(df_final)




############################# Delete all Column except for CH3 which is CH1-CH2 or #############################
############################# the difference signal #############################

keep_col2 = ['CH3']
new_df2 = df2[keep_col2]
#new_df2.to_csv("newalpha45phi0.csv", index=False)

keep_col3 = ['CH3']
new_df3 = df3[keep_col3]
#new_df3.to_csv("newalpha50phi0.csv", index=False)

#print(new_df2)

############################# Rename Columns #############################

new_df2.columns = ['CH3 45']

#df3.rename(columns={'CH3': 'CH350'})


############################# Order Columns #############################

new_columns = []
for i in range(len(df.columns)):
    new_columns.extend([df.columns[i],df2.columns[i],df3.columns[i]])

#print (new_columns)

############################# Link Data #############################

data_out = pd.concat([df,new_df2,new_df3],axis=1)

print(data_out)


############################# Plot #############################


x='TIME'

y='CH4'

z='CH3'

w='CH2'

v='CH1'

data_out.plot(x,legend=False)
#df.plot(x,z)
data_out.legend([TIME,CH1,CH2,CH3,CH4,CH3,CH3],['Time','CH1','CH2','CH3 at r'\alpha'=45','Frequency','CH3 at r'\alpha'=45','CH3 at r'\alpha'=45'])


plt.show()