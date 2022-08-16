
#加、减、乘、除计算

# def test_cals():
if __name__=="__main__":
    operate_type = input("请选择运算类型：1加法，2减法，3乘法，4除法：")
    while int(operate_type) not in (1,2,3,4):
        print("输入类型错误，请输入1到4的数字")
        operate_type = input("请重新输入1到4：")

    num_one = int(input("请输入第1个数字： "))
    num_two = int(input("请输入第2个数字： "))
    if operate_type == "1":
        result =num_one+num_two
        print("计算结果为 "+str(result))
    elif operate_type == "2":
        result = num_one-num_two
        print("计算结果为 "+str(result))
    elif operate_type == "3":
        result = num_one*num_two
        print("计算结果为 "+str(result))
    elif operate_type == "4":
        if num_two == 0:
            print("被除数不能为0")
        else:
            result = num_one/num_two
            print("计算结果为 "+str(result))
    else:
        print("算法类型错误")




