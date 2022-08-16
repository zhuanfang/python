
if __name__ == "__main__":
    num_one = input("请输入第一位数： ")
    num_two = input("请输入第二位数： ")
    sum_value = float(num_one)+float(num_two)
    print("加法运算: " + num_one + '+' + num_two + '=' + str(sum_value))

    diff_value = float(num_one) - float(num_two)
    print("减法运算： " + num_one + '-' + num_two + '=' + str(diff_value))

    mul_value = float(num_one)*float(num_two)
    print("乘法运算：" + num_one + '*' + num_two + '=' + str(mul_value))

    if num_two == 0:
        print("被除数不能等于0")
    else:
        div_value = float(num_one) / float(num_two)
        print('除法运算：' + num_one + '/' + num_two + '=' + str(div_value))

    after_value = float(num_one)//float(num_two)
    print("相除取整数：" + num_one + '//' + num_two + '=' + str(after_value))

    left_value = float(num_one)%float(num_two)
    print("相除取余数：" + num_one + '%' + num_two + '=' + str(left_value))

    # 计算圆的周长
    pai = 3.14
    circle_length = input("请输入圆的直径： ")
    length = 2*pai*(int(circle_length)/2)
    print("圆的周长：" + str(length))

    # 计算圆的面积
    area = pai*(int(circle_length)/2)**2
    print("圆的面积：" + str( area))

