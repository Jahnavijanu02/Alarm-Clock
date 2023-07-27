# Alarm Clock
This is a simple Python script that allows you to set an alarm in Visual Studio Code. The script continuously checks the current time and plays an alarm sound when the specified alarm time is reached.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3: You can download Python from the official website (https://www.python.org/downloads/) and install it following the instructions.

## Installation

1. Clone the repository or download the Python script (alarm_clock.py) to your local machine.

2. Open Visual Studio Code.

3. In Visual Studio Code, open the folder containing the alarm_clock.py script.

4. Open the integrated terminal in Visual Studio Code by selecting `View` > `Terminal` from the menu.

5. Install the required dependency for playing the alarm sound using the following command:

```
pip install playsound
```

## Usage

1. In the integrated terminal, navigate to the folder where the alarm_clock.py script is located.

2. To run the script, execute the following command in the terminal:

```
python alarm_clock.py
```

3. The script will prompt you to enter the alarm time in the format "HH:MM" (hours and minutes). For example, to set the alarm for 8:30 AM, you should enter "08:30", and for 2:45 PM, you should enter "14:45".

4. Once you've entered the alarm time, the script will continuously check the current time and compare it with the specified alarm time.

5. When the alarm time is reached, the script will display "Wake up!" and play the alarm sound. Make sure you have a sound file named "oversimplified-alarm-clock-113180.mp3" in the same directory as the Python script, or replace it with your preferred alarm sound file by updating the `playsound.playsound()` function call.

6. To stop the alarm, press `Ctrl + C` in the terminal.

## Notes

- The alarm uses the 24-hour format (HH:MM) for setting the time. Please ensure you enter the correct time format when prompted.

- Ensure that your computer's speakers are on and the volume is turned up to hear the alarm sound.

- If you encounter any issues or have suggestions for improvements, feel free to open an issue in the repository.

## Credits

This script uses the `playsound` library to play the alarm sound. The library can be found on PyPI: https://pypi.org/project/playsound/

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
