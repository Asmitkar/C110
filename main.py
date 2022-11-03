import time
counter = int(input('enter the time in number of seconds '))

def countdowntimer(counter):
    while (counter>0):
        miniutes = int(counter/60)
        seconds = int(counter%60)
        timer = f'{miniutes}: {seconds}'
        print(timer)
        time.sleep(1)
        counter-= 1
    print('time up!!')

countdowntimer(counter)