from datetime import date, timedelta
def yestoto():
    for i in range(-1,2):
        dt=date.today()+timedelta(i)
        print(dt)
yestoto()