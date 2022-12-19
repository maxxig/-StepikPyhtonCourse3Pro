def func(number):
    def rec(step = number):
        if step <= 0:
            print(step)
            return step
        else:
            print(step)
            rec(step-5)
            print(step)
    rec()

func(int(input()))