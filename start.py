"""Download and truncate Rosstat corporate dataset."""

from boo import download, build, read_dataframe

print("Please be prepared download and build operations "
      "can take several minutes!")

# download raw file from Rosstat
try:
   download(2012)
except FileExistsError:
   print("Raw file already downloaded")

# create truncated version with fewer columns and good column names 
try:
   build(2012)
except FileExistsError:
   print("Work file already created")    

# read trimmed version as dataframe
df = read_dataframe(2012)

print("Here is a summary of 2012 dataset:")
print(df.shape[0], "rows and", df.shape[1], "columns")
