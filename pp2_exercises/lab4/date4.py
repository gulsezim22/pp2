from datetime import datetime, time
def date_difference(dt1,dt2):
    timedelta=dt2-dt1
    return timedelta.days*86400+timedelta.seconds