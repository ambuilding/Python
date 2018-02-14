## Classify whisky

- Pandas
  - Series: 1d array-like
  - DataFrame: 2d array-like, it represents talbe-like data(row and column)
  - `whisky` is a pandas dataframe
- load a CSV file, view the beginning and end of a Pandas DataFrame， index it by location
  - Regions file contains the regions in which each of the whiskies produced.
  - Whiskies file contains all other details about the whiskies.

```
  (['Body', 'Sweetness', 'Smoky', 'Medicinal',
    'Tobacco', 'Honey', 'Spicy', 'Winey', 'Nutty', 'Malty', 'Fruity',
    'Floral'], dtype='object')
```

- explore correlations in your data
  - plot a correlation matrix
  - find out about correlation of different flavor attributes.

- use spectral co-clustering to cluster whiskies based on their flavor profiles
  - find clusters of whiskeys in our correlation matrix of whiskey flavors.

- compare correlation matrices.
  - draw the clusters as groups that we just discovered in our whisky DataFrame.
  - `Group` is a column consisting of distillery group memberships.
  - rename the indices to match the sorting.
  - `correlations` is a two-dimensional np.array with
  - both rows and columns corresponding to distilleries and
  - elements corresponding to the flavor correlation of each row/column pair

### prepare plots in Bokeh, a library designed for simple, interactive plotting.

- the analysis of Scotch whiskies.
  - an interactive grid plot using Bokeh.
  -  plot the correlations among distillery flavor profiles as well as
  - plot a geographical map of distilleries colored by region and flavor profile.
- create the names and colors, plot the correlation matrix of whisky flavors.
  - use these colors to plot each distillery geographically.

- define a list `correlation_colors` with string values corresponding to colors to be used to plot each distillery pair.
  - Low correlations among distillery pairs will be white,
  - high correlations will be a distinct group color if the distilleries from the same group,
  - and gray otherwise.

- make an interactive grid of the correlations among distillery pairs based on the quantities
- plotting geographic points.

- define a function `location_plot(title, colors)`
  - takes a string title and a list of colors corresponding to each distillery
  - outputs a Bokeh plot of each distillery by latitude and longitude.
  - display the distillery name, latitude, and longitude as hover text.
  - `Region` is a column of in the pandas dataframe whisky, containing the regional group membership for each distillery.

- plot each distillery, colored by region and taste coclustering classification, respectively.
  - Create the list `region_cols` consisting of the color in `region_colors` that corresponds to each whisky in `whisky.Region`.
  - Create a list `classification_cols` consisting of the color in `cluster_colors` that corresponds to each cluster membership in `whisky.Group`.
  -  How well do the coclustering groupings match the regional groupings?

- We see that there is not very much overlap between the regional classifications and the coclustering classifications.
  - This means that regional classifications are not a very good guide to Scotch whisky flavor profiles.
