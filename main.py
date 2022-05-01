import time
import matplotlib.pyplot as plt
import numpy as np
import math
import random

#exData = [7.3, 8.4, 2.6, 6.3, 2.0, 5.4, 5.0, 9.8]

theta = [0, -45, -90, 180, 90, 45]

def data2Line(exData, theta):
    dataX = []
    dataY = []
    for i in range(6):
        pt = exData[i]
        x = pt * (math.sin(math.radians(theta[i]))) #SOH
        y = pt * (math.cos(math.radians(theta[i]))) #CAH
        dataX.append(x)
        dataY.append(y)
    return dataX, dataY

def main():
    #print(dataCordsX)
    #print(dataCordsY)


    #colors = [0.63342, 0.982739, 0.12383, 0.77777, 0.8102953, 0.293764, 0.3957382, 0.428375]
    colors = ['#000000','#000000','#000000','#000000','#000000','#000000']
    #plt.scatter(x=dataCordsX, y=dataCordsY, s=area, c=colors, alpha=0.5)

    plt.draw()
    while True:
        exData = [random.randrange(0, 14), random.randrange(0, 14), random.randrange(0, 14),
                  random.randrange(0, 14), random.randrange(0, 14), random.randrange(0, 14),
                  random.randrange(0, 14), random.randrange(0, 14)]

        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        gZone = plt.Circle((0, 0), 24, color='g', alpha=1)
        ax.add_patch(gZone)
        yZone = plt.Circle((0, 0), 11, color='y', alpha=1)
        ax.add_patch(yZone)
        rZone = plt.Circle((0, 0), 6, color='r', alpha=1)
        ax.add_patch(rZone)

        dataPoints = []
        for p in range(8):
            if p == 0 and exData[p] <= exData[p+1]:
                dataPoints.append(exData[0])
            elif p == 0 and exData[p] > exData[p+1]:
                dataPoints.append(exData[1])
            elif p == 1:
                continue
            elif p == 4 and exData[p] <= exData[p+1]:
                dataPoints.append(exData[4])
            elif p == 4 and exData[p] > exData[p+1]:
                dataPoints.append(exData[5])
            elif p == 5:
                continue
            elif p == 2:
                dataPoints.append(exData[2])
            elif p == 3:
                dataPoints.append(exData[3])
            elif p == 6:
                dataPoints.append(exData[6])
            elif p == 7:
                dataPoints.append(exData[7])
        print("PRINT", dataPoints)

        dataCordsX, dataCordsY = data2Line(dataPoints, theta)
        scat = ax.scatter(x=dataCordsX, y=dataCordsY, s=200, c=colors, alpha=1)

        label = []
        for i in range(6):
            number = float(dataPoints[i])
            label.append(number)
            #print(label[i])
            plt.plot((0, dataCordsX[i]), (0, dataCordsY[i]), c='k')
            #3, 4, 5, 6
            if i == 3 or i == 4:
                plt.annotate(text=str(label[i]), xy=(dataCordsX[i], dataCordsY[i]),
                             xytext=(dataCordsX[i] - 2, dataCordsY[i] + 1))
            elif i ==5 or i == 6:
                plt.annotate(text=str(label[i]), xy=(dataCordsX[i], dataCordsY[i]),
                             xytext=(dataCordsX[i]-1.4, dataCordsY[i] - 2))
            else:
                plt.annotate(text=str(label[i]), xy=(dataCordsX[i], dataCordsY[i]),
                             xytext=(dataCordsX[i]+1, dataCordsY[i]+1))

        plt.pause(0.1)
        plt.close(fig)

main()

'''
https://matplotlib.org/3.5.0/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
https://stackoverflow.com/questions/52381397/how-to-plot-multiple-points-from-a-list-using-matplotlib
https://matplotlib.org/stable/gallery/animation/animation_demo.html#sphx-glr-gallery-animation-animation-demo-py
'''