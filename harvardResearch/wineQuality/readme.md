## wine

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
