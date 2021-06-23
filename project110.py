import plotly.figure_factory as ff
import pandas as pd
import random
import statistics as s
import plotly.graph_objects as go
df=pd.read_csv('project110.csv')
data=df["reading_time"].tolist()
populationMean=s.mean(data)
populationSd=s.stdev(data)
print("Mean: ",populationMean)
print("Standard Deviation: ",populationSd)
#sampleSd=s.stdev(dataSet)
#print("Sample Mean: ",sampleMean)
#print("Sample SD: ",sampleSd)
def showFig(meanList): 
    df=meanList
    mean=s.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.3],mode="lines",name="Mean"))
    fig.show()
def extract(counter): 
    dataSet=[]
    for i in range(0,counter): 
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)
    sampleMean=s.mean(dataSet)
    return sampleMean
def setup(): 
    meanList=[]
    for i in range(0,1000): 
        setOfMeans=extract(100)
        meanList.append(setOfMeans)
    showFig(meanList)
setup()
