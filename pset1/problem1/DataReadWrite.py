from scipy.linalg import toeplitz
import numpy as np
import math
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from IPython.display import Audio
from matplotlib import rcParams as rc
from scipy.linalg import qr
import wave
import sys
import numpy as np
from scipy import fft, ifft
from scipy.fftpack import fftfreq
import  struct, random
def creatMatrix(N,alpha):
	d = np.zeros((N,N))
	for i in range(0,N):
		k = math.sqrt(alpha/3.14) * math.exp(-alpha*((i)^2))
		b = k * np.eye(N, N, i)
		d = d + b
	Q, R = qr(d)
	c = Q.dot(R.T)
	FinMatrix = d + c - np.eye(N,N,0)
	return FinMatrix
# Нахождение свертки
def Svert(B,X):
	Y = B.dot(X)
	return Y
# Write new signal into a file
def WriteWav(Y,fs_rate,N):
	sampleRate = 44100.0 # hertz
	duration = 1.0 # seconds
	frequency = 440.0 # hertz
	obj = wave.open('sound.wav','w')
	obj.setnchannels(1) # mono
	obj.setsampwidth(2)
	obj.setframerate(fs_rate)
	for i in range(N):
	   #value = Y[i]
	   #data = struct.pack('<h', value)
	   obj.writeframesraw( Y[i] )
	obj.close()
def ReadWav(FileName):
	fs_rate, signal = wav.read(FileName)
	l_audio = len(signal.shape)
	if l_audio == 2:
		signal = signal.sum(axis=1)/2
	N = signal.shape[0]
	secs = N / float(fs_rate)
	Ts = 1.0/fs_rate # sampling interval in time
	t = np.arange(0, secs, Ts)
	if N > 9999:
		NewSignal = signal[0:1000]
		N = 1000
	else:
		NewSignal = signal 
	return t,N,fs_rate,signal,NewSignal