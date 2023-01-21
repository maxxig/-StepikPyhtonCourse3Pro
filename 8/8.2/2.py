def func(s, f=100):
    if(s <= f):
        print(s)
        func(s+1)
func(1)