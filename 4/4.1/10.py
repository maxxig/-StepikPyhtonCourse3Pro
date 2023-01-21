import sys

arr = [int(line.rstrip()) for line in sys.stdin]
a_p_k, a_p_g = arr[1] - arr[0], arr[1]/arr[0]

a_p_k_result = all(arr[i+1] == (arr[i] + a_p_k) for i in range(len(arr)-1))
a_p_g_result = all(arr[i+1] == (arr[i] * a_p_g) for i in range(len(arr)-1))

if a_p_k_result == True:
    print('Арифметическая прогрессия')
elif a_p_g_result == True:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')