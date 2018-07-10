from time import sleep
import notify2
from threading import Timer

"""
Someone told me that I could make my battery last longer if I charged it to a maximum of 80%
so I wrote this little baby to make noise in my ears everytime my battery hits 80% so I can take it off charge
"""

file1 = "/sys/class/power_supply/BAT0/status"

file2 = "/sys/class/power_supply/BAT0/capacity"


def batteryNotifier():
    with open(file1) as status:
        for line in status:
            if "Charging" in line:
                with open(file2) as capacity:
                    for line in capacity:
                        data = int(line)
                        if data >= 80:
                            notify2.init('Battery Monitor')
                            notify2.Notification("80% Reached\nPlease Unplug Charger").show()
                            print('\a')
                            sleep(5)
    timer = Timer(10.0, batteryNotifier)
    timer.start()

if __name__ == '__main__':
        batteryNotifier()
