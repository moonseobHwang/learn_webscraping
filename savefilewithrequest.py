import requests

url = 'http://blog.naver.com/otter35'
url = 'https://www.coupang.com/'
# https://www.whatismybrowser.com/detect/what-is-my-user-agent
header = {'User-Agent': ''}
# Try coutinue 3 times without headers-> Timeout
res = requests.get(url=url, headers=header)
print(type(res), res)
# <class 'requests.models.Response'> <Response [200]>

print(res.status_code)
if(res.status_code == 200):
    with open('datas/response01.html', 'w') as fp:
        fp.write(res.text)