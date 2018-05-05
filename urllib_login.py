import http.cookiejar
import urllib.request

from bs4 import BeautifulSoup

loginurl = 'http://jwk.lzu.edu.cn/academic/j_acegi_security_check'
homeurl = "http://jwk.lzu.edu.cn/academic/showHeader.do"
picurl = "http://jwk.lzu.edu.cn/academic/getCaptcha.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Host": 'jwk.lzu.edu.cn',
    "Accept-Language": 'zh-cn',
    "Content-Type": 'application/x-www-form-urlencoded',
    'Referer': 'http://jwk.lzu.edu.cn/academic/index.jsp',
    "Upgrade-Insecure-Requests": "1",
    "Origin": 'http://jwk.lzu.edu.cn',
    "DNT": '1',
    "Connection": 'keep-alive'
}

# 构造jar自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 验证码
req_pic = urllib.request.Request(picurl, headers=headers)
pic = opener.open(req_pic)
with open('checkcode.gif', 'wb') as f:
    f.write(pic.read())

# 构造data
payload = {
    'groupId': '',
    'j_username': input("username: "),
    'j_password': input("psswd: "),
    'j_captcha': input("cap_code"),
    'button1': '%B5%C7%C2%BC'
}
data = urllib.parse.urlencode(payload).encode(encoding='utf-8')

# 登陆
req_log = urllib.request.Request(loginurl, data, headers)
res_log = opener.open(req_log)
req_home = urllib.request.Request(homeurl, headers=headers)
res_home = opener.open(req_home)
text = BeautifulSoup(res_home.read(), "html.parser")
# if "用户名不能为空！" in text.string:
#     print("login error!")
if text.find_all(alt="点击刷新验证码"):
    print("login error!")
else:
    print("res ：", text)
