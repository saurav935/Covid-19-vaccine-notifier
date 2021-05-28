
import requests
import time
from datetime import datetime, timedelta

import json

print("Welcome to Covid-19 vaccine notifier !!")

age = 52
pin_codes = ["462003"]
print_flag = "Y"
num_days = 2

today_date = datetime.today()


list_format = [today_date + timedelta(days=i) for i in range(num_days)]

actual_dates = [i.strftime("%d-%m-%y") for i in list_format]


while True:
    counter = 0

    for pin_code in pin_codes:
        for date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin_code, date)

            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

            result = requests.get(URL, headers = header)


            if result.ok:
                response_json = result.json()
                if response_json['centers']:
                    if print_flag.lower() == 'y':
                        for center in response_json["centers"]:
                            for session in center['sessions']:
                                if session['min_age_limit'] <= age and session['available_capacity'] > 0:
                                    print('Pincode: ' + pin_code)
                                    print("Available on: {}".format(date))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])

                                    if (session["vaccine"] != ''):
                                        print("\t Vaccine type: ", session["vaccine"])
                                    print("\n")
                                    counter = counter + 1


            else:
                print("No Response received !")


    if counter == 0:
        print("No vaccination slot is available!")
    else:
        print("Search Completed!")

    dt = datetime.now() + timedelta(minutes = 3)

    while datetime.now() < dt:
        time.sleep(1)
        
