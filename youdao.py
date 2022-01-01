import requests
import hashlib
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/?keyfrom=fanyi-new.logo',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1816146931@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=1907025455.1891806; _ntes_nnid=e3c9ac1cdc08847e9b0bdd4813987082,1623662196713; _ga=GA1.2.364243456.1632298271; JSESSIONID=aaaINquBUVAxQ77d9Vq4x; ___rl__test__cookies=1640962259874'
}
UserAgent = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'

def main():
    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    scouce = input("输入需要翻译的句子：")
    # md = hashlib.md5()
    # md.update(UserAgent)
    # bv = md.hexdigest()
    ts = str(time.time()*1000)
    salt = ts+str(random.randint(0,10))
    # md.update(b"fanyideskweb"+scouce.encode("utf-8")+salt.encode("utf-8")+b"Y2FYu%TNSbMCxc3t2u^XT")
    # sign = md.hexdigest()
    sign_t = "fanyideskweb" + scouce + salt + "Y2FYu%TNSbMCxc3t2u^XT"
    sign = hashlib.md5(sign_t.encode('utf-8')).hexdigest()
    bv = hashlib.md5(UserAgent.encode('utf-8')).hexdigest()

    data = {
    'i': scouce,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'lts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
    }
    session = requests.session()
    resp = session.post(url,headers=headers,data=data)
    text = resp.json()["translateResult"][0][0]
    print(text)


if __name__ == "__main__":
    main()
   