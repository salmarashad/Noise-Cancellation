import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft


#third octave frequencies
C3 = 130.81 
D3 = 146.83
E3 = 164.81
F3 = 174.61
G3 = 196
A3 = 220
B3 = 246.93

#fourth octave frequencies 
C4 = 261.62
D4 = 293.66
E4 = 329.62
F4 = 349.22
G4 = 392
A4 = 440
B4 = 493.86


#time ranging from 0-3, resolution of 12*1024 (high)
t = np.linspace(0,3, 12 * 1024)
#number of samples 
N = 3*1024



# notes played 
left=[G3,G3,A3,G3,C3,B3,G3,G3,A3,G3,0,0]
right=[0,C4,A3,0,0,0,G3,0,0,0,D4,C4]

#time 
startnote=[0,  0.2, 0.3, 0.5, 0.5, 0.7, 1, 1.1, 1.3, 1.5, 1.8, 2.4, 3 ]
duration=[0, 0.2, 0.1, 0.2, 0.0, 0.2, 0.3, 0.1, 0.2, 0.3, 0.3, 0.6, 0.6 ]

#x stores the waveform, initialising with 0's
x = np.zeros(len(t))   
i = 0
while i < 12:
    #creating each sinosoid
    x1 = np.sin(2*np.pi*left[i]*t)
    x2 = np.sin(2*np.pi*right[i]*t)
    #add to waveform with appropriate time range 
    x += ( (x1+x2) * ((t>=startnote[i]) & (t <= (startnote[i] + duration[i]))) )
    i += 1
    
#normalising the amplitudes  
x = x / np.max(np.abs(x))

#og in freqency domain
x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:int(N/2)])

#creation of noise 
fn1 = np.random.randint(0, 512)
fn2 = np.random.randint(0, 512)
n1 = np.sin(2 * np.pi * fn1 * t)
n2 = np.sin(2 * np.pi * fn2 * t)
noise = n1 + n2
#og with noise added 
xn = x + noise

#og with noise in frequency domain 
xn_f = fft(xn)
xn_f = 2/N * np.abs(xn_f[0:int(N/2)])

#identifying the peaks 
max_peak_original = np.max(x_f)
#gets highest
threshold = np.ceil(max_peak_original)

# finds the indices of peaks in xnf above the threshold (a tuple)
peak_indices = np.where(xn_f > threshold)[0]

#frequency range 
f= np. linspace(0 , 512 , int(N/2))

# get the corresponding frequencies
fn1 = f[peak_indices[0]]
fn2 = f[peak_indices[1]]

# round the frequencies at the indices
f_rounded = np.round(f[peak_indices])

# filter the noise by subtracting two tones with the rounded frequencies
x_filtered = xn - (np.sin(2 * np.pi * f_rounded[0] * t) + np.sin(2 * np.pi * f_rounded[1] * t))
x_filtered_f = fft(x_filtered )
x_filtered_f = 2/N * np.abs(x_filtered_f[:len(f)])


    

plt.subplot(6, 1, 1)
plt.plot(t, x)
plt.title('Original Tune')
sd.play(x, 12 * 1024)
sd.wait()

plt.subplot(6, 1, 2)
plt.plot(f, x_f)
plt.tight_layout() 
plt.show()

plt.subplot(6, 1, 3)
plt.plot(t, xn)
plt.title('Original Tune with Noise')
sd.play(xn, 12 * 1024)
sd.wait()

plt.subplot(6, 1, 4)
plt.plot(f, xn_f)
plt.tight_layout() 
plt.show()

plt.subplot(6, 1, 5)
plt.plot(t, x_filtered)
plt.title('Filtered Tune')
sd.play(x_filtered, 12 * 1024)
sd.wait()

plt.subplot(6, 1, 6)
plt.plot(f, x_filtered_f)
plt.tight_layout() 
plt.show()







