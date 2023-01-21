
def triangle(number):
    def rec(step):
        if step>0:
            #print('*' * step)
            rec(step-1)
            print('*' * step)
    rec(number)

triangle(10)