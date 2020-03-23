from datetime import datetime
import time

def setAlarm(h, m):
    print("La alarma se activará a las {}:{}".format(h,m))
    resp = input("Es eso correcto?: ").lower()
    while resp != "si":
        h = int(input("Hora: "))
        m = int(input("Minutos: "))
        print("La alarma se activará a las {}:{}".format(h,m))
        resp = input("Es eso correcto?: ").lower()
    print("Perfecto. Buenas noches!")    
    return (h,m)

#Only this function is used by the main program.
def dt(alarm_h, alarm_m):
    #returns the number of seconds until the alarm is supposed to ring
    date = datetime.now()
    hour, minute, second = date.hour*3600, date.minute*60, date.second
    converted_time = hour+minute+second
    converted_alarm = (int(alarm_h)*3600)+(int(alarm_m)*60)
    return converted_alarm - converted_time
