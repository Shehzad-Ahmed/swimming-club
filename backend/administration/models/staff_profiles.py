from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.models import Base


class StaffProfiles(Base):

    contract_start = models.DateField()

    contract_end = models.DateField()

    residential_no = models.CharField(max_length=100)

    home_address = models.TextField()

    contact_no = PhoneNumberField(null=False, region="GB")

    designation = models.TextField()

    staff = models.OneToOneField(to="core.Users", on_delete=models.CASCADE, null=True)
