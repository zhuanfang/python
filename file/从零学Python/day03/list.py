
def test_list():
    list_data = ["mingren","chutian","zuozhu","xiaoying","1","2"]
    list_len = len(list_data)
    print(list_len)

    print(list_data[0])
    print(list_data[-3])

    list_data.append("end")
    print(list_data)

    list_data.insert(3,"kakaxi")
    print(list_data)

    list_data.pop()
    print(list_data)

    list_data.pop(1)
    print(list_data)

    list_data[1] = "linlin"
    print(list_data)
