import requests
import re

headers = {
    'Referer': 'https://music.163.com/',
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 "
                  "Safari/537.36"
}

def get_songs(playlist_url, out_dir):

    res = requests.get(playlist_url, headers=headers)
    for i in re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', res.text):
        download_url = "http://music.163.com/song/media/outer/url?id=%s" % i[0]
        try:
            with open(out_dir + i[1]+'.mp3', 'wb') as f:
                f.write(requests.get(download_url, headers=headers).content)
        # except FileNotFoundError:
        #     pass
        except OSError:
            pass

#https://music.163.com/playlist?id=79386231&userid=453522325
if __name__ == '__main__':
    playlist_url = "https://music.163.com/playlist?id=%s" % "490981147"
    out_dir = "D:/Temp/music/"
    get_songs(playlist_url, out_dir)