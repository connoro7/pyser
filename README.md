#Browser CLI

## Feature Roadmap
[x] stdin/stdout implemented
[x] module to make request to ddg
[] parse response from search
[] format response as list, add key to select results by corresponding key (integer)
[] get desired page from stdin as number
[] open page using default browser, w3m, links, lynx
[] omniprompt keyboard shortcuts
[x] '?' for help menu
[] search history
[] i'm feeling lucky/ducky flag
[] storage for bookmarks
[] mark as bookmark
[] speed dial for bookmarks/bookmarks bar


# Python virtual env:
## Set up Virtual env:
cd into new directory
$ `python3.11 -m venv env`

>> then activate virtual env:
## Activate virtual env:
Start virtual env with: `$ source env/bin/activate`
Deactivate with `$ deactivate`

## Add packages to venv:
$ `pip install Flask`
$ `pip freeze > requirements.txt`

