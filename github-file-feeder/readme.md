# Github file feeder #

# this is WORK IN PROGRESS #

# DO NOT USE IT #

This script provides easy way to follow changes in any github project file
via RSS.

### Requirements ###

- python dependencies (check in requirements.txt)

### Usage ###

Installation (under virtualenv):

```
    mkvirtualenv feeder
    pip install -r requirements.txt

```

##### Simple usage: #####

For development you might use local uwsgi instance:
```
    $ uwsgi --http :9090 --wsgi-file github_feeder.py
```

Now navigate to http://localhost:9090/file=<github_user>/<project_name>/<branch_name>/<file_name>

For instance in order to get RSS feed for **https://github.com/systemd/systemd/blob/master/NEWS**
use URL:

`http://localhost:9090/file=systemd/systemd/master/NEWS`

##### Hosting under HTTP server: #####

You can host this with Nginx / uwsgi or just uwsgi (depends on your 
requirements)

uwsgi --http :9090 --wsgi-file github_feeder.py