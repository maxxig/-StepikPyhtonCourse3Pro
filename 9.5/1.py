def power(degree):
    def power_internal(val):
        return pow(val, degree)
    return power_internal


result = power(2)(-2948492393)
print(result)