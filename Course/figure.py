import pylab

pylab.figure(1)
pylab.plot([0,1,2,3,4,5,6],[1,2,4,8,16,32,64],'r-')
pylab.title('Test My pylab Library')
pylab.xlabel('X-Label ',fontsize=20)
pylab.ylabel('Y-Label',fontsize=20)
pylab.show()