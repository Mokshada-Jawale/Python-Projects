# Countdown Timer
import time

def get_time():
    t = input('Enter the Time in seconds: ')
    return t

def countdown(t):
    while t:
        mins, secs = divmod(t,60) #The divmod() function is used to convert the remaining time into minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timer Completed!')

if __name__ == '__main__':
    t = get_time()
    countdown(int(t))
