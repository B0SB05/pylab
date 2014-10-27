#! /usr/bin/python
import pylab
import numpy as np

def producePlot(lowTemps, highTemps):
#	for i in range(0,len(lowTemps)):
#		diffTemps.append(int (highTemps[i] - lowTemps [i]))
	diffTemps=list(np.array(highTemps)-np.array(lowTemps))
	pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
	pylab.plot(range(1,32),diffTemps)
	pylab.xlabel('Days')
	pylab.ylabel('Temperature Ranges')
	pylab.show()

def loadWordList(filePath=None):
	if (filePath != None ):
		high=[]
		low =[]
		inFile=open(filePath,'r')
		for line in inFile:
			fields=line.split()
			if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]: 
				continue
			else: 
				high.append(int (fields[1]))
				low.append(int (fields[2]))
	return (low,high)

(low,high)=loadWordList('julyTemps.txt')
producePlot(low,high)
