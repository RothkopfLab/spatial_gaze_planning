import spm1d
import numpy as np
import pylab as plt
import pandas as pd
import scipy 

dMeans = pd.read_csv("spatialPlanningData.csv", sep = "\t")

print dMeans.head()

shapes = {}
for s in [4,19,26,13]:
    shapes[s] = np.loadtxt("spatialPlanningShape-"+str(s)+".gz")

i = 1
for a,b in dMeans.groupby(["seed"]):
    plt.subplot(2,2,i)
    i += 1

    m1 = b[b.cols == 0][["posX", "posY"]].values
    m2 = b[b.cols == 1][["posX", "posY"]].values
    T2    = spm1d.stats.hotellings2(m1, m2)
    T2i   = T2.inference(0.05)

    for x,y in b.groupby(["cols"]):
        mat = y[["posX", "posY"]].values
        matM = np.array([np.mean(mat, axis = 0)])
        matC = np.array([np.cov(mat.T)])
        plt.scatter(mat[:, 0], mat[:, 1], color = ["red","green", "blue"][x])

    plt.xlim(0,1680)
    plt.ylim(0,1050)
    plt.imshow(scipy.misc.imresize(shapes[a], 1.5),
                    extent = [240, 1440, -75, 1124])



    print "-----" + str(a) + "-----"
    print "Mean Single: " 
    print np.mean(m1,axis = 0)
    print "Cov Single: " 
    print np.cov(m1.T)
    print "Mean Double: " 
    print np.mean(m2,axis = 0)
    print "Cov Single: " 
    print np.cov(m2.T)
plt.show()
