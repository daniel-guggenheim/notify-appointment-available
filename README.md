# Notify Appointment Slot Available
Script to check if an appointment slot is available, and if so, send a push notification to your phone.

1. Change the URL to the correct one. For that, use chrome network tab feature: `right-click` on the page -> `inspect` -> `network` tab. And check the exact call that is made when fetching the appointment page.

2. Update the script to use the proper notification method that is convenient to you.

3. Change the constant: `APPOINTMENT_DATE_SHOULD_BE_EARLIER_THAN`


3. Run with

```
python notify-new-availability.py
```
