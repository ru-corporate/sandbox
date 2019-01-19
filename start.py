"""Download and trim Rosstat corporate dataset."""

from boo import Corporate

# Please be prepared download and build operations take a long time!

# download row file from Rosstat
Corporate(2012).download()

# create trimmed version with fewer columns, rename columns 
Corporate(2012).build()

# read trimmed version as dataframe
df = Corporate(2012).dataframe()
