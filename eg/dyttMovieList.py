from bs4 import BeautifulSoup


import urllib3.request

def downloadSongs():

    url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    http = urllib3.PoolManager()

    page = http.request(method='GET', url=url, headers = headers)

    html = page.data

    #from_encoding  解决中文显示
    soup = BeautifulSoup(html, 'html.parser', from_encoding='gb18030')
    # print(soup.prettify())

    for a in soup.find_all(name='a', attrs={'class': 'ulink'}):

        # print(a.text)
        nextPageUrl = a.text + ' 网页地址：' + 'http://www.dytt8.net/' + a.get('href')

        print(nextPageUrl)

        #可以通过nextPageUrl获取评分和下载地址（未完待续）




if __name__ == '__main__':
    downloadSongs()
