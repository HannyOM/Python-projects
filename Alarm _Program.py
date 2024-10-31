from datetime import datetime
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Get alarm time from user input
alarm = input("Enter the time for the alarm (HH:MM:SS AM/PM): ")

while True:
    # Get the current time in the same format as the alarm input
    now = datetime.now().strftime("%I:%M:%S %p")

    # Check if the current time matches the alarm time
    if alarm.upper() == now:
        print("Time To Wake Up")
        pygame.mixer.music.load(r"C:\Users\user\Downloads\PYTHON\LojayFalling.wav")
        pygame.mixer.music.play()

        # Wait for 20 seconds
        time.sleep(20)

        # Stop the music
        pygame.mixer.music.stop()
        break  # Exit loop after alarm plays
