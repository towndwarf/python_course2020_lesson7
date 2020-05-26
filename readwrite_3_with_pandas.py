import hw_7_4_data
import pandas as pd
import pathlib


file = pd.DataFrame(hw_7_4_data.people, columns=hw_7_4_data.col_names)
file.to_csv(hw_7_4_data.filename_utf8, encoding="utf-8")


print('End of the csv file creation')
print(f'At {pathlib.Path(__file__).parent.absolute()}\\{hw_7_4_data.filename_utf8}.')


# read with Panda
print(' --- file read with Panda module --- ')
df = pd.read_csv(hw_7_4_data.filename_utf8, encoding="utf-8")
for d in df.iterrows():
    name = d[1].Name
    matsav_mishpahti = d[1]['Family status']
    gender = d[1].Gender
    city = d[1].City
    print(d[1].Email)