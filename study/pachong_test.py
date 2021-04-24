
import urllib2
def download1(url):
    return urllib2.urlopen(url).read()

url="http://www.baidu.com"
print download1(url)