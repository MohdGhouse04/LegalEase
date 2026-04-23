import pandas as pd

df = pd.read_csv("data/raw/ipc_dataset.csv")

print("Rows:", len(df))
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())