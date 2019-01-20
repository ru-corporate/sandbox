"""Download and truncate Rosstat corporate dataset."""

from boo import download, build, read_dataframe

print("Please be prepared download and build operations "
      "can take several minutes!")

# download raw file from Rosstat
#download(2012)

# create truncated version with fewer columns and rename columns 
#build(2012)

# read trimmed version as dataframe
df = read_dataframe(2012)

print("Here is a summary of 2012 dataset:")
print(df.describe().transpose())
