import pandas as pd
import glob

result = pd.DataFrame([])
file_names = glob.glob("abc*")

for i, file in enumerate(file_names):
    print('Appending file ' + str(i + 1) + ' out of ' + str(len(file_names)))
    df = pd.read_csv(file)
    result = result.append(df)

result.to_csv('result.csv')
