#encoding:UTF-8
#online reg: https://regex101.com/
import urllib
import urllib2
import cookielib
import re
import win32com


def open_url():
    values = {}
    values['username'] = "cjkx38"
    values['password'] = "Newpassword48"
    data = urllib2.urlencode(values)
    binary_data = data.encode(encoding='UTF8')
    url = "http://sds12.comm.mot.com/LicensingTools/llt/index.cfm?operator=CreateEntitlement"
    request = urllib2.Request(url,binary_data)
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError as e:
        print(e.reason)
    print(response.read())

def test():
    req = urllib2.Request('http://blog.csdn.net/cqcre')
    try:
        urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        else:
            print('OK')

def test_cookie():
       # 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.cookiejar.CookieJar()
    # 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name = ' + item.name)
        print('Value = ' + item.value)

    filename = "D:\cookie.txt"
    cookie1=cookielib.cookiejar.MozillaCookieJar(filename)
    handler1=urllib.request.HTTPCookieProcessor(cookie1)
    opener=urllib.request.build_opener(handler1)
    response= opener.open('http://www.baidu.com')
    cookie1.save(ignore_discard=True, ignore_expires=True)  # 创建MozillaCookieJar实例对象

def test_readfromcookie():
    cookie = cookielib.cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load("D:\cookie.txt", ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib.request.Request("http://www.baidu.com")
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print(response.read())

def re_model():
    # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
    pattern = re.compile(r'hello')

    # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
    result1 = re.search(pattern, 'yjhello')
    result2 = re.match(pattern, 'helloo CQC!')
    result3 = re.match(pattern, 'helo CQC!')
    result4 = re.match(pattern, 'hello CQC!')

    # 如果1匹配成功
    if result1:
        # 使用Match获得分组信息
        print(result1.group())
    else:
        print('1匹配失败！')

    # 如果2匹配成功
    if result2:
        # 使用Match获得分组信息
        print(result2.group())
    else:
        print('2匹配失败！')

        # 如果3匹配成功
    if result3:
        # 使用Match获得分组信息
        print(result3.group())
    else:
        print('3匹配失败！')

        # 如果4匹配成功
    if result4:
        # 使用Match获得分组信息
        print(result4.group())
    else:
        print('4匹配失败！')

def test_findall():
    pattern=re.compile(r'\d+')
    print(re.split(pattern,'one11two2three3four4'))
    print(re.findall(pattern, 'one11two2three3four4'))
    for m in re.finditer(pattern,'one11two2three3four4'):
        print(m.group())

    pattern1 = re.compile(r'(\w+) (\w+)')
    s = 'i say, hello world!'
    print(re.sub(pattern1, r'\2 \1', s))

    def func(m):
        return m.group(1).title() + ' ' + m.group(2).title()
    print(re.sub(pattern1, func, s))

    inputStr = "hello crifan, hello crifan";
    replacedStr = re.sub(r"(\w+) crifan, \1 crifan", "crifanli", inputStr);
    print("replacedStr=", replacedStr )# crifanli

    inputStr1 = "hello crifan, nihao crifan";
    replacedStr1 = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr1);
    print("replacedSt1r=", replacedStr1)  # crifan

def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456 nihao 789"

    def _add111(matched):
        intStr = matched.group("number")  # 123
        intValue = int(intStr)
        addedValue = intValue + 111  # 234
        addedValueStr = str(addedValue)
        return addedValueStr

    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr)
    print("replacedStr=", replacedStr)          # hello 234 world 567 nihao 789


if __name__=='__main__':
    pythonReSubDemo()

