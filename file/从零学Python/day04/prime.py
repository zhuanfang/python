if __name__ == "__main__":
    number = int(input("其输入一个数字： "))
    numbr_center = int(number / 2)
    print(numbr_center)

    start = 2
    is_prime = True

    while start <= numbr_center:
        if number % start == 0:
            is_prime = False
            break
        start += 1
    if is_prime:
        print(str(number)+"是素数")
    else:
        print(str(number)+"不是素数")

def test_break():
    sum = 0
    for i in range(1,10):
        if i == 3:
            sum += 1
            continue
        sum += 1
        print(sum)

