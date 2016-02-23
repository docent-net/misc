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
    $ python scraper.py --dir <dir> --urls <playlist_url or file path>
```

Help:

```
    $ python scraper.py --help
    Usage: scraper.py [OPTIONS] COMMAND [ARGS]...

    Options:
      -d, --dir TEXT  Directory where video files will be saved  [required]
      --urls TEXT     URL for Youtube playlist or path to a file which contains playlists and / or videos URLS [required]
      --help          Show this message and exit.
```
