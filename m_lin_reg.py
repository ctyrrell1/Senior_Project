from numpy import *
from pylab import plot,show
import csv


filename = 'C:/Users/Corey/Desktop/CSCI/Senior Project/samples/sample3_notitle.txt'

data = csv.reader(open(filename, 'r'), delimiter = " ", quotechar = '|')
xi, y = [], []
count = 0
for count in range(0,4):
    xi.append([])

'''have to adjust these values to add more or less because of data-set size'''
for row in data:
    xi[0].append(row[0])
    xi[1].append(row[1])
    xi[2].append(row[2])
    xi[3].append(row[3])
    y.append(row[4])
i = 0
j = 0 
for val1 in xi:                    #convert all xi to floats from strings
	for val2 in xi[i]:
		xi[i][j]= float(val2)
		j +=1
	i +=1
	j=0
i = 0
for val3 in y:
    y[i] = float(val3)
    i+= 1


#X = vstack([ones(len(xi[0])), xi[0], ones(len(xi[0])), xi[1], ones(len(xi[0])), xi[2], ones(len(xi[0])), xi[3]]).T
X = vstack([xi[0], xi[1], xi[2], xi[3], ones(len(xi[0]))]).T    
a = linalg.lstsq(X, y)[0]

def predict_multireg(x0, x1, x2, x3):
    #predicted_UNI_GPA = a[0] * 3.45 + a[1] * 643 + a[2] * 589 + a[3] * 3.76 + a[4]
    predicted_UNI_GPA = a[0] * x0 + a[1] * x1 + a[2] * x2 + a[3] * x3 + a[4]
    return predicted_UNI_GPA

def plot_multireg():
    plothelper = a[3] * array(xi[3]) + a[4]
    plot(xi[3], y, 'o')
    plot(xi[3], plothelper, 'r')
    show()
