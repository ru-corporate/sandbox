"""Download and truncate Rosstat corporate dataset."""

from boo import Corporate

# Please be prepared download and build operations take a long time!

d = Corporate(2012)

# download row file from Rosstat
d.download()

# create truncated version with fewer columns and rename columns 
d.build()

# read trimmed version as dataframe
df = d.dataframe()

print("Here is the start of 2012 dataset:")
print(df.head())
