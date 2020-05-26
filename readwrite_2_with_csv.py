import hw_7_4_data
#############
# FILE READ-WRITE using csv module
import csv

with open(hw_7_4_data.filename, newline='\n') as csv_file:
    file_handler = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in file_handler:
        print(', '.join(row))
    csv_file.close()

print(' --- file read with csv module --- ')

with open(hw_7_4_data.filename, "rt", encoding='utf-8') as infile:
    read = csv.reader(infile)
    for row in read:
        print(f'{row}')


