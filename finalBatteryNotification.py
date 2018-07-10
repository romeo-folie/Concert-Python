from time import sleep
import notify2
from threading import Timer


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
