def recursive_sum(data):
    def rec(data):
        res = 0
        if type(data) == int:
            res = res + data
        else:
            for d in data:
                res = res + rec(d)
        return res
    return rec(data)

my_list = [[[[-11, 99], -7], [35, [-50, -59, 3]], [-63, -89], 36, [0]]]

print(recursive_sum(my_list))