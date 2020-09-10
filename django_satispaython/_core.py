import json

from satispaython.utils import load_key
from .models import SatispayPayment
from django.conf import settings


def get_data(response, error_messages):
    if response.status_code == 200:
        return response.json()
    else:
        raise ResponseStatusError(response, error_messages.get(response.status_code))


def get_keys():
    key = load_key(settings.SATISPAYTHON_PRIVATE_KEY_PATH)
    with open(settings.SATISPAYTHON_KEY_ID_PATH) as file:
        key_id = file.read()
    return { 'key_id': key_id, 'key': key }


def send_payment_request(call, parameters, update, error_messages):
    response = call(**get_keys(), **parameters, staging=settings.SATISPAYTHON_STAGING)
    data = get_data(response, error_messages)
    return update_or_create_payment(data) if update == True else generate_payment_object(data)


def update_or_create_payment(response_data):
    defaults = format_payment_data(response_data)
    payment_id = defaults.pop('payment_id')
    return SatispayPayment.objects.update_or_create(payment_id=payment_id, defaults=defaults)


def generate_payment_object(response_data):
    data = format_payment_data(response_data)
    return SatispayPayment(**data)


def format_payment_data(response_data):
    data = {
        'payment_id': response_data['id'],
        'code_identifier': response_data['code_identifier'],
        'payment_type': response_data['type'],
        'amount_unit': response_data['amount_unit'],
        'currency': response_data['currency'],
        'status': response_data['status'],
        'expired': response_data['expired'],
        'sender_type': response_data['sender']['type'],
        'receiver_id': response_data['receiver']['id'],
        'receiver_type': response_data['receiver']['type']
    }
    if 'metadata' in response_data:
        data = { **data, 'metadata': json.dumps(response_data['metadata']) }
    if 'id' in response_data['sender']:
        data = { **data, 'sender_id': response_data['sender']['id'] }
    if 'name' in response_data['sender']:
        data = { **data, 'sender_name': response_data['sender']['name'] }
    if 'insert_date' in response_data:
        data = { **data, 'insert_date': response_data['insert_date'] }
    if 'expire_date' in response_data:
        data = { **data, 'expire_date': response_data['expire_date'] }
    if 'external_code' in response_data:
        data = { **data, 'external_code': response_data['external_code'] }
    return data