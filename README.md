# DAVLL
To set up the DAVLL system, the paper "Laser frequency stabilization using linear magneto-optics" by Valeriy V. Yashchuk, Dmitry Budker, and John R. Davis. Published by the American Institute of Physics. Vol. 71, No. 2, Feb. 2000. DOI: 10.1063/1.1150205. url: http://dx.doi.org/10.1063/1.1150205. was followed. 

Graphs on pg. 343 were recreated for both resonances and both quater wave plate axis as it was uncertain which was the fast axis and which was the slow axis. 

There are 4 folders. r1-a3 is the first resonance where the axis is defined as 3deg. r1-a93 is the first resonance where the axis is defined as 93deg. r2-a3 is the second resonance where the axis is defined as 3deg. r2-a93 is the second resonance where the axis is defined as 93deg. 

The graphs that are changes in alpha have a constant phi where phi is along the axis. The graphs that are changes in phi have a constant alpha=43deg. 

Parameters: 

Negative terminal: fluxuates between -10.29 - -10.41 V. 

Positive terminal: fluxuates between +10.38 - +10.49 V. 

Linear polarizer is at 43deg defined as 45deg - where both beams coming out of the Wallisten Crystal were about 2.2mW. 

Quarter Wave Plate - Axes found at 3/183deg and 93/273deg by put the linear polarizer at either all horiontal or all vertical and rotating the quarter wave plate until 1 beam was coming out of the Wallisten Crystal. Not sure which is the fast axis and which is the slow axis.

The laser frequancy is sweeped by 1 Hz, 4 Vpp, and 50% symmetry to get a triagnlar wave.

The "CH_ Peak Detect" column in the .csv files are ignored as that column is reading the max and min voltage at each time. It is made for ns pulses and my pulse is much slower (more like ms). So we just want the actual reading from the signal at each time. 
