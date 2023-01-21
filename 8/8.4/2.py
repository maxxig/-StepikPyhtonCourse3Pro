def linear(lst):
    res = []
    def rec(element):
        result_lst = []
        if type(element) == int:
            result_lst.append(element)
        else:
            for e in element:
                result_lst.extend(rec(e))
        return result_lst
    return rec(lst)

my_list = [12, [13, [53, [632, [6, [2342341, [98, [3123], [2432], [4324]]]]]]]]

print(linear(my_list))