## 3.3 k-Nearest Neighbors classification kNN

- determine the Euclidean distance between two points expressed as NumPy arrays
- find the most common vote in an array or sequence of votes
- Compare two different methods for finding the most common vote
- The most commonly occurring element in a sequence is called mode in statistics.
  - Finding a mode is a common statistics operation.
- find the nearest neighbors of an observation, use it to predict the class of an observation
- generate synthetic data
- make a prediction grid, use enumerate / NumPy meshgrid
- plot the prediction grid, the bias-variance tradeoff
- apply the homemade kNN classifier to a real dataset
  -Compare the performance of the homemade kNN classifier to the performance of the kNN classifier from the scikit-learn module
  - a classic data set created by Ron Fisher in 1933
  - it consists of 150 different iris flowers
  - 50 from each of three different species.
  - For each flower, we have the following covariates:
    - sepal length/width
    - petal length/width

### the quality of wine

- analyze a dataset consisting of an assortment of wines classified as "high quality" and "low quality"
- use k-Nearest Neighbors classification to determine whether or not other information about the wine helps us correctly guess whether a new wine will be of high quality.

- Read in the data as a pandas dataframe using `pd.read_csv(url)`
- inspect the dataset and perform some mild data cleaning.
- scale the numeric data and extract the first two principal components.
  - find the mean and standard deviation along each column of a dataframe by selecting axis=0 in np.mean and np.std

- plot the first two principal components of the covariates in the dataset.
  - The high and low quality wines will be colored using red and blue.
- create a function that calculates the accuracy between predictions and outcomes.
- Because most wines in the dataset are classified as low quality
  - one very simple classification rule is to predict that all wines are of low quality(0).
- use the kNN classifier from scikit-learn to predict the quality of wines in our dataset.
- select a subset of our data to use in our homemade kNN classifier, not the whole dataset(selection).
- use our homemade kNN classifier and compare the accuracy of our results to the baseline.
