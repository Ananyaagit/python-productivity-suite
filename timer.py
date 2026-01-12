import time

def timer_menu():
    seconds = int(input("Enter time in seconds: "))
    while seconds:
        print("Time left:", seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
