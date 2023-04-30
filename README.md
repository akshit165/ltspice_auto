# ltspice_auto

Calculation of LTSpice circuit provided is given in the Circuit Analysis.jpeg.
Vx is calculated initially, then Vout is calculated using nodal analysis of the circuit. 

Vo = (Rf/R1) * ((R5*(R4 * V3 + R3 * V4)*(R1 + R2))/(R4 * R5 * R1 + R3 * R5 * R1 + R3 * R4 * R1 + R4 * R5 * R2 + R3 * R5 * R2 + R3 * R4 * R2) - V1 * R2 - V2 * R1)/(R2)

After the calculation, the equation for Vo with Vx substituted resembles that of an inverting amplifier circuit with a voltage divider network in the feedback path. The resistors R4 and R5 form a voltage divider network that determines the gain of the circuit. The resistors R1 and R2 form a voltage divider network that sets the input voltage to the amplifier, and the feedback resistor Rf determines the amount of output voltage that is fed back to the input. However, the presence of V3 and V4 in the equation suggests that this circuit may be a more complex configuration than a simple inverting amplifier with a voltage divider network in the feedback path.

The python script auto_sim.py uses the ltspice library and matplotlib to simulate and plot the response of a circuit designed in LTSpice. Here's a breakdown of what the script does:

1. Imports the necessary libraries: ltspice, matplotlib, and subprocess.
2. Sets the path to where the LTSpice circuit file is saved, the path to the LTSpice executable, and the save path for the LTSpice output file.
3. Opens the LTSpice circuit file using subprocess.Popen.
4. Pauses the script for 5 seconds to give LTSpice time to simulate the circuit.
5. Parses the output file using ltspice.Ltspice.parse.
6. Extracts the time vector and voltage data for each signal of interest using ltspice.Ltspice.get_time and ltspice.Ltspice.get_data.
7. Creates a 5-subplot figure using matplotlib.pyplot.subplots.
8. Plots each signal in a separate subplot using matplotlib.pyplot.plot.
9. Sets the titles, axis labels, and limits for each subplot using various matplotlib functions.
10. Displays the plot using matplotlib.pyplot.show.

Requirements to run this python script on your PC:-
1. Install matplotlib and ltspice library by using pip in your terminal.
   pip install matplotlib &
   pip intall ltspice
   
2. Change the file_savepath (Line 5) to the directory where the ltspice circuit file (opamp.asc) is saved.
3. Change the ltspice_path (Line 6) to the directory where the LTspice.exe is stored.
