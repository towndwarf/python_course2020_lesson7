import pandas as pd
import smtplib
# from email.message import Message
# from email.header import Header

filename_utf8 = 'filename_utf8.csv'
df = pd.read_csv(filename_utf8, encoding="utf-8")
for d in df.iterrows():
    name = d[1].Name
    matsav_mishpahti = d[1]['Family status']
    gender = d[1].Gender
    city = d[1].City
    print(d[1].Email)

sender = "Private Person <doe@smtp.mailtrap.io>"

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("041aa6eae34402", "cb9ed2edf5ffb2")
    for d in df.iterrows():
        name = d[1].Name
        matsav_mishpahti = d[1]['Family status']
        gender = d[1].Gender
        min1 = 'ה'
        min2 = 'ן'
        if d[1].Gender == 'f':
            min1 = ''
            min2 = 'נת'
        city = d[1].City
        receiver = d[1].Email

        # family status
        add_family = ''
        if matsav_mishpahti == 'married':
            if gender == 'f':
                add_family = ' ביחד עם בעלך '
            else:
                add_family = ' ביחד עם אשתך '
        elif matsav_mishpahti == 'in relationships':
            add_family = ' ביחד עם חברך '

        # configuring mail
        #  msg = Message()
        #  msg['Subject'] = Header('הזמנה לתחרות ב' + city, 'utf-8')
        #  msg['From'] = 'My Test <test@gmail.com>'
        #  msg['To'] = receiver

        to_send = f"{name} היקר{min1} ,\n \
    את{min1} {add_family} מוזמ{min2} להשתתף בתחרות דפיקות ראש בקיר העולמי, שתתקיים ב {city} לאחר מבחני סמסטר."

        message = f"""\
        Subject: הזמנה לתחרות ב
        To: {receiver}
        From: {smtplib}
        {to_send}"""
        print(message)
        server.sendmail(sender, receiver, message.encode("utf8"))
        # time.sleep(20)

print('end')
