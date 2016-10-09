# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

class QSBK:
    def __init__(self):
        self.pageIndex=1
        self.user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories=[]
        self.enable=False

    def getPage(self, pageIndex):
        try:
            url='http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getPageItems(self,pageIndex):
        pageContent=self.getPage(pageIndex)
        if not pageContent:
            print "页面加载失败"
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?<a.*?<h2>(.*?)'
                             '</h2>.*?<div.*?content.*?<span>(.*?)'
                             '</span>.*?</a>(.*?)'
                             '<div.*?stats".*?number">(.*?)'
                             '</i>', re.S)
        items = re.findall(pattern, pageContent)
        pageStories=[]
        for item in items:
            haveImg = re.search("img", item[2])
            if not haveImg:
                pageStories.append([item[0].strip(),item[1].strip(), item[3].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input=raw_input()
            self.loadPage()
            if input=="Q":
                self.enable=False
                return
            print u"第%d页\t发布人:%s\t发布内容:%s\t赞:%s\n" %(page,story[0],story[1],story[2])

    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories=self.stories[0]
                nowPage+=1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)


spider=QSBK()
spider.start()