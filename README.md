# django-satispaython

A simple django app to manage Satispay payments following the [Web-button flow](https://developers.satispay.com/docs/web-button-pay).

## Requirements

* python >= 3.6
* django >= 3
* [`satispaython`](https://github.com/otto-torino/satispaython) >= 0.2

## Installation

You can install this package with pip: `pip install django-satispaython`.

## Usage

### Key generation and key-id

In order to use django-satispaython you need to generate a [RSA private key](https://developers.satispay.com/reference#genereate-rsa-keys) and then get a [key-id](https://developers.satispay.com/reference#keyid).
Django-satispaython is based on [satispaython](https://github.com/otto-torino/satispaython) so you can import it, [create a key](https://github.com/otto-torino/satispaython#key-generation) and [obtain a key-id](https://github.com/otto-torino/satispaython#obtain-a-key-id-using-a-token).

### Configuration

Once you created a RSA key and got a key-id add django-satispaython to your INSTALLED_APPS:

```python
INSTALLED_APPS = (
  #...
  'django_satispaython.apps.DjangoSatispaythonConfig',
  #...
)
```

Then add the followings to you django settings:

```python
SATISPAYTHON_PRIVATE_KEY_PATH = '/path/to/my/key.pem'
SATISPAYTHON_KEY_ID_PATH = '/path/to/my/key-id.txt'
SATISPAYTHON_STAGING = True
```

* `SATISPAYTHON_PRIVATE_KEY_PATH`: the path of your PEM file containing the RSA private key used to get your key-id.
* `SATISPAYTHON_KEY_ID_PATH`: the path of the file containing the key-id coupled with the private-key.
* `SATISPAYTHON_STAGING`: if `True` django-satispaython will use the [Sandbox](https://developers.satispay.com/docs/sandbox-account) endpoints.

### Satispay API

In order to use the [Satispay API](https://developers.satispay.com/reference) import django-satispaython.api:

```python
from django_satispaython import api as satispay
```

Then you can:

#### Create a payment

```python
satispay.create_payment(amount_unit, currency, callback_url, expiration_date=None, external_code=None, metadata=None, idempotency_key=None)
```

You may use satispaython utility function [`format_datetime`](https://github.com/otto-torino/satispaython#create-a-payment) to get a correctly formatted `expiration_date` to supply to the request.

#### Get payment details

```python
satisapy.get_payment_details(payment_id)
```

> :information_source: All these functions return an instance of the SatispayPayment model *without* actually storing it.

If you want to store a newly created payment in the database or update an already existing one with the informations provided by the response, set the `update` parameter to `True`.

```python
satispay.create_payment(amount_unit, currency, callback_url, expiration_date=None, external_code=None, metadata=None, idempotency_key=None, update=False)
satisapy.get_payment_details(payment_id, update=False)
```

In this case an output similar to django's [`update_or_create`](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#update-or-create) will be returned.

## TODOS

* Signals
* ImproperlyConfiguredException