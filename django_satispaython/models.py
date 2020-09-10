from django.db import models


class SatispayPayment(models.Model):
    payment_id = models.CharField(max_length=255, primary_key=True)
    code_identifier = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    amount_unit = models.IntegerField()
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=255)
    expired = models.BooleanField()
    metadata = models.TextField(null=True, blank=True)
    sender_id = models.CharField(max_length=255, null=True, blank=True)
    sender_type = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=255, null=True, blank=True)
    receiver_id = models.CharField(max_length=255)
    receiver_type = models.CharField(max_length=255)
    insert_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    external_code = models.CharField(max_length=255, null=True, blank=True)