import random
import threading
import pandas as pd
import smtplib
import time
from email.message import Message
from email.header import Header

filename_utf8 = 'filename_utf8.csv'

df = pd.read_csv(filename_utf8, encoding="utf-8")

# for d in df.iterrows():
#    name = d[1].Name
#    matsav_mishpahti = d[1]['Family status']
#    gender = d[1].Gender
#    city = d[1].City
#    print(d[1].Email)

sender = "Private Person <doe@smtp.mailtrap.io>"
count_row = df.shape[0]  # gives number of row count
thread_range = range(count_row)
thread_pool_dict = {rng: 0 for rng in range(count_row)}


def send_single_mail(msg_id):
    time.sleep(random.randint(0, 80))
    global thread_pool_dict
    global df
    print(f'Running {msg_id} thread')
    try:
        if thread_pool_dict[msg_id] < -3:
            return

        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("041aa6eae34402", "cb9ed2edf5ffb2")
            row = df.iloc[msg_id, :]
            #row = row[1]
            name = row.Name
            matsav_mishpahti = row['Family status']
            gender = row.Gender
            min1 = 'ה'
            min2 = 'ן'
            if gender == 'f':
                min1 = ''
                min2 = 'נת'
            city = row.City
            receiver = row.Email

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
            msg = Message()
            msg['Subject'] = Header('הזמנה לתחרות ב' + city, 'utf-8')
            msg['From'] = 'My Test <test@gmail.com>'
            msg['To'] = receiver
            to_send = f"{name} היקר{min1} ,\n \
    את{min1} {add_family} מוזמ{min2} להשתתף בתחרות דפיקות ראש בקיר העולמי, שתתקיים ב {city} לאחר מבחני סמסטר."

            message = f"""\
            Subject: Hi Mailtrap
            To: {receiver}
            From: {sender}
            {to_send}"""

            server.sendmail(sender, receiver, message.encode("utf8"))
            print("SENT:" + message)
            thread_pool_dict[msg_id] = 1
            print("End of thread")

    except smtplib.SMTPDataError as e:
        thread_pool_dict[msg_id] = thread_pool_dict[msg_id] - 1
        print(f"Problem with {msg_id} thread, {e}")
        if thread_pool_dict[msg_id] > -4:
            time.sleep(random.randint(1, 60))
            send_single_mail(msg_id)
            print(f"Fed up with {msg_id} thread, quitting")

    except Exception as e:
        print(f"General exception from {msg_id} thread, {e}, quitting")

    return None


if __name__ == "__main__":
    # creating thread
    for thread_idx in thread_range:
        t1 = threading.Thread(target=send_single_mail, args=(thread_idx,))
        t1.start()

    print('End of main thread')
