from datetime import datetime
from pygame import mixer
import time

# localtime = datetime.strftime(datetime.now(), "%H:%M:%S")
# print(localtime)
# print(type(localtime))
def iterable_time(time):
    time = datetime.now().strftime("%H:%M:%S")
    time_list = list(filter(lambda x: x.isdigit(), time))
    index = 0
    int_time_list = []
    temp_time_list=["a","b","c"]
    for i in range(0,6,2):
        temp_time_list[index]=time_list[i]+time_list[i+1]
        # int(time_list[index])
        int_time_list.append(int(temp_time_list[index]))
        index += 1
    return int_time_list

def current_time():
    return datetime.now().strftime("%H:%M:%S")

def print_time(tyam):
    return f"{tyam[0]} hour {tyam[1]} minute {tyam[2]} second"

def water():
    mixer.init()
    mixer.music.load("./water.mp3")
    mixer.music.play()
    print("Water Drinking Time. Drink 0.475 litres of water.\nEnter 'drank' to stop the alarm.")
    while True:
        a = input()
        while(a.lower() != "drank"):
            a = input()
        if a == "drank":
            mixer.music.stop()
            break

# print(iterable_time(current_time()))
def eyes():
    mixer.init()
    mixer.music.load("./eyes.mp3")
    mixer.music.play()
    print("Eye Exercise Time. Enter 'eyesdone' to stop the alarm.")
    while True:
        a = input()
        while(a.lower() != "eyesdone"):
            a = input()
        if a == "eyesdone":
            mixer.music.stop()
            break
            
def physical():
    mixer.init()
    mixer.music.load("./physical.mp3")
    mixer.music.play()
    print("Physical Exercise Time. Enter 'physicaldone' to stop the alarm.")
    while True:
        a = input()
        while(a.lower() != "physicaldone"):
            a = input()
        if a == "physicaldone":
            mixer.music.stop()
            break


def phy_min_next(a):
    a[1] = phy_start_time[1] + 45
    if a[1] >= 60:
        return a[1]%60
    else :
        return a[1]
def eye_min_next(a):
    a[1] = eye_start_time[1] + 30
    if a[1] >= 60:
        return a[1]%60
    else :
        return a[1]


water_per_day = 3.5  #3.5 liters of water to be consumed in a day
# water_interval time is 1 hour
water_drank = 0     
eye_start_time = phy_start_time = iterable_time(current_time()) 
# eye=[1,2,3]
# print(eye_min_next(eye))  
print(f"Started program at:\t{print_time(phy_start_time)}")
if __name__ == "__main__":
    while True:
        time_now = iterable_time(current_time())
        print(f"Current time is:\t{print_time(time_now)}")
        if (time_now[0] >= 9 and (time_now[0] <= 18 and time_now[1] <= 59)):
            print(time_now)
            # if (time_now[0] >= 0 and time_now[0] <= 0):
            if time_now[1] == 0 and time_now[2] == 0:
                water()
                water_drank+=0.4375
                print("/n Your drinking time will refresh in (1 hour minus time you spent drinking water).")
            if time_now[1] == eye_min_next(time_now)and time_now[2] == 0:
            # if time_now[1] == 20 and time_now[2] == 0:
                eye_start_time[1]+=30
                eyes()
                print("/n Your eye exercise time will refresh in (30 minutes minus time you spent doing eye exercise).")
            if time_now[1] == phy_min_next(time_now) and time_now[2] == 0:
            # if time_now[1]==22 and time_now[2]==0:
                print("Physical exercise time")
                phy_start_time[1]+=45
                physical()
                print("/n Your physical exercise time will refresh in (45 minutes minus time you spent doing physical exercise).")

            else:
                time.sleep(1)
        else:
            print("You are not supposed to be working at this time 🚫. Please take a break.💔")
            print("You drank ",water_drank," liters of water 💦 during this program execution.")
            break