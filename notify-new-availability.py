import requests, random, time

APPOINTMENT_DATE_SHOULD_BE_EARLIER_THAN = '2022-10-10'

def fetch_appointment_dates():
    url = "https://afspraak.utrecht.nl/qmaticwebbooking/rest/schedule/branches/6799b9a23eb23e3be8cff82b78da95d10503b9057b8cf48bc34c4bc47f0/dates;servicePublicId=1234949b1362b36017b7c84333270eb7a2c3a5a8106ebe9374914370ab8a6803;customSlotLength=10"

    response = requests.request("GET", url)
    return response

def check_appointment_date():
    response = fetch_appointment_dates()
    
    current_available_dates = response.json() # format is: [{'date': '2022-10-10'}, {'date': '2022-10-13'}]
    print(f"Received those availabilities: {current_available_dates}")
    
    for element in current_available_dates:
        date = element['date']
        if date < APPOINTMENT_DATE_SHOULD_BE_EARLIER_THAN:
            print(f"New early appointment available on date {date}")
            send_notification(f"New early appointment available on date {date}")
            return True
    return False

def send_notification(message):
    """
    Using pushover. Any notification app, email, sms, etc. can work instead of this.
    """
    post_url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token' : '', # TODO: replace with correct one
        'user': '', # TODO: replace with correct one
        'title': 'New appointment',
        'message': message,
    }
    requests.post(post_url, data=data)

def run_always():
    try:
        while True:
            appointment_found = False
            try:
                appointment_found = check_appointment_date()

            except KeyboardInterrupt as e:
                raise e
            except Exception as e:
                print("Caught exception...")
                print(e)
            
            if appointment_found:
                raise Exception("Appointment found, stopping program.")

            
            wait_time = random.randint(180, 300) # CAREFUL: do not fetch too often, otherwise you get blocked
            print('Waiting {} seconds...'.format(wait_time))
            for i in range(wait_time):
                time.sleep(1)
    except KeyboardInterrupt:
        print("Interruption by user. Stopping program.")

if __name__ == "__main__":
    run_always()
