import time
import subprocess


def pomRound():
    rounds = 0
    while rounds < 4:
        s = 25 * 60
        while s:
            mins = s // 60
            secs = s % 60

            countdown = "{:02d}:{:02d}".format(mins, secs)
            print(countdown, end = "\r")
            time.sleep(1)
            s -= 1
        print("Take A Break!")
        rounds += 1
        subprocess.call(["afplay", "sounds/game.wav"])

        b = 5 * 60
        while b:
            mins = b // 60
            secs = b % 60

            countdown = "{:02d}:{:02d}".format(mins, secs)
            print(countdown, end = "\r")
            time.sleep(1)
            b -= 1
        print("Back At It!")
        subprocess.call(["afplay", "sounds/complete.mp3"])

    print("Time For A Long Break!!!")
    longBreak()

def longBreak():
    t = 30 * 60
    while t:
        mins = t // 60
        secs = t % 60

        countdown = "{:02d}:{:02d}".format(mins, secs)
        print(countdown, end = "\r")
        time.sleep(1)
        t -=1
    print("You Got This!")
    subprocess.call(["afplay", "sounds/gong.mp3"])

pomRound()
