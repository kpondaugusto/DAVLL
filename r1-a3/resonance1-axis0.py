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

#print(df_final)


############################# Delete all Column except for CH3 which is CH1-CH2 or #############################
############################# the difference signal and 1 Time #############################

keep_col = ['TIME','CH3']
new_df = df[keep_col]

keep_col2 = ['CH3']
new_df2 = df2[keep_col2]

keep_col3 = ['CH3']
new_df3 = df3[keep_col3]

#print(new_df2)

############################# Rename Columns #############################

new_df.columns = ['Time','55']

new_df2.columns = ['45']

new_df3.columns = ['50']


############################# Link Data #############################

data_out = pd.concat([-new_df,-new_df2,-new_df3],axis=1)

print(data_out)


############################# Plot #############################


x='Time'



data_out.plot(x)

plt.title('Resonance 1, axis=3deg, for Change in alpha')
plt.show()





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

keep_col6 = ['CH3']
new_df6 = df6[keep_col6]

#print(new_df4)

############################# Rename Columns #############################

new_df4.columns = ['Time','35']

new_df5.columns = ['45']

new_df6.columns = ['55']


############################# Link Data #############################

data_out = pd.concat([-new_df4,-new_df5,-new_df6],axis=1)

print(data_out)


############################# Plot #############################


x='Time'

data_out.plot(x)

plt.title('Resonance 1, axis=3deg, for Change in Phi')
plt.show()






