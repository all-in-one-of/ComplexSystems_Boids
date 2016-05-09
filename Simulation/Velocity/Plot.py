import os;
import os.path;
import sys;
from mpl_toolkits.mplot3d import Axes3D;
import numpy as np;
from numpy import linalg as LA
import matplotlib.pyplot as plt;

totalFrames = 5000;

Avg = [];

for i in xrange(1, totalFrames):
    print "Start writing frame " + str(i) + "...\n";
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

    Avg.append(LA.norm(average));

    f.close();

plt.plot(np.linspace(0, totalFrames, totalFrames + 1), Avg);
plt.show();