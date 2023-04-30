import ltspice
import matplotlib.pyplot as plt
import subprocess
import time

ltspice_path = 'C:/Users/Akshit/AppData/Local/Programs/ADI/LTspice/LTspice.exe'
circuit_file = 'C:/Users/Akshit/Desktop/opamp.asc'
subprocess.Popen([ltspice_path, '-Run', circuit_file])

time.sleep(5)
l = ltspice.Ltspice("C:/Users/Akshit/Desktop/opamp.raw")
l.parse() 

timet = l.get_time() * 1e9
V_source1 = l.get_data('V(v1)')
V_source2 = l.get_data('V(v2)')
V_source3 = l.get_data('V(v3)')
V_source4 = l.get_data('V(v4)')
V_source5 = l.get_data('V(vout)')

print(V_source5)

# Create subplots for each signal
fig, axs = plt.subplots(5, 1, figsize=(8, 15), sharex=True)

# Plot each signal in a separate subplot
axs[0].plot(timet, V_source1, label='V(v1)', color='blue')
axs[0].set_title('V(v1)')
axs[0].set_ylabel('Voltage (V)')
axs[0].set_xlim([timet[0], 100])
axs[0].set_xticks(range(0, 101, 10))
axs[1].plot(timet, V_source2, label='V(v2)', color='red')
axs[1].set_title('V(v2)')
axs[1].set_ylabel('Voltage (V)')
axs[1].set_xlim([timet[0], 100])
axs[1].set_xticks(range(0, 101, 10))
axs[2].plot(timet, V_source3, label='V(v3)', color='green')
axs[2].set_title('V(v3)')
axs[2].set_ylabel('Voltage (V)')
axs[2].set_xlim([timet[0], 100])
axs[2].set_xticks(range(0, 101, 10))
axs[3].plot(timet, V_source4, label='V(v4)', color='purple')
axs[3].set_title('V(v4)')
axs[3].set_ylabel('Voltage (V)')
axs[3].set_xlim([timet[0], 100])
axs[3].set_xticks(range(0, 101, 10))
axs[4].plot(timet, V_source5, label='V(vout)', color='black')
axs[4].set_title('V(vout)')
axs[4].set_ylabel('Voltage (V)')
axs[4].set_xlim([timet[0], 100])
axs[4].set_xticks(range(0, 101, 10))

#Axis Labels
fig.text(0.5, 0.04, 'Time (ns)', ha='center')
fig.text(0.04, 0.5, 'Voltage (V)', va='center', rotation='vertical')

#Legend
plt.legend()

plt.subplots_adjust(hspace=0.5)

plt.show()