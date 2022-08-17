# def get_sequence(num):
#     n = 0
#     one = 1
#     two = 2
#     while n < num:
#         yield two
#         tmp = one
#         one = two
#         two += tmp
#         n += 1
#
# if __name__ == "__main__":
#     number = int(input('请输入一位数字：'))
#     number_list = get_sequence(number)
#     for value in number_list:
#         print(value)

# 生成 斐波那契数列--除第一个和第二个数外，任意一个数都可由前两个数相加得到
# def fab(max):
#     n,a,b = 0,0,1
#     while n < max:
#         a,b = b, a+b
#         print(b)
#         n += 1
# if __name__ == '__main__':
#     fab(5)

# def fab(max):
#
#     n,a,b = 0,0,1
#     L = []
#     while n < max:
#         a,b = b,a+b
#         L.append(b)
#         n += 1
#     print(L)
#     return L
# if __name__ == '__main__':
#     fab(5)

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        a, b = b, a + b
        yield b
        n = n+1
if __name__ =="__main__":
    for i in fab(5):
        print(i)
