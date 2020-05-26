import hw_7_4_data

#############
# SIMPLE FILE WRITE
f = open('myfile.txt', 'w') # python will convert it to
                            # open(file='myfile.txt',mode = 'w', encoding='ascii',errors="ignore")

f.write('Hi there!\n')  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it
#############

#############
# SIMPLE FILE WRITE - LINE BY LINE

# file = open(completefilepath,'r',encoding='utf8',errors=None | "ignore")
with open(file=hw_7_4_data.filename, mode="w", encoding="ascii") as file_handle:
    line = ','.join(hw_7_4_data.col_names) + '\n'
    file_handle.writelines(line)
    for line_arr in hw_7_4_data.people_en:
        line = ','.join(line_arr)  # converting an array to CSV line
        file_handle.writelines(line + '\n')
    file_handle.close()

#############
# SIMPLE FILE WRITE - write all lines in 1 batch

with open(file=hw_7_4_data.filename, mode="w", encoding="utf-8") as file_handle:
    lines = list()
    lines.append(','.join(hw_7_4_data.col_names) + '\n')
    for line_arr in hw_7_4_data.people_en:
        lines.append(','.join(line_arr) + '\n')  # converting an array to CSV line

    file_handle.writelines(lines)
    file_handle.close()

# ### end of SIMPLE FILE WRITE ###

# =======
#
# read the file
#
# =============

# the most simple file read
print(' -- the most simple file read -- ')
for line in open(hw_7_4_data.filename):
    csv_row = line.split()  # returns a list ["1","50","60"]
    print(csv_row)

print(' -- simple file read -- ')


# simple read
with open(hw_7_4_data.filename) as file:
    lis = [line.split() for line in file]  # create a list of lists
    for i, x in enumerate(lis):  # print the list items
        print(f'line{i} = {x}')
    file.close()




