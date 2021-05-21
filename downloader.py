import m3u8
import requests
import json
from config import VIDEOS

for video in VIDEOS:
    url = video[1]
    file_name = video[0]
    domain_url = video[2]


    r = requests.get(url)
    m3u8_master = m3u8.loads(r.text)
    for chunk in m3u8_master.data['playlists']:
        print(chunk['stream_info']['resolution'])
    print("Enter a number(indexed from 0) for your prefered resolution: ", end="")
    i = int(input())
    playlist_url = m3u8_master.data['playlists'][2]['uri']

    r = requests.get(domain_url + playlist_url)
    playlist = m3u8.loads(r.text)
    with open(file_name+".ts", 'wb') as f:
        for segment in playlist.data['segments']:
            url = segment['uri']
            r = requests.get(domain_url + url)
            f.write(r.content)
    print('done downloading ' + file_name)
   
    with open(str(file_name) + ".txt", 'a') as f:
        f.write(json.dumps(playlist.data['segments'][0]['key']).replace(", ", ",\n"))