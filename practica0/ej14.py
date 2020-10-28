# http://www.pressthered.com/adding_dates_and_times_in_python/
# https://realpython.com/python-time-module/

from datetime import timedelta

# https://docs.python.org/3/library/datetime.html

# A timedelta object represents a duration, the difference between two dates or times.

#class datetime.timedelta
# (days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

#All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.
#Only days, seconds and microseconds are stored internally. Arguments are converted to those units:
#A millisecond is converted to 1000 microseconds.
#A minute is converted to 60 seconds.
#An hour is converted to 3600 seconds.
#A week is converted to 7 days.

def suma_tiempos():
    a = input("Ingrese el primer tiempo en formato horas:minutos:segundos: \n")
    a = a.split(":")
    b = input("Ingrese el primer tiempo en formato horas:minutos:segundos: \n")
    b = b.split(":")
    delta1 = timedelta(hours=int(a[0]), minutes=int(a[1]), seconds=int(a[2]))
    delta2 = timedelta(hours=int(b[0]), minutes=int(b[1]), seconds=int(b[2]))
    delta = delta1+delta2
    return delta

print(suma_tiempos())

#implementar tuplas si quieres