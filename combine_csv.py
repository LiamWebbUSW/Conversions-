import pandas as pd
import glob
import os.path


file_path = "C:/Users/j20ra/OneDrive - University of South Wales/API PC downloads/upload paper 4 18_07_2025/neoutputs/"

data = []
for csvfile in glob.glob(os.path.join(file_path, "walesrt2025_07_11*.csv")):
    df = pd.read_csv(csvfile, encoding="utf-8", delimiter=",")
    data.append(df)

data = pd.concat(data, ignore_index=True)
data.to_csv("C:/Users/j20ra/Documents/merged/nemerged/merged11_07.csv")

#xmlmerge tests/*.xml > combine.xml
