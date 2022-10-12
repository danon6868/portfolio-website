# Personal portfolio website

This is a Python Django-based personal portfolio website.

The website uses [Wagtail CMS](https://github.com/wagtail/wagtail). Wagtail is a Django Content Management System.

All content: personal information, portfolio projects, social media links, etc. can be
adjusted in Wagtail admin.

This repo can be used as a starting point for developing a production-ready Django personal website with deployment to
Heroku. I am releasing the full source code for the site so that others may benefit from it.

## Live website

Currently the static version of the site is hosting via GitHub Pages. It is planned to deploy the full version to Heroku.
To view the website demo, please visit [danon6868.github.io](https://danon6868.github.io/){:target="_blank"}.

> **_NOTE:_**  The web application may take a few seconds to start up.

## Local development

Setup local environment for the development process.

Go to `./portfolio` directory and activate virtual environment.

#### Run in a terminal

```shell
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Go to `http://127.0.0.1:8000/admin/` in your browser to the Wagtail CMS admin to populate it with your data and to
configure homepage.
