## Bird migration

### GPS - The global positioning system

#### GPS data can be used to track bird migration patterns
- One fascinating area of research uses GPS to track movements of animals.
- It is now possible to manufacturer a small GPS device that is solar charged,
- so you don't need to change batteries, and use
it to track flight patterns of birds.
- The data comes from the LifeWatch INBO project.
- We will use a small data set that consists of migration data for three gulls named Eric, Nico, and Sanne.


- plot latitude and longitude on a simple 2D plot
  - Latitude and longitude are coordinates along the surface of a sphere, where a standard 2-D plot is a plane.
  - `speed_2d` That is how fast they were flying on a 2D plane that is a local approximation to the curved surface of the earth.

- examine 2D flight speed of the birds
  - deal with data entries that are not numeric.
  - `np.isnan()` make sure that you always examine your data carefully,
  - look for the presence of NaNs before preparing your plots.

- deal with timestamped data using datetime
  - operate on the time and date stamps,
  - measure elapsed time between any two timestamps,
  - convert them(str) into so-called daytime object, that supports our arithmetic operations.
  - timedelta object
  - UTC stands for coordinated universal time, which is an offset that is expressed in hours.

```
If the times that passes between any two consecutive observations was the exact same,
for all observations, we would see one perfectly straight line.

In this case we see a couple of jumps in our curve.
What this indicates to us is that
there are observations that are further apart
from one another than other observations in the data set.
```

- calculate and plot daily mean speed
  - Our data consists of time stamps which are spaced unevenly.
  - have I hit the next day.
  - keep collecting the indices.
  - compute mean speed, next_day plus 1, reset inds
  - identify when exactly Eric carries out his migration.(the high speed)
- find out where he actually migrates from and where does he end up.
- Cartopy
  - a library that provides cartographic tools for Python
  - use Cartopy to plot data on a cartographic projection。
  - plot their projected trajectories on the map.
  - we can see the flight trajectories as before, but in this case, we've used an actual cartographic projection.

```
the flight trajectories superimposed on top of a map
gives us much more insight about
the migratory patterns of these birds.
```

### patterns of flight for each of the three birds in our dataset
#### group the flight patterns by bird and date, and plot the mean altitude for these groupings.

- group the dataframe by birdname and then find the average speed_2d for each bird.
- group the flight times by date and calculate the mean altitude within that day. `?pd.DataFrame.groupby` for help
- group the flight times by both bird and date, and calculate the mean altitude for each.
- find the average speed for each bird and day.
