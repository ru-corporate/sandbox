"""Download and truncate Rosstat corporate dataset."""

from boo import download, build, read_dataframe

print("Please be prepared: "
      "download and build operations "
      "can take long time!")

year = 2017

# Download raw file from Rosstat
try:
    download(year)
except FileExistsError:
    print("Raw file already downloaded")

# Select fewer columns and assign short column names
# Will save to new file
try:
    build(year)
except FileExistsError:
    print("Work file already created")

# Read data as dataframe
df = read_dataframe(year)

print(year, "dataset:", df.shape[0], "rows and", df.shape[1], "columns")

