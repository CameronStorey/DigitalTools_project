import pandas as pd
import numpy as np
import time


times_file = open('times.txt', 'w')

df = pd.DataFrame(np.random.randn(10**6, 4), columns=list('ABCD'))   #create a dataframe with random values
df['E'] = df['D']   #make the fifth column a copy of the fourth one, in order to have two identical columns

start_feather = time.time()
df.to_feather('Feather')
end_feather = time.time()
times_file.write("The required time using Feather format is: " + str(end_feather-start_feather) + " seconds " + '\n')

start_hdf = time.time()
df.to_hdf('HDF', key= 'df')
end_hdf = time.time()
times_file.write("The required time using HDF format is: " + str(end_hdf-start_hdf) + " seconds " + '\n')

start_parquet = time.time()
df.to_parquet('Parquet')
end_parquet = time.time()
times_file.write("The required time using Parquet format is: " + str(end_parquet-start_parquet) + " seconds " + '\n')

readFrame = pd.read_feather('Feather', columns=None, use_threads=True)
print(readFrame)
