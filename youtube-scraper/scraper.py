#!/usr/bin/env python3

import requests
import click
import pafy
from bs4 import BeautifulSoup
from urlparse import urljoin

@click.group(invoke_without_command=True)
#@click.command()
@click.option('--dir', '-d',
              help='Directory where video files will be saved',
              required=True)
@click.option('--url',
              help='Youtube playlist URL',
              required=True)
def fetch(dir, url):
    urls = fetch_videos_urls_from_playlist(url)
    download_videos(urls, dir)

def fetch_videos_urls_from_playlist(playlist_url):
    res = requests.get(playlist_url)
    soup = BeautifulSoup(res.text, "html.parser")
    videos = []

    for _video_tag in soup.find_all(class_="pl-video-title"):
        href = _video_tag.find("a")["href"]
        videos.append(href)

    return videos

def download_videos(urls, dir):

    base_url = 'https://www.youtube.com'

    print("Total videos: %i" % (len(urls)))

    for idx, _url in enumerate(urls):
        _video = pafy.new(urljoin(base_url,_url))
        print("Downloading (%s / %s): %s\n" %
              ((idx+1),
               len(urls),
               _video.title
               ))
        best = _video.getbest()
        best.download(quiet=False, filepath=dir)

if __name__ == '__main__':
    fetch()
