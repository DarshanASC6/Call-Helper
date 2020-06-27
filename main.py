import random, json, time

# Import JSON compatability into the file
with open('data.json') as f:
    data = json.load(f)


dial = 30
# 30 seconds

ready = 3
# 3 seconds

calltime = 120
# 2 minutes

subject = random.choice(data['Darshan'])

method = (random.choice(data['contact methods']) + "ing")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')

def start():
    print("Start", method, subject)

    countdown(int(dial))
    # Start dialing their number stoopid

    print("Ready?")

    countdown(int(ready))

    print("Go!?")

    countdown(int(calltime))
    # Start talking

start()
