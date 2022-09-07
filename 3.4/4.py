from datetime import datetime, timedelta, time
input_time = datetime.strptime(input(), '%H:%M:%S')
delta = timedelta(hours=input_time.hour, minutes=input_time.minute, seconds=input_time.second)
print(int(delta.total_seconds()))

