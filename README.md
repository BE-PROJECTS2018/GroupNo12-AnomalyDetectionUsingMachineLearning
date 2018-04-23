# GroupNo12-AnomalyDetectionUsingMachineLearning
We collected logs using Splunk which were truncated and compiled into the given csv format. 
There are two files 1521029641_1296.csv and testall.csv. 1521029641_1296.csv file consists of all the logs that were generated with some
error message or warning or some anomaly, whereas testall.csv is for all the system logs. 
_________________________________________________________________________________

To execution of the program is in order 
1. kmodes.py : For generation of clusters
2. heatmap.py : generating heatmap diagram
3. Scatterplot.py : generating scatter plot graph
4. Parallelcoords.py: Generating parallel coordinates graph for error logs
5. Parallelcoordsfull.py.: Generating parallel coordinates graph for all the logs