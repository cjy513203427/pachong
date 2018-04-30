# coding=utf-8
import urllib2
import film
import re
opener = urllib2.build_opener()#构建一个handler对象
def search():
    req = urllib2.Request('http://s.ygdy8.com/plus/so.php')
    #so.php请求参数将中文进行了Url.encode()，所以需要将中文encode('gb2312')处理
    req.add_data('kwtype=0&searchtype=title&keyword=%s' %(film.filmName).decode("utf-8").encode('gb2312'))
    html = opener.open(req).read().decode('gb2312')
    reg = r'/html/tv/oumeitv/[0-9]{8}/[0-9a-zA-Z.]{9,10}'
    return re.findall(reg,html)
search()
#/html/tv/oumeitv/20140930/46270.html
#/html/tv/oumeitv/20151007/49245.html
def openSearchResult():
    list = search()
    req = urllib2.Request('http://www.ygdy8.com'+list[0])
    html = opener.open(req).read().decode('gb2312','ignore')
    reg = u'ftp://[a-z0-9]+:[a-z0-9]+@[a-z0-9]+.[a-z]{1,8}.[a-z]{3}:[\d]{4}/[\u4e00-\u9fa5]{0,10}[\W]*\[阳光电影www.ygdy8.com\][\u4e00-\u9fa5]*[\d]+[\u4e00-\u9fa5]\[[\u4e00-\u9fa5]+\].rmvb'
    return re.findall(reg,html)
openSearchResult()
#ftp://dygod1:dygod1@y068.dydytt.net:1001/傲骨贤妻第六季/[阳光电影www.ygdy8.com]傲骨贤妻第六季第01集[中英双字].rmvb
#ftp://dygod2:dygod2@y009.dygod.org:1004/行尸走肉第五季/[阳光电影www.ygdy8.com]行尸走肉第五季第01集[中英双字].rmvb
#ftp://ygdy8:ygdy8@yg90.dydytt.net:2048/[阳光电影www.ygdy8.com]行尸走肉第八季第09集[中英双字].rmvb
#[\u4e00-\u9fa5]中文匹配
def getList():
    for i in openSearchResult():
        print i
getList()