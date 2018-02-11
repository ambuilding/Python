## Classify whisky

- Pandas
  - Series: 1d array-like
  - DataFrame: 2d array-like, it represents talbe-like data(row and column)
- load a CSV file, view the beginning and end of a Pandas DataFrame
- index a Pandas DataFrame by location
- explore correlations in your data
  - plot a correlation matrix
  - find out about correlation of different flavor attributes.

- use spectral co-clustering to cluster whiskies based on their flavor profiles
  - find clusters of whiskeys in our correlation matrix of whiskey flavors.

-  compare correlation matrices

### prepare plots in Bokeh, a library designed for simple, interactive plotting.

- create the names and colors we will use to plot the correlation matrix of whisky flavors.
  - use these colors to plot each distillery geographically.

- define a function `location_plot(title, colors)`
  - takes a string title and a list of colors corresponding to each distillery
  - outputs a Bokeh plot of each distillery by latitude and longitude.
  - display the distillery name, latitude, and longitude as hover text.

- We see that there is not very much overlap between the regional classifications and the coclustering classifications.
  - This means that regional classifications are not a very good guide to Scotch whisky flavor profiles.
