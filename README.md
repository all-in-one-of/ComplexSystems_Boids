# ComplexSystems_Boids
A Murmuration implementation in Houdini
To Generate the simulation files open Boids_Python.hipnc. 
- In Houdini open a python terminal
- Copy paste and run the code in the folder HoudiniProjects\Boids\scripts\Export_sym.py. This generates plain text for position of 
  each particle at each frame.
- Do the same for HoudiniProjects\Boids\scripts\Export_sym_v.py to generate velocity data.
- Execute PlotSimulationData.py to plot Average - Std. Deviation for velocity.
- Modify Str = "C:\\Simulation\\Velocity\\frame_" + str(i) + ".txt"; to Str = "C:\\Simulation\\Position\\frame_" + str(i) + ".txt";
  to generate the plot for position.
