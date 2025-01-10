# Noise-Cancellation
This project generates a musical tune, adds synthetic noise, and applies filtering to remove the noise. It visualizes and plays back the original, noisy, and filtered signals.

### Requirements:
- numpy
- matplotlib
- sounddevice
- scipy

  
### Install dependencies with:

```
pip install numpy matplotlib sounddevice scipy
```

### How It Works:
- Tune Generation: Creates a musical tune using sine waves based on predefined notes and timing.
- Noise Addition: Adds random noise by combining sine waves of random frequencies.
- FFT Analysis: Analyzes the signals in the frequency domain and detects noise peaks.
- Noise Filtering: Removes noise by subtracting detected noise frequencies.
- Visualization & Playback: Plots the signals and plays them for comparison.
