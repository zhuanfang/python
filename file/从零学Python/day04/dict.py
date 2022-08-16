
def test_dict():
    dict_none = {}

    dict_all = {'math':96,'english':97,'chinese':98}
    print(dict_all)

    #使用dict()创建字典
    tuple_math = ('math','96')
    tuple_english = ('english','97')
    tuple_chinese = ('chinese','99')
    dict_a = dict([tuple_math,tuple_english,tuple_chinese])
    print(dict_a)

    # 使用zip() 合并两个列表分别作为字典的key 与 value
    list_key = ['math','english','chinese']
    list_value = ['91','92','93']
    score = dict(zip(list_key,list_value))
    print(score)

    # 读取字典的 values/keys/items(组成了一个元组 返回一个列表)
    print(dict_all.values())
    print(dict_all.keys())
    print(dict_all.items())

    # 使用get() 获取key值对应的value
    math_value = dict_all.get("math")
    print(math_value)

    # in / mot in 判断key在字典中是否存在
    print('math' in dict_all)
    print('heihei' not in dict_all)

    # pop() 删除一个key 对应的元素，key存在，则返回对应的数值
    pop_result = dict_all.pop('math','96')
    print(pop_result)

    # 使用 update() 更新字典，也就是追加元素
    dict_all.update({"history":'99'})
    print(dict_all)

    # 使用 fromkeys() 创建一个新的字典，key来自序列，value来自自定义
    dict_new = dict_none.fromkeys([11,22,33,44],100)
    print(dict_new)