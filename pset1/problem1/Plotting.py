import matplotlib.pyplot as plt
def PlOne(signal,t):
	p1 = plt.plot(t, signal, "g") # plotting the signal
	plt.xlabel('Time')
	plt.ylabel('Amplitude')
	plt.show()
def PlTwo(N,signal,Y,t):
	tnew = t[0:N]
	signalcut = signal[0:N]
	p1 = plt.plot(tnew, signalcut, "g")
	p2 = plt.plot(tnew,Y,"r")
	plt.xlabel('Time')
	plt.ylabel('Amplitude')
	plt.legend(["Original", "Svert"])
	plt.show()