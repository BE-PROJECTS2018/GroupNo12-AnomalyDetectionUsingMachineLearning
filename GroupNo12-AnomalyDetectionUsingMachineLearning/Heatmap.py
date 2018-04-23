#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import catheat
df=pd.read_csv('C:/Users/papibono/Desktop/BE_PROJECT/1521029641_1296.csv',header=0)
# Plot the categorical columns as heatmap
ax = catheat.heatmap( df[['SourceName','TaskCategory','EventCode','EventType']],
                      palette='Paired' )

plt.show()

