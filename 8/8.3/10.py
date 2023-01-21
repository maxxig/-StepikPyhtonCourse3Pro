def is_palindrome(string):
    def rec(step = 0):
        if step == len(string):
            return True
        elif string[step] != string[-step-1]:
            return False
        else:
            return rec(step+1)
    return rec()

print(is_palindrome('1'))