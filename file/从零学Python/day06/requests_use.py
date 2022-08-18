import requests


def test_request():
    url = 'http://httpbin.org/get'
    payload = {'key1':'value1','key2':['value2', 'value3']}
    r = requests.get(url,params = payload)
    print(r)

    with open('','r',encoding='utf-8') as f:
        file = f.read()

def test_request1():
    id = 'wwdae6409305b8bd0c'
    select = 'yfVfCz4aehQ1etcO9Rqh9lx9GPpdcjute5Zyi9w8ZO0'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    header ={'corpid':'wwdae6409305b8bd0c',
              'corpsecret':'yfVfCz4aehQ1etcO9Rqh9lx9GPpdcjute5Zyi9w8ZO0'}
    #r =requests.get(url,headers=headers)

    r = requests.get(url,params=header)
    print(r.json())
    token = r.json()['access_token']
    print(token)
    with open('token.yaml','w',encoding='UTF-8') as f:
        f.write(token)





