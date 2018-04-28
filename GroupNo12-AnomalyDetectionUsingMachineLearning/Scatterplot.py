#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('clusters.csv',header=0)
"""
Remove # to get the desired graph
"""

#sns.stripplot(x="RecordNumber", y="SourceName",hue="cluster",data=df,jitter=True);
#sns.stripplot(x="RecordNumber", y="TaskCategory",hue="cluster",data=df,jitter=True);
#sns.stripplot(x="RecordNumber", y="EventCode",hue="cluster",data=df,jitter=True);
#sns.stripplot(x="RecordNumber", y="EventType",hue="cluster",data=df,jitter=True);
#sns.stripplot(y="SourceName", x="EventCode",hue="cluster",data=df,jitter=True);
#sns.stripplot(y="SourceName", x="EventType",hue="cluster",data=df,jitter=True);
#sns.stripplot(y="TaskCategory", x="EventCode",hue="cluster",data=df,jitter=True);
#sns.stripplot(y="TaskCategory", x="EventType",hue="cluster",data=df,jitter=True);
#sns.stripplot(y="EventType", x="EventCode",hue="cluster",data=df,jitter=True);
sns.stripplot(y="SourceName", x="TaskCategory",hue="cluster",data=df,jitter=True);

plt.show()
