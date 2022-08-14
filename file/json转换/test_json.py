import json

# if __name__ == "__main__":
def test_obg():
    with open("json.txt","r",encoding="UTF-8") as f:
        read_conns = f.readlines()
        #print(read_conns)
        data = {}
        key_value = 0
        for i in read_conns:
            #print(i)
            i_info = i.split(",")
            i_json = {"name":i_info[0],"url":i_info[1].replace("\n","")}
            #print(i_json)
            data[key_value]=i_json
            key_value +=1
        print(data)
        # 内容写入文件中
        file = open("json.json","w",encoding="UTF-8")
        json.dump(data, file, ensure_ascii=False)

def test_name():
    connect = open("json.txt","r",encoding="UTF-8")
    connect_info = connect.readlines()
    name = "mamingyuan"
    for i in connect_info:
        if name in i:
            print("mamingyuan 在文件中")
        else:
            print("mamingyuan 不在文件中")