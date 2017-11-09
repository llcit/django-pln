# django-pln
[![Python](https://img.shields.io/badge/python-2.7,3.4,3.5,3.6-blue.svg?style=flat)](https://www.python.org)
[![Django](https://img.shields.io/badge/django-1.8,1.9,1.10-green.svg?style=flat)](https://www.djangoproject.com)
[![Django CMS](https://img.shields.io/badge/djangocms-3.4.x-green.svg?style=flat)](https://www.django-cms.org)

This is an app of Django for Personal Learning Network(PLN). Check the [What is a PLN?](http://clt.manoa.hawaii.edu/projects/pln/)

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Django or Django-cms is required.

### Quick start
1. Download and install [django-pln](https://github.com/mingchen/django-pln) on your django project.
2. Add your settings 'pln',
```python
INSTALLED_APPS = (
	...
	'<your app directory>.uhcas_auth',
	...
)
```
3. Migrate your database,
```bash
python manage.py migrate pln
```
