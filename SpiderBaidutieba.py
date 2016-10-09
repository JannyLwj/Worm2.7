__author__ = 'Janny'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseUrl=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)

    def getPage(self, pageNum):
        try:
            url=self.baseUrl+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败，错误原因：", e.reason

    def getTitle(self):
        pageContent=self.getPage(1)
        pattern=re.compile('<h3.*?core_title_text.*?>(.*?)</h3>', re.S)
        result=re.search(pattern,pageContent)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self):
        pageContent = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern, pageContent)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

    def getContent(self):
        pageContent = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result = re.search(pattern, pageContent)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

baseURL= 'http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL)
bdtb.getPage(1)



