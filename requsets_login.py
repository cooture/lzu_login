import requests

loginurl = 'http://jwk.lzu.edu.cn/academic/j_acegi_security_check'
homeurl = "http://jwk.lzu.edu.cn/academic/showHeader.do"

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

session = requests.Session()
##### 获取到验证码并保存
checkcodecontent = session.get("http://jwk.lzu.edu.cn/academic/getCaptcha.do", headers=headers)
with open('checkcode.gif', 'wb') as f:
    f.write(checkcodecontent.content)

payload = {
    'groupId': '',
    'j_username': input("username: "),
    'j_password': input("psswd: "),
    'j_captcha': input("cap_code: "),
    'button1': '%B5%C7%C2%BC'
}

# data = "groupId=&j_username=320160939901&j_password=wsrxb123&j_captcha=" + checkcode + "&button1=%B5%C7%C2%BC"
response_login = session.post(loginurl, headers=headers, data=payload)
response_home = session.post(homeurl, headers=headers)

if "用户名不能为空！" in response_home.text:
    print("login error!")
else:
    print('服务器端返回码： ', "登陆成功！", response_home.status_code, response_home.text)
