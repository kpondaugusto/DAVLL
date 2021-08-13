#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 09:44:30 2021

@author: kierapond
"""


import pandas as pd 
import matplotlib.pyplot as plt


############################# Read files #############################

df4 = pd.read_csv('alpha45phi35.CSV',low_memory=False)
df5 = pd.read_csv('alpha45phi45.CSV',low_memory=False)
df6 = pd.read_csv('alpha45phi55.CSV',low_memory=False)


#print(df_final)


############################# Delete all Column except for CH3 which is CH1-CH2 or #############################
############################# the difference signal and 1 Time #############################

keep_col4 = ['TIME','CH3']
new_df4 = df4[keep_col4]

keep_col5 = ['CH3']
new_df5 = df5[keep_col5]
#new_df2.to_csv("newalpha45phi0.csv", index=False)

keep_col6 = ['CH3']
new_df6 = df6[keep_col6]
#new_df3.to_csv("newalpha50phi0.csv", index=False)

print(new_df4)

############################# Rename Columns #############################

new_df4.columns = ['Time','CH3 35']

new_df5.columns = ['CH3 45']

new_df6.columns = ['CH3 55']

#df3.rename(columns={'CH3': 'CH350'})


############################# Link Data #############################

data_out = pd.concat([-new_df4,-new_df5,-new_df6],axis=1)

print(data_out)


############################# Plot #############################


x='Time'

# y='CH4'

# z='CH3'

# w='CH2'

# v='CH1'

data_out.plot(x)
#df.plot(x,z)

plt.title('Difference Signal as a Function of Time for Resonance 1 axis=3deg for Change in Phi')
plt.show()



