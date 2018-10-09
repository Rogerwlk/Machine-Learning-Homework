import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

f = open('data/train.csv', 'r')
header = f.readline()
images = []
labels = []
sample_digits = {}

# set up 10 subplots for 10 digits
fig = plt.figure(tight_layout=True)
ax = [fig.add_subplot(2, 5, x) for x in range(1, 11)]
for a in ax:
	a.axes.get_xaxis().set_visible(False)
	a.axes.get_yaxis().set_visible(False)

# read file, draw one sample digit and store sample digit
for line in f:
	temp = line.strip().split(',')
	temp = [int(x) for x in temp]
	labels.append(temp[0])
	images.append(np.array(temp[1:]))
	if temp[0] not in sample_digits:
		img = np.reshape(images[-1], (28, 28))
		ax[temp[0]].imshow(img, cmap='gray')
		sample_digits[temp[0]] = temp[1:]
fig.savefig('sample_digits.png')
fig.clf()

# ref: https://matplotlib.org/gallery/statistics/hist.html
fig, ax = plt.subplots(tight_layout=True)
ax.hist(labels, bins=10, density=True) # normalized histogram
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1)) # set y-axis
fig.savefig('histogram.png')
fig.clf()

f.close()