
def test_str():
    str_data = "这是个字符串String"
    print(str_data)

    # encode --编码，decode --解码
    str_encode = str_data.encode("UTF-8")
    print(str_encode)

    str_decode = str_encode.decode("utf-8")
    print(str_decode)

    str_len = len(str_data)
    print(str_len)

    #格式化字符串
    str_format = "这是字符串格式化： %s" % str_data
    print(str_format)

    #参数格式化
    # #f“{参数}”
    # "%s %d %f" %("计算","6","6.123456")
    # "{}".format(参数)
    int_value = 667
    int_format1 = "这是整数格式化： %d" % int_value
    int_format2 = f"这是整数格式化: {int_value}"
    int_format3 = "这是整数格式化: {}".format(int_value)
    print(int_format1)
    print(int_format2)
    print(int_format3)

    # 综合使用
    format_value = "综合格式化：%s %d %f 的值" %("计算",66,66.123456)
    print(format_value)