import pandas as pd
import smtplib
import time

filename = 'filename_en.csv'

# read with Pandas
print(' --- file read with Pandas module --- ')
df = pd.read_csv(filename, encoding="ascii")  # encoding could be omitted
for row in df.iterrows():
    name = row[1].Name
    matsav_mishpahti = row[1]['Family status']
    gender = row[1].Gender
    city = row[1].City
    # print(row[1].Email)

sender = "Private Person <doe@smtp.mailtrap.io>"

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("041aa6eae34402", "cb9ed2edf5ffb2")
    for row in df.iterrows():
        name = row[1].Name
        matsav_mishpahti = row[1]['Family status']
        gender = row[1].Gender
        min1 = 'ה'
        min2 = 'ן'
        if row[1].Gender == 'f':
            min1 = ''
            min2 = 'נת'
        city = row[1].City
        receiver = row[1].Email

        # family status
        add_family = ''
        if matsav_mishpahti == 'married':
            if gender == 'f':
                add_family = 'together with your handsome husband '
            else:
                add_family = 'together with your charming wife '
        elif matsav_mishpahti == 'in relationships':
            add_family = ' together your spouse '

        to_send = f"Dear {name},\n\
        You {add_family} are heartily invited to participate\
        in a head-bang'ing contest,\n\
        which is to take a place in {city} after the end semester exams."

        message = f"""\
        Subject: You are invited
        To: {receiver}
        From: {sender}
        {to_send}"""
        print(message)
        server.sendmail(sender, receiver, message)
        # time.sleep(20) # sleep for 20 sec
        print('sent as ASCII')

print("That's all folks")
