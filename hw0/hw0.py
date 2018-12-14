# CS5785 Applied Machine Learning
# Homework 0
# Andrea Qiu zq64, Roger Wang rw575

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy

f = open('iris.data')
data = []
label = []
color_dict = {'Iris-setosa': 'r', 'Iris-versicolor': 'g', 'Iris-virginica': 'b'}

for line in f:
	if len(line) > 1:
		temp = line.strip().split(',')
		data.append([float(x) for x in temp[:4]])
		label.append(temp[-1])
data = numpy.array(data)
label = numpy.array(label)
color = [color_dict[l] for l in label]
# 0 sepal length, 1 sepal width, 2 petal length, 3 petal width
label = {0:'sepal length', 1:'sepal width', 2:'petal length', 3:'petal width'}
red_patch = mpatches.Patch(color='red', label='Iris Setosa')
blue_patch = mpatches.Patch(color='blue', label='Iris Versicolour')
green_patch = mpatches.Patch(color='green', label='Iris Virginica')

def plot(x, y, name):
	plt.scatter(data[:,x], data[:,y], color=color)
	plt.xlabel(label[x])
	plt.ylabel(label[y])
	plt.legend(handles=[red_patch,blue_patch,green_patch])
	plt.savefig(name)
	plt.clf()
plot(0, 1, 'plot1.png')
plot(0, 2, 'plot2.png')
plot(0, 3, 'plot3.png')
plot(1, 2, 'plot4.png')
plot(1, 3, 'plot5.png')
plot(2, 3, 'plot6.png')
# plt.scatter(data[:,0], data[:,1], color=color)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.savefig('plot1.png')
# plt.clf()
# plt.scatter(data[:,0], data[:,2], color=color)
# plt.savefig('plot2.png')
# plt.clf()
# plt.scatter(data[:,0], data[:,3], color=color)
# plt.savefig('plot3.png')
# plt.clf()
# plt.scatter(data[:,1], data[:,2], color=color)
# plt.savefig('plot4.png')
# plt.clf()
# plt.scatter(data[:,1], data[:,3], color=color)
# plt.savefig('plot5.png')
# plt.clf()
# plt.scatter(data[:,2], data[:,3], color=color)
# plt.savefig('plot6.png')
# plt.clf()