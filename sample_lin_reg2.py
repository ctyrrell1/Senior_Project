from numpy import arange,array,ones,linalg,corrcoef,std
from pylab import plot,show
import csv


filename = 'C:/Users/Corey/Desktop/CSCI/Senior Project/samples/sample2.txt'

data = csv.reader(open(filename, 'r'), delimiter = ",", quotechar = '|')
xi, y = [], []
for row in data:
    xi.append(row[0])
    y.append(row[1])

i = 0
for val in xi:
    xi[i] = float(val)
    i+=1
i = 0
for val2 in y:
    y[i] = float(val2)
    i+=1

x = array(xi)
A = array([ x, ones(len(x))])

# linearly generated sequence
m, c = linalg.lstsq(A.T,y)[0] # obtaining the parameters
# m is the correlation coefficient * the standard deviation of y divided by the standard deviation of x

# plotting the line
def plot_linreg():
    plot(x, y, 'o')
    plot(x,m*x + c,'r')
    show()


#now find the standard deviation and the correlation coefficient to predict, for reference only
#stdx = std(x)
#stdy = std(y)
#r = m / (stdy/stdx)  #correlation coefficient

#make a prediction
def predict_linreg(testnum):
    prediction = c + m * float(testnum)
    return prediction
