import satispaython

from ._core import send_payment_request


def create_payment(amount_unit, currency, callback_url, expiration_date=None, external_code=None, metadata=None, idempotency_key=None, update=False):
    parameters = {
        'amount_unit': amount_unit,
        'currency': currency,
        'callback_url': callback_url,
        'expiration_date': expiration_date,
        'external_code': external_code,
        'metadata': metadata,
        'idempotency_key': idempotency_key
    }
    return send_payment_request(satispaython.create_payment, parameters, update, {})


def get_payment_details(payment_id, update=False):
    parameters = { 'payment_id': payment_id }
    return send_payment_request(satispaython.get_payment_details, parameters, update, {})