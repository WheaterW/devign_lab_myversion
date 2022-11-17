import pandas as pd
dataset = pd.read_json("data/raw/dataset.json")
print(dataset.head(5))