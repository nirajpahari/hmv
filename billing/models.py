from django.db import models
from django.utils import timezone

# Create your models here.


class Billing(models.Model):

    ROOMS = (
        ('102', '102'),
        ('103', '103'),
        ('104', '104'),
        ('105', '105'),
        ('202', '202'),
        ('203', '203'),
        ('204', '204'),
        ('205', '205'),
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('Mix', 'Mix'),
    )

    STATUS = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
        ('Partially Paid', 'Partially Paid')
    )

    room = models.CharField(max_length=3, choices=ROOMS, primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS)
    advance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now=True)


    @property
    def remaining_amount(self):
        return self.amount-self.advance


    def __str__(self):
        return self.room
