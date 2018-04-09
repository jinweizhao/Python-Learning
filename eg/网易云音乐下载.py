import requests
import urllib



def downloadSongs():

    #不设置请求头会被识别，只能请求到一首歌
    headers = {
       'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    #网易原创歌曲榜
    r = requests.get("http://music.163.com/api/playlist/detail?id=2884035", headers = headers)

    arr = r.json()['result']['tracks']

    for i in range(20):
        # 歌曲名字
        name = arr[i]["name"] + '.mp3'

        #http://music.163.com/song/media/outer/url?id=317151.mp3

        songID = arr[i]['id']

        link = "http://music.163.com/song/media/outer/url?id=%s.mp3" % songID

        # print(name + '-' + link)

        path = '/Users/shaopingdong/Desktop/网易云音乐歌单/' + name

        urllib.request.urlretrieve(link, path)

        print(name + ' ' + '下载完成%s' % (i + 1))



if __name__ == '__main__':
    downloadSongs()