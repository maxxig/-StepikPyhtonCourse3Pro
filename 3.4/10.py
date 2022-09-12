from datetime import datetime, timedelta

st_time = datetime.strptime(input(), '%H:%M')
fin_time = datetime.strptime(input(), '%H:%M')

while((st_time + timedelta(minutes=45)) <= fin_time):
    print(f'{datetime.strftime(st_time, "%H:%M")} - {(datetime.strftime(st_time + timedelta(minutes=45), "%H:%M"))}')
    st_time += timedelta(minutes=55)