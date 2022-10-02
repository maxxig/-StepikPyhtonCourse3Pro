import sys
from datetime import datetime, timedelta

arr = [ datetime.strptime(line.rstrip(), '%d.%m.%Y') for line in sys.stdin]

ASC = all(arr[i] < arr[i+1] for i in range(len(arr)-1))
DESC = all(arr[i] > arr[i+1] for i in range(len(arr)-1))

if ASC == True:
    print('ASC')
elif DESC == True:
    print('DESC')
else:
    print('MIX')

