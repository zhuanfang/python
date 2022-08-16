
# 叠加计算
def test_add():
    sum = 0
    for i in range(1,11):
        sum += 2
        print(sum)
    print(sum)

# for 循环计算 100内的奇数/偶数之和
def test_sum():
    sum = 0
    for i in range(1,101):
        #if i%2 == 0: # 计算1-100 内的所有偶数 相加
        if i%2 != 0:  # 计算1-100 内的所有奇数 相加
            sum += i
            #print(sum)
    print(sum)


def test_sum1():
    sum1 = 0
    n = 0
    while n <=100:
        if n % 2 == 0:
            sum1 += n
        n += 1
    print(sum1)


