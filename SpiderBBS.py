# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import time

class BBS:
    def __init__(self):
        self.user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        BBSstories=[]

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

    def getBBScontent(self, BBScontent):
        pattern = re.compile('<tr valign="bottom".*?>.*?</tr>', re.S)
        items = re.findall(pattern, BBScontent)
        for item in items:
            if "Label1" in item and  "Label2" in item and  "Label6" in item:
                BBStitle=re.search('(?<=Label1\">).+(?=</span>)', item)
                BBSresponse=re.search('(?<=Label2\">).+(?=</span>)', item)
                BBStime = re.search('(?<=Label7\">).+(?=</span>)', item)
                print BBStitle.group()
                print BBSresponse.group()
                print BBStime.group()
                #存入数据库

    def start(self):
        content=self.getPage()
        self.getBBScontent(content)


spider=BBS()
spider.start()