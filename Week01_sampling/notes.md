# Week 01 - Effect of a sampling rate on signals

## Objective
In this project, we will investigate the effect of how many times a discrete measurable value is captured on signals. Python will be used to simulate the sinusodial graph at different sampling rates.

The sinousodial signal is defined as:
g(t) = cos(2π * fs * t)
, where fs represents signal rate.

The signal will be sampled at 4 different rates:

50 Hz

25 Hz

10 Hz

5 Hz

## Observations
Plotted 4 different graphs with various sampling rates (Manipulated variable). 

5 Hz sampling rate: Distorted graphs compared to the expected oscillating sinusoidal waveform. Inaccurate graph due to low sampling rates

10 Hz: Even though the waveform is partially present, it lacks accuracy as distortion still remains.

25 Hz: Oscillations are more present, and sinusoidal shape is recognizable. However, it still maintains a rigid look.

50 Hz: Even though the smoothness is still lacking, this sampled signal returns the most accurate representation of waveform out of the 4 different simulations conducted.

## Explanation

Sampling rate directly correlates to the number of measurements of amplitude that has been taken over time. This would mean a lesser Hz would result to more distorition in the simulation. To put it simply, it tries to connect the points of measurement linearly rather than following the waveform that should be expected. As more data points are collected, it starts to resemble the sinusoidal waveform. 

At lower sampling rates like 5 Hz and 10 Hz, the sinusoidal waveform isn't visible due to lack of captured points. Instead of a smooth, oscillating graph, heavy distortions can be observed.

At higher sampling rates such as 25 Hz and 50 Hz, the graph starts to smoothen out because of the increased captured points.

## Conclusion

Through this simulation, we found out how sampling rates heavily affect the accuracy of the g(t) function, a continuous-time signal. This can be applied to a real-world situation, where g(t) represents an AC voltage. This information is significant because insufficient sampling rate directly affect digital control performance.

One example is the power calculation within AC circuits, where P = IRMS * VRMS. Low sampling rate directly affects the peak-to-peak calculation in the sinusoidal graph, ultimately causing the calculated power to be less than the actual power.
