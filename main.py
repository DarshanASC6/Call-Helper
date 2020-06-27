import random, json, time, playsound

# Import JSON compatability into the file
with open('data.json', encoding="utf8") as f:
    data = json.load(f)

dial = 30
# 30 seconds

ready = 3
# 3 seconds

calltime = 120
# 2 minutes

r = random.randint(0,1)

subject = random.choice(data['Darshan'])

method = (random.choice(data['contact-methods']) + "ing")

tips = random.choices(data['contact-starters'])

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    playsound.playsound("Go.mp3")

def start():
    print("Get ready to start", method, subject)

    countdown(int(dial))
    # Start dialing their number stoopid

    print("Ready?")

    countdown(int(ready))

    print("Go!")

    countdown(int(calltime))
    # Start talking

    if r:
        print("Try starting out with these:")
        for i in range(ready):
            tips = random.choices(data['contact-starters'])
            print(tips)
    else:
        print("You got this!")

start()
