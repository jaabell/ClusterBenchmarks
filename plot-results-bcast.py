import matplotlib.pyplot as plt
import numpy as np
import glob

files = glob.glob("./results-bcast/test-bcast-size-*.txt")

# print(files)


# file = files[0]

for file in files:

	data = np.genfromtxt(file,dtype=None, names=("N","Time"))

	# print(data)

	N = [t[0] for t in data]
	t = [t[1] for t in data]

	plt.figure()
	plt.semilogx(N,t,".")
	plt.title(file)
	plt.xlabel("Bcast $N$")
	plt.ylabel("Time (s)")



plt.show()