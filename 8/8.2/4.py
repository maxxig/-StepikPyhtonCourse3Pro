import sys

data = [int(i.strip()) for i in sys.stdin]
#data =[1,2,3,4]
def func(numbers):
    def rec(step):
        if step < len(numbers):
            rec(step+1)
            print(numbers[step])
    rec(0)

func(data)