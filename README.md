# shortify
Simple URL shortener with redis storage, inspired by [shortify aiohttp](https://github.com/aio-libs/aiohttp-demos/tree/master/demos/shortify)

![screenshot](/static/images/screenshot_shortify.png)

Quickstart
```bash
$ pip install pipenv
$ pipenv install
$ pipenv shell
(shortify)$ export SECRET_KEY='change me'
(shortify)$ export DEBUG=True
(shortify)$ python manage.py runserver
```