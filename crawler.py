# coding = UTF-8

import urllib2
import re
import os


# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html


# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re, html)
    return(url_lst)


def getFile(url):
    file_name = url.split('/')[-1]
    try:
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')

        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            f.write(buffer)
        f.close()
        print "Successfully downloaded" + " " + file_name
    except urllib2.HTTPError:
        print "Cannot download" + " " + file_name


# root_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/'
# root_url = 'http://algsdatasci.wikischolars.columbia.edu/'
# root_url = 'http://www.cs.columbia.edu/~verma/classes/uml/'
root_url = 'https://w4111.github.io/'

# raw_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/index.htm'
# raw_url = 'http://www.cs.columbia.edu/~verma/classes/uml/index.html'
raw_url = 'https://w4111.github.io/'

html = getHtml(raw_url)
url_lst = getUrl(html)

try:
    os.stat('./pdf_db')
except:
    os.mkdir('./pdf_db')
os.chdir(os.path.join(os.getcwd(), './pdf_db'))

for url in url_lst[:]:
    # url = root_url + url
    getFile(url)
