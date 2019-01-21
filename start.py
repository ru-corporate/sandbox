"""Download and truncate Rosstat corporate dataset."""

from boo import download, build, read_dataframe

print("Please be prepared download and build operations "
      "can take several minutes!")

year = 2012

# download raw file from Rosstat
try:
   download(year)
except FileExistsError:
   print("Raw file already downloaded")

# create truncated version with fewer columns and good column names 
try:
   build(year)
except FileExistsError:
   print("Work file already created")    

# read trimmed version as dataframe
df = read_dataframe(year)

print(f"{year} dataset:")
print(df.shape[0], "rows and", df.shape[1], "columns")
