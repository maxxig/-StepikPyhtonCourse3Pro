def func(number):
    print_num = 1
    def rec(step, print_num):
        if(step > 4):
            print(' ' * int(((number-step)/2)) + str(print_num) * step)
            rec(step - 4, print_num + 1)
            print(' ' * int(((number-step)/2)) + str(print_num) * step)
            # print(str(print_num) * step)
        elif (step == 4):
            print(' ' * int(((number - step) / 2)) + str(print_num) * step)
    rec(number, print_num)

func(16)