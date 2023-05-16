# Django petty-survey

A small survey application developed in django. The following packages are required for this project

* [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks/)
* [django-htmx](https://github.com/adamchainz/django-htmx)
* [django-email-blacklist](https://github.com/Zeioth/django-email-blacklist)

Use `pip install -r requirements.txt` to install all dependencies.

In your project file settings.py add the following lines. `see the example settings.py file` 

```python
INSTALLED_APPS = [
    ...,
    "django_htmx",
    "widget_tweaks",
    "django-email-blacklist",
    
    "survey" # local app (petty-survey)
    ...,
]

# Add this for load dispoable email domains
DISPOSABLE_EMAIL_DOMAINS = "/path_to_your/disposable_email_domains.txt"
````

Finally `python manage.py runserver`.