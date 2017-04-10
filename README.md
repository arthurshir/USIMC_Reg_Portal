# United States International Music Competition Registration Portal
USIMC Registration Portal is a live portal for applicants to register for the 2017 USIMC competition. It includes rule restrictions, application editing and submission, account management, and payments through Stripe (Est. projected $30k - $40k in transactions). It's written in Python, built with Django with PostgreSQL database, SASS for stylesheets, and is hosted on a Ubuntu instance on Amazon Web Services with an Nginx+uWSGI web server. Hourly PostgreSQL dump backed up to Dropbox folder.

## Building
Start a virtual environment, pip install requirements.txt, and add a .env with all deployment variables. (DEBUG, SECRET_KEY, DATABASE_PASSWORD, EMAIL_PASSWORD, STRIPE_TEST_SECRET_KEY, STRIPE_TEST_PUBLISHABLE_KEY, STRIPE_LIVE_SECRET_KEY, STRIPE_LIVE_PUBLISHABLE_KEY)

## Caveats
Forms don't include complete validation and is currently a mix between Django's forms instances and custom validation. Validation of models before submission of application is also in need of refactoring, (but has sufficient unit tests to back validity).
 
## Stuff I'm proud of

* rules.json - This JSON file handles the choices of multiple-choice fields in the model, various rule restrictions, and payment information in a single location. It was a neat solution that allowed for extremely easy adjustments to rules. It interfaces with the Python application with a wrapper "usimc_rules.py" for sufficient server side validation.
* SASS stylesheets architecture - I used a single base.scss to encapsulate all css attributes and modularized all styling of components. It's a common paradigm but it was my first time putting it into action which was really neat.
* Overall design - This was my first completely independant website, so I created a brand styling guide and complete UI design, which turned out pretty nicely.

## Libraries

* Django dbbackup https://django-dbbackup.readthedocs.io/en/stable/
* Djnago crontab https://github.com/kraiz/django-crontab
* Stripe https://pypi.python.org/pypi/stripe/
* Python dot-env https://github.com/theskumar/python-dotenv
* Crispy Forms https://github.com/django-crispy-forms/django-crispy-forms

## Things I'd do differently next time

* Modularize views.py. File became huge and difficult to read 
* Redo the form validation to stick to one paradigm
* Hire a separate designer and customer service worker to interface with client.
* Utilize a React + Node stack instead of Django