import numpy as np
import matplotlib.pyplot as plt

#Controlled Sampling Rate and Signal for Reference
f_signal = 8
t_controlled = np.arange(0, 1, 0.001)
g_controlled = np.sin(2 * np.pi * f_signal * t_controlled)

rates = [50, 25, 10, 5]

for i in rates:
    t_sampled = np.arange(0, 1, 1/i)
    g_sampled = np.sin(2 * np.pi * f_signal * t_sampled)

    plt.figure()
    plt.plot(t_sampled, g_sampled, label = "Signal")
    plt.xlabel("Time, t (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Time vs Amplitude at {i} Hz")
    plt.legend()
    plt.grid()

    plt.savefig(f"sampling_rate_plots_{i}Hz.png")
    plt.close()

