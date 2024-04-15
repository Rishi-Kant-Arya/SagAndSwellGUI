import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
def u(x):
 array = x
 array_cp = []
 for i in range(len(x)):
    if x[i] > 0:
        array_cp.append(1)
    if x[i] <= 0.0:
        array_cp.append(0)
 return np.array(array_cp)

class SineWaveGUI:
 def __init__(self, master):
    self.master = master
    self.master.title("Voltage Sag and Swell generator")
    # Create new frames for the input and output widgets
    self.input_frame = tk.Frame(self.master)
    self.input_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    self.output_frame = tk.Frame(self.master)
    self.output_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
    # Create GUI widgets for voltage sag wave
    self.sag_amplitude_label = tk.Label(self.input_frame, text="Sag voltage Amplitude:")
    self.sag_amplitude_label.grid(row=0, column=0, padx=10, pady=10)
    self.sag_amplitude_entry = tk.Entry(self.input_frame)
    self.sag_amplitude_entry.grid(row=0, column=1, padx=10, pady=10)
    self.sag_frequency_label = tk.Label(self.input_frame, text="Sag voltage frequency:")
    self.sag_frequency_label.grid(row=1, column=0, padx=10, pady=10)
    self.sag_frequency_entry = tk.Entry(self.input_frame)
    self.sag_frequency_entry.grid(row=1, column=1, padx=10, pady=10)
    
    self.sag_percentage_label = tk.Label(self.input_frame, text="Sag percentage:")
    self.sag_percentage_label.grid(row=2, column=0, padx=10, pady=10)
    self.sag_percentage_entry = tk.Entry(self.input_frame)
    self.sag_percentage_entry.grid(row=2, column=1, padx=10, pady=10)
    
    self.sag_start_label = tk.Label(self.input_frame, text="Start time of sag:")
    self.sag_start_label.grid(row=3, column=0, padx=10, pady=10)
    self.sag_start_entry = tk.Entry(self.input_frame)
    self.sag_start_entry.grid(row=3, column=1, padx=10, pady=10)
    
    self.sag_end_label = tk.Label(self.input_frame, text="End time of sag:")
    self.sag_end_label.grid(row=4, column=0, padx=10, pady=10)
    self.sag_end_entry = tk.Entry(self.input_frame)
    self.sag_end_entry.grid(row=4, column=1, padx=10, pady=10)
    
    
    # Create GUI widgets for voltage swell waveform
    self.swell_amplitude_label = tk.Label(self.input_frame, text="Swell voltage Amplitude:")
    self.swell_amplitude_label.grid(row=5, column=0, padx=10, pady=10)
    self.swell_amplitude_entry = tk.Entry(self.input_frame)
    self.swell_amplitude_entry.grid(row=5, column=1, padx=10, pady=10)
    self.swell_frequency_label = tk.Label(self.input_frame, text="Swell voltage Frequency:")
    self.swell_frequency_label.grid(row=6, column=0, padx=10, pady=10)
    self.swell_frequency_entry = tk.Entry(self.input_frame)
    self.swell_frequency_entry.grid(row=6, column=1, padx=10, pady=10)
    
    self.swell_percentage_label = tk.Label(self.input_frame, text="Swell percentage:")
    self.swell_percentage_label.grid(row=7, column=0, padx=10, pady=10)
    self.swell_percentage_entry = tk.Entry(self.input_frame)
    self.swell_percentage_entry.grid(row=7, column=1, padx=10, pady=10)
    self.swell_start_label = tk.Label(self.input_frame, text="Start time of swell:")
    self.swell_start_label.grid(row=8, column=0, padx=10, pady=10)
    self.swell_start_entry = tk.Entry(self.input_frame)
    self.swell_start_entry.grid(row=8, column=1, padx=10, pady=10)
    
    self.swell_end_label = tk.Label(self.input_frame, text="End time of swell:")
    self.swell_end_label.grid(row=9, column=0, padx=10, pady=10)
    self.swell_end_entry = tk.Entry(self.input_frame)
    self.swell_end_entry.grid(row=9, column=1, padx=10, pady=10)
    self.plot_button = tk.Button(self.input_frame, text="Plot", 
    command=self.plot_sag_and_swell_wave)
    self.plot_button.grid(row=10, column=1, padx=10, pady=10)
    # Create a new frame for the plot widget
    self.plot_frame = tk.Frame(self.output_frame)
    self.plot_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    # Create the matplotlib figure and plot objects
    self.figure = Figure(figsize=(5, 5), dpi=100)
    self.sine_plot, self.cos_plot = self.figure.subplots(nrows=2, sharex=True, sharey=True)
    self.figure.subplots_adjust(hspace=0.5)
    # Create the canvas object and add it to the plot frame
    self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
    self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 def plot_sag_and_swell_wave(self):
 # Get user input for amplitude and frequency of sag waveform
    V_nom = float(self.sag_amplitude_entry.get())
    freq = float(self.sag_frequency_entry.get())
    V_sag = float(self.sag_percentage_entry.get()) 
    t0 = float(self.sag_start_entry.get())
    t1 = float(self.sag_end_entry.get())
    
    # Get user input for amplitude and frequency of swell waveform
    V_nom2 = float(self.swell_amplitude_entry.get())
    freq2 = float(self.swell_frequency_entry.get())
    V_swell = float(self.swell_percentage_entry.get()) 
    t2 = float(self.swell_start_entry.get())
    t3 = float(self.swell_end_entry.get())
    # Generate x and y values for sag wave
    x = np.arange(0, 0.2, 0.0002)
    
    y_sin = V_nom*(1 - (V_sag/100)*(u(x - t0) - u(x - t1)))*np.sin(2*np.pi*freq*x)
    
    # Clear existing plot and plot new sag wave
    self.sine_plot.clear()
    self.sine_plot.plot(x, y_sin)
    self.sine_plot.set_xlabel("time(s)")
    self.sine_plot.set_ylabel("Voltage")
    self.sine_plot.set_title("Sag Waveform")
    
    
    # Generate x and y values for swell wave
    x = np.arange(0, 0.2, 0.0002)
    y_cos = V_nom2*(1 + (V_swell/100)*(u(x - t2) - u(x - t3)))*np.sin(2*np.pi*freq2*x)
    
    # Clear existing plot
    self.cos_plot.clear()
    self.cos_plot.plot(x, y_cos)
    self.cos_plot.set_xlabel("time(s)")
    self.cos_plot.set_ylabel("Voltage")
    self.cos_plot.set_title("Swell Waveform")
    self.canvas.draw()
    self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5)
 
if __name__ == '__main__':
 root = tk.Tk()
 app = SineWaveGUI(root)
 root.mainloop()