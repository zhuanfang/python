# 元组：位置固定不可编辑，只能查询 ，len()

def test_tuple():
    tuple_data = ("1","heihei","lala")
    print(tuple_data)

    print(tuple_data[0])
    print(tuple_data[-1])

    tuple_len = len(tuple_data)
    print(tuple_len)

    # 定义一个元素值的元组，必须加一个逗号
    tuple_best = ("python",)
    print(tuple_best)