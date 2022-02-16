import csv
from re import T
from unittest import result
import plotly.figure_factory as ff
import statistics
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
stdev=statistics.stdev(data)
print("mean is",mean)
print("median is",median)
print("mode is",mode)

firstS,firstE=mean-stdev,mean+stdev
secondS,secondE=mean-(2*stdev),mean+(2*stdev)
thirdS,thirdE=mean-(3*stdev),mean+(3*stdev)

fig=ff.create_distplot([data],["reading score"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[firstS,firstS],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[firstE,firstE],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondS,secondS],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[secondE,secondE],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))

fig.show()
list_of_data_within_1_stdev=[result for result in data if result > firstS and result <firstE]
list_of_data_within_2_stdev=[result for result in data if result > secondE and result <secondE]
list_of_data_within_3_stdev=[result for result in data if result > thirdE and result <thirdE]


print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(stdev))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_stdev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_stdev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_stdev)*100.0/len(data)))