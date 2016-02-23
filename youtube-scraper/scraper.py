#!/usr/bin/python3

import requests
import click
import pafy
from bs4 import BeautifulSoup
from urlparse import urljoin
from os import path

@click.group(invoke_without_command=True)
#@click.command()
@click.option('--dir', '-d',
              help='Directory where video files will be saved',
              required=True)
@click.option('--urls', '-u',
              help='URL for Youtube playlist or path to a file which contains playlists or videos URLS ',
              required=True)
def fetch(dir, urls):

    # if urls provided is a path to a file then we simply
    # parse this file for urls and get all the urls into one list:
    if path.exists(urls):
        urls_list = parse_urls_from_file(urls)
    # playlist scraping:
    elif "playlist" in urls:
        urls_list = fetch_videos_urls_from_playlist(urls)
    # direct video url
    else:
        urls_list = [urls]

    download_videos(urls_list, dir)

def parse_urls_from_file(path):
    urls = []
    with open(path, "r") as _file:
        for _line in _file:
            if "playlist" in _line:
                _urls = fetch_videos_urls_from_playlist(_line)
                urls += _urls
            else:
                urls.append(_line)
    return urls

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
        _filepath = "%s/%s.%s" % (
            dir,
            _video.title.replace(':',''),
            best.extension)
        if not path.exists(_filepath):
            best.download(quiet=False, filepath=_filepath)
        else:
            print("File exist - skipping: %s\n" % _filepath)

if __name__ == '__main__':
    fetch()
