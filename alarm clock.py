import datetime
import time
import playsound

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up!")
            playsound.playsound("oversimplified-alarm-clock-113180.mp3")  # Replace "sound.mp3" with your preferred alarm sound file
            break
        else:
            print("Current Time:", current_time)
            time.sleep(1)

set_alarm()