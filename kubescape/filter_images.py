import pandas as pd

# variables
file = "image_scanning/image_scanning_prod_040123.csv"
file_output = "filter_images.csv"

# get file, remove duplicates, write to new file
df = pd.read_csv(file)
df = df.drop(columns=['STAT.', 'SCAN TIME', 'REGISTRY'])
df.drop_duplicates(subset="IMAGE TAG", inplace=True)
df = df.reset_index(drop=True)
df.to_csv(file_output, index=False)
print(df['IMAGE TAG'])