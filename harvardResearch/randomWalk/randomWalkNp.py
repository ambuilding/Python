import numpy as np
import matplotlib.pyplot as plt

# delta_X = np.random.normal(0, 1, (2, 5))
# X = np.cumsum(delta_X, axis=1)

X_0 = np.array([[0], [0]])
delta_X = np.random.normal(0, 1, (2, 100))
X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis=1)

plt.plot(X[0], X[1], "ro-")
plt.savefig("rw.pdf")
