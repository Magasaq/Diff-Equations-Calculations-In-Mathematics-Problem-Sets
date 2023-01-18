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
from Plotting import PlOne,PlTwo
from DataReadWrite import Svert,WriteWav,ReadWav
from GenMat import GenMat
from richardson import Rich

FileName = "1.wav"
t,N,fs_rate,signal,NewSignal = ReadWav(FileName)
alpha = 0.2
Mat = GenMat(N,alpha)
print(Mat)
Y = Svert(Mat,NewSignal)
PlOne(signal,t)
PlTwo(N,signal,Y,t)
WriteWav(Y,fs_rate,N)
X = Rich(Mat,Y,N)