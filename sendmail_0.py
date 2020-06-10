import smtplib
import csv

filename = 'filename_en.csv'

# read with csv
with open(filename, newline='\n') as csv_file:
    file_handler = csv.reader(csv_file, delimiter=',', quotechar='|')
    cnt = True
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("041aa6eae34402", "cb9ed2edf5ffb2")

        for row in file_handler:
            if cnt:
                cnt = False
                continue

            #Name, Gender, City, Email, Family status
            name = row[0]
            matsav_mishpahti = row[4]
            gender = row[1]
            city = row[2]
            receiver = row[3]
            # print(row[1].Email)

            sender = "Private Person <doe@smtp.mailtrap.io>"

            min1 = 'ה'
            min2 = 'ן'
            if gender == 'f':
                min1 = ''
                min2 = 'נת'

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
    server.close()
    csv_file.close()

print("That's all folks")
