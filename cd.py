# matrix = []
# n = int(input())
# matrix = [[0]*n for i in range(n)]
#
# for i in range(0, n):
#     if i % 2 == 0:
#         matrix[i][0] = 'w'
#     else:
#         matrix[i][0] = 'b'
#
#
#
# for i in range(0, n):
#     if matrix[i][0] == 'w':
#         first = 'w'
#         second = 'b'
#     else:
#         first = 'b'
#         second = 'w'
#     for j in range(1, n):
#         if j % 2 ==0:
#             matrix[i][j] = first
#         else:
#             matrix[i][j] = second
# #
# print(matrix)
#
#  # ваш код
# value = int(input())
#
#
# lst = ["First try: ", "Second try: ", "Third try: "]
#
# for i in lst:
#     attempt = int(input(i))
#     if i == "Third try: " and attempt != value:
#         print("You lose!")
#         break
#
#     if attempt < value:
#         print("more")
#     elif attempt > value:
#         print("less")
#     else:
#         print("You win!")
#         break

#
#
# def bubble_sort(arr):
#     arr = [int(i) for i in arr.split()]
#     for j in range(len(arr)):
#         for i in range(len(arr)-1-j):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#     return arr

def inversion_count(arr):
    cnt = 0
    for j in range(len(arr)-1):
        for i in range(j+1, len(arr)):
            if arr[j] > arr[i]:

                cnt+=1
    return cnt


def cat_jumps(n):
    f = [0]*(n)
    f[0] = 0
    if n > 1 : f[1] = 1
    if n > 2:  f[2] = 2

    for i in range(3, n):
        f[i] = min(f[i-1], f[i-3]) + 1
    return f[n-1]
# ваш код
def is_bigger(a, b):
    a = a.split(":")
    b = b.split(":")
    if int(a[0]) > int(b[0]):
        return True
    elif int(a[0]) == int(b[0]) and int(a[1]) > int(b[1]):
        return True
    elif int(a[0]) == int(b[0]) and int(a[1]) == int(b[1]) and int(a[2]) >= int(b[2]):
        return True
    return False

def check_logs(log):
    if not log:
        return 0
    cnt = 1
    for j in range(len(log) - 1):
        if is_bigger(log[j], log[j+1]):
                cnt += 1
    return cnt


def del_left(l):
    new = []
    for i in range(1, len(l), 2):
        new.append(l[i])
    return new


def del_right(l):
    new = []
    for i in range(len(l)-2, -1, -2):
        new.append(l[i])
    new.reverse()
    return new

def last_number(n):
    lst = [i for i in range(1, n+1)]
    while True:
        lst = del_left(lst)

        if len(lst) == 1:
            return lst[0]

        lst = del_right(lst)

        if len(lst) == 1:
            return lst[0]


def who_took_the_car_key(message):
    new = ''
    for i in message:
        # print(int(i))
        new += chr(int(i, 2))
    return new

def squares_for_grains(grains):
    import math
    return int(math.log(grains, 2)) + 1

def stick_max_len(s1, s2):
    minn = min(s1,s1)
    maxx = max(s1, s2)
    if maxx / 3 > minn:
        return maxx / 3
    while True:
        if minn*2 <=maxx:
            return float(minn)
        else:
            minn -=1

a = ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110', '01100100', '01100101', '01110010']
# 'Alexander'
print(stick_max_len(5, 10))