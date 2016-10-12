# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

class BBS:
    def __init__(self):
        self.user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories=[]
        self.enable=False

    def getPage(self):
        try:
            url='http://cdweb.ap.mot-solutions.com/sec/BulletinBoard/index.aspx'
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

    def getPageItems(self):
        pageContent=self.getPage()
        if not pageContent:
            print "页面加载失败"
            return None
        pattern = re.compile('<tr.*? valign=bottom.*?>.*?<td.*?style.*?<a.*?<span.*?>(.*?)'
                             '</span>.*?<td.*?</td>.*?<td.*?>.*?<span.*?>(.*?)'
                             '</span>.*?<td.*?>.*?<span.*?>(.*?)'
                             '</span>.*?<td.*?>.*?<span.*?>(.*?)'
                             '</span>.*?<td.*?>.*?<span.*?>(.*?)'
                             '</span>.*?<td.*?>.*?<span.*?>(.*?)'
                             '</span>',re.S)
        items = re.findall(pattern, pageContent)
        pageStories=[]
        for item in items:
            print item[0]
            print item[1]
            print item[2]
            print item[3]
            print item[4]
            print item[5]
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip(),item[4].strip(),item[5].strip()])
        return pageStories

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItems()
                if pageStories:
                    self.stories.append(pageStories)


    def getOneStory(self, pageStories):
        for story in pageStories:
            input=raw_input()
            self.loadPage()
            if input=="Q":
                self.enable=False
                return
            print u"贴主题:%s\t回复人数:%s\t浏览人数:%s\t发帖人:%s\t发布时间:%s\t更新时间:%s\n" %(story[0],story[1],story[2],story[3],story[4],story[5])

    def start(self):
        print u"正在BBS帖子，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        while self.enable:
            if len(self.stories) > 0:
                pageStories=self.stories[0]
                del self.stories[0]
                self.getOneStory(pageStories)

spider=BBS()
spider.start()