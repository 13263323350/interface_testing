import requests

url = 'http://passport.zfwx.com/login?'
param = {'callback': 'success_jsonpCallback', 'username': 'testset13 ', 'password': '12312456', 'remember_me': 'on',
         '_': '1567490527563'}
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1;\
         Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"
          }
res = requests.get(url, param, headers=header)
print(res)
print(res.text)
# a=res.text.split('(')[1].split(",")[5]
# print(a[5])
a = res.text.split('(')  # 错误登录验证
print(a[1])
name = '"realname":"许富凯"'
name2 = '{"msg":"用户名或密码错误！","ret":"10000"})'

if res.text == 'success_jsonpCallback({"msg":"用户名或密码错误！","ret":"10000"})':
    if res.text.split('(')[1] == name2:
        print('ok', name2)

# elif res.text.split('(')[1].split(",")[2] == name:
#     print("ok",name)
else:
    print('no')
# print(type(a))
# print(a[1])
# print(type(a[1]))
# b=a[1].split(',')
# print(b)
# print(len(b))
# print(b[1])
