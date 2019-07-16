This service leverages the file.io api in order to provide a mechanism where a user can send a file or text to another user on the service. The sending part of this is done without logging in to any system.





### File structure

Directory structure description below:

```python
[name_of_project]/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py, in turn includes urls.py in apps

- apps/                    # A directory to store all our custom apps
    - accounts/            # An example custom app that includes sign-up and log-in
        - models.py        # Customized user class is here
        - urls.py          # URLs for sign-up and log-in pages
        - views.py         # Views for sign-up and log-in pages
        - forms.py         # Form for editing user profile, sign-up
        - templates/       # Templates for user profile stuff
    - core/                # An example custom app that has some static pages
        - static/          # Static files
        - templates/       # Core templates, including base templates
        - etc
- manage.py                # Entry point
- Pipfile                  # Development requirements
```



## Going further

### Mailgun-powered email

Add env variables to Heroku as such:
    * MAILGUN_API_KEY
    * MAILGUN_DOMAIN

Then, add the following to your production.py:

    # Anymail (Mailgun)
    # ------------------------------------------------------------------------------
    # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
    INSTALLED_APPS += ['anymail']  # noqa F405
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
    ANYMAIL = {
        'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN')
    }


### AWS S3

AWS S3 is great for handling uploaded files. Typically, this is exactly what
you need: AWS supports as many and as large of files that your users might want
to upload.

- Use AWS:
    - Setup AWS and get your keys (follow this guide:
        https://devcenter.heroku.com/articles/s3#s3-setup)
    - Configure your keys using heroku config:add for each of the
        AWS settings specified by config/settings/production.py

