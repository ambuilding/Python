import pandas as pd
import numpy as np
import datetime

"""
Put your script to transform the data in the transform() function.

You should read the 311_data.csv file in the work folder,
and use pandas to do the transformations.

Save the results as output1.csv.
"""

def transform():
    datafile = "311_data.csv"
    data = pd.read_csv(datafile)

    df = data[['Created Date','Closed Date','Agency','Borough']]

    def fixClosedDate(date):
        if date is np.NaN:
            return datetime.datetime.today()
        else:
            return datetime.datetime.strptime(date,'%m/%d/%Y %I:%M:%S %p')

    df.loc[:, 'Created Date'] = df.loc[:, 'Created Date'].apply(lambda x:datetime.datetime.strptime(x,'%m/%d/%Y %I:%M:%S %p'))
    df.loc[:, 'Closed Date'] = df.loc[:, 'Closed Date'].apply(fixClosedDate)
    df.loc[:, 'processing_time'] =  df.loc[:, 'Closed Date'] - df.loc[:, 'Created Date']
    df.loc[:, 'start_time_window'] = df.loc[:, 'Created Date'].apply(lambda x: x.hour)

    return df.to_csv('output1.csv')
