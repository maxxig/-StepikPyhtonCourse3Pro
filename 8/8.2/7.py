def print_digits(number):
    str_number = str(number)

    def rec(s, i=0):
        if i < len(str_number):
            print(str_number[i])
            rec(str_number, i + 1)
            #print(str_number[i])

    rec(str_number)


print_digits(2077)