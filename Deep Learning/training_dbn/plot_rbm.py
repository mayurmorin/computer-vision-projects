# USAGE
# python plot_rbm.py

# import the necessary packages
from sklearn.neural_network import BernoulliRBM
import matplotlib.pyplot as plt
from sklearn import datasets

# load the MNIST dataset and apply min/max scaling to scale the pixel intensity
# values to the range [0, 1]
digits = datasets.load_digits()
data = digits.data.astype("float")
data = (data - data.min(axis=0)) / (data.max(axis=0) + 1e-5)

# train the Restricted Boltzmann Machine on the data
rbm = BernoulliRBM(n_components=64, learning_rate=0.05, n_iter=20, random_state=42,
	verbose=True)
rbm.fit(data)

# initialize the plot
plt.figure()
plt.suptitle("64 MNIST components extracted by RBM")

# loop over the number of components generated by the RBM
for (i, comp) in enumerate(rbm.components_):
	# construct a sub-plot for the component and display the image
	plt.subplot(8, 8, i + 1)
	plt.imshow(comp.reshape((8, 8)), cmap=plt.cm.gray_r, interpolation="nearest")
	plt.xticks([])
	plt.yticks([])

# show the output plot
plt.show()