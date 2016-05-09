import os;
import os.path;
import sys;
from mpl_toolkits.mplot3d import Axes3D;
import numpy as np;
from numpy import linalg as LA
import matplotlib.pyplot as plt;

totalFrames = 5000;

Avg = [];
SigmaSq = [];

for i in xrange(2, totalFrames):
    Str = "C:\\Simulation\\Velocity\\frame_" + str(i) + ".txt";
    f = open(Str);

    count = 0;
    line = f.readline();

    average = np.zeros(3);

    while line:
        data = line.split(',');

        if len(data) != 3: 
            continue;

        count += 1;
        average[0] += float(data[0]);
        average[1] += float(data[1]);
        average[2] += float(data[2]);

        line = f.readline();

    average *= 1.0 / count;
    averageNorm = LA.norm(average);
    Avg.append(averageNorm);

    f.close();
    
    print "Starting calculation of variance for frame ", i, "...";
    #================================================
    f = open(Str);
    line = f.readline();
    variance = 0;
    
    while line:
        data = line.split(',');

        if len(data) != 3: 
            continue;
        
        data[0] = float(data[0]);
        data[1] = float(data[1]);
        data[2] = float(data[2]);

        data = np.array(data);
        data -= average;
        dataNorm = LA.norm(data);
        
        variance += (dataNorm-averageNorm)**2;

        line = f.readline();
        
    f.close();

    variance /= count;
    SigmaSq.append(np.sqrt(variance));


X = np.linspace(0, len(Avg)-1, len(Avg));

plt.xlabel('Frames');
plt.ylabel('Average - Std. Deviation');

plt.plot(X, Avg, label='Average');
plt.plot(X, SigmaSq, 'r--', label='Std. Deviation');

plt.legend();
plt.title('Boid Ordering Params - Velocity');

plt.show();