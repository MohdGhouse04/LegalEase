import pandas as pd
import json

chunks=[]

# -------- IPC chunks ----------
df=pd.read_csv("data/raw/ipc_dataset.csv")

for _,row in df.iterrows():

    txt=f"""
Offense: {row['Offense']}
Description: {row['Description']}
Punishment: {row['Punishment']}
Bailable: {row['Bailable']}
Court: {row['Court']}
"""

    chunks.append({
      "source":"IPC",
      "text":txt.strip()
    })


# -------- Constitution chunks ------
with open("data/processed/constitution_text.json") as f:
    constitution=json.load(f)["text"]

chunk_size=1500
overlap=200

start=0

while start < len(constitution):
    piece=constitution[start:start+chunk_size]

    chunks.append({
      "source":"Constitution",
      "text":piece
    })

    start += (chunk_size-overlap)

# Save
with open("data/processed/chunks.json","w") as f:
    json.dump(chunks,f,indent=2)

print("Total chunks:",len(chunks))