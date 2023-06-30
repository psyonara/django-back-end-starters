from django.db import models
from django.utils.translation import gettext_lazy as _


class Make(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EngineType(models.TextChoices):
    DIESEL = 'diesel', _('Diesel')
    PETROL = 'petrol', _('Petrol')
    ELECTRIC = 'electric', _('Electric')
    HYBRID = 'hybrid', _('Hybrid')


class EngineConfiguration(models.TextChoices):
    INLINE = 'inline', _('Inline')
    V = 'v', _('V')
    FLAT = 'flat', _('Flat')
    W = 'w', _('W')
    ROTARY = 'rotary', _('Rotary')


class DrivetrainType(models.TextChoices):
    FRONT_WHEEL_DRIVE = 'fwd', _('Front Wheel Drive')
    REAR_WHEEL_DRIVE = 'rwd', _('Rear Wheel Drive')
    ALL_WHEEL_DRIVE = 'awd', _('All Wheel Drive')


class TransmissionType(models.TextChoices):
    MANUAL = 'manual', _('Manual')
    AUTOMATIC = 'automatic', _('Automatic')
    CVT = 'cvt', _('Continuously Variable Transmission')


class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50, blank=True)
    mileage = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_type = models.CharField(
        max_length=100,
        choices=EngineType.choices,
        default=EngineType.PETROL,
        blank=True
    )
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    horsepower = models.PositiveIntegerField(null=True, blank=True)
    torque = models.PositiveIntegerField(null=True, blank=True)
    zero_to_sixty = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    quarter_mile_time = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    engine_configuration = models.CharField(
        max_length=100,
        choices=EngineConfiguration.choices,
        default=EngineConfiguration.INLINE,
        blank=True
    )
    cylinders = models.PositiveIntegerField(null=True, blank=True)
    drivetrain = models.CharField(
        max_length=100,
        choices=DrivetrainType.choices,
        default=DrivetrainType.FRONT_WHEEL_DRIVE,
        blank=True
    )
    transmission = models.CharField(
        max_length=100,
        choices=TransmissionType.choices,
        default=TransmissionType.MANUAL,
        blank=True
    )
    range = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make.name} {self.model} ({self.year})"
