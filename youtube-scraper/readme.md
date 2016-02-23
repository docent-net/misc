# Youtube scraper #

This script will download all videos from provided youtube playlist

### Requirements ###

- python dependencies (check in requirements.txt)

### Usage ###

Installation (under virtualenv):

```
    mkvirtualenv scraper
    pip install -r requirements.txt

```

Simple usage:

```
    $ python scraper.py --dir <dir> --url <playlist_url>
```

Help:

```
    $ python scraper.py --help
    Usage: scraper.py [OPTIONS] COMMAND [ARGS]...

    Options:
      -d, --dir TEXT  Directory where video files will be saved  [required]
      --url TEXT      Youtube playlist URL  [required]
      --help          Show this message and exit.
```
