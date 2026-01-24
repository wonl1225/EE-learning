# Week 01 - Effect of a sampling rate on signals

## Objective
In this project, we will investigate the effect of how many times a discrete measurable value is captured on a continuous sinusoidal signal. Python was used to visualize and simulate the signal under multiple sampling rates.

The sinousodial signal is defined as:

g(t) = cos(2π * fs * t)

where fs represents signal frequency.

The signal was sampled at 4 different rates:

50 Hz

25 Hz

10 Hz

5 Hz

## Observations
Same sinusoidal graph were plotted using four different sampling rates. 

5 Hz: The graph is extremely distorted compared to the expected oscillating sinusoidal waveform. The lack of samples plot a misleading signal.

10 Hz: Although certain portions of the waveform are partially present, the signal lacks accuracy because distortion still remains, caused by the low sampling rate.

25 Hz: Even though it still maintains a rigid look, oscillations of the sinusoidal graph becomes more recognizable. 

50 Hz: This sampled rate produces the most accurate representation out of the 4 different simulations. The high sampling rate causes this plot to resemble the original sinusoidal shape accurately. 

## Explanations

Sampling rate directly represents the number of discrete measurements from a signal over a certain interval. This means when the signal is captured with a low sampling rate, distortion is caused due to its low-sample. With less point of measurements captured, they are connected linearly rather than following the expected waveform. As more data points are collected, it starts to resemble the sinusoidal waveform. 

At lower sampling rates like 5 Hz and 10 Hz, the sinusoidal waveform isn't visible due to lack of captured points. Instead of a smooth, oscillating graph, heavy distortions can be observed.

At higher sampling rates such as 25 Hz and 50 Hz, the graph starts to smoothen out because of the increased captured points.

Such result imply that there is a minimum sampling rate to observe a oscillatory behaviour of a signal. While the calculation and theory behind this phenomenon will be covered in future coursework, this experiment provided an fundamental understanding of the concept.

## Limitations

This python simulation assumes ideal conditions, where it assumes perfectly executed linear interploation between samples collected with noise-free environment. For a real-world hardware system, additional factors such as sensor inaccuracy and noise would affect signal quality.

## Conclusion

This simulation represents how sampling rates affect the accuracy of a continuous-time signal critically in terms of accurate representation. Insufficient sampling and low sampling rate may lead to distorted signals, which directly affect performance and calculations.

This can be also applied to more practical situation, where the continuous-time signal represents AC voltage. P = I_RMS * V_RMS in AC circuits, and RMS value rely on accurate peak-to-peak estimation. Low sampling rate in this situation will systematically underestimate RMS voltage and RMS current, which will lead to inaccurate power calculations with higher errors.
