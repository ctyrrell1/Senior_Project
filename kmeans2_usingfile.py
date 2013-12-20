from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
import csv

# data generation
#data = vstack((rand(150,2) + array([.5,.5]),rand(150,2)))

filename = 'C:/Users/Corey/Desktop/CSCI/Senior Project/samples/sample2.txt'

data = csv.reader(open(filename, 'r'), delimiter = ",", quotechar = '|')
xi = []
for row in data:
    xi += [[float(row[0]), float(row[1])]]

x = vstack(xi)


# computing K-Means with K = 2 (2 clusters)
#centroids,_ = kmeans(x,3)
# assign each sample to a cluster
#idx,_ = vq(x,centroids)

# some plotting using numpy's logical indexing


def predict_cluster(xaxis, yaxis):
    centroids,_ = kmeans(x,3)
# assign each sample to a cluster
    idx,_ = vq(x,centroids)
    predict_this = array([xaxis, yaxis])
    diffarr = abs(centroids[0] - predict_this)
    best = diffarr[0] + diffarr[1]
    best_centroid = centroids[0]
    for i in range(len(centroids)):
        diffarr = abs(centroids[i] - predict_this)
        diff = diffarr[0] + diffarr[1]
        if diff < best:
            best = diff
            best_centroid = centroids[i]
    return best_centroid

def plot_cluster():
    centroids,_ = kmeans(x,3)
# assign each sample to a cluster
    idx,_ = vq(x,centroids)
    plot(x[idx==0,0],x[idx==0,1],'ob',
         x[idx==1,0],x[idx==1,1],'or',
         x[idx==2,0],x[idx==2,1],'oy')
    plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
    show()
