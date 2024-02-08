#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:19:38 2022

@author: kierapond
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/kierapond/Documents/GitHub/DAVLL/r2-a93/alpha50phi0.csv',skiprows=range(0,15),low_memory=False)


print(df)


plt.plot(df) #green one i think - idk which one it is??? 