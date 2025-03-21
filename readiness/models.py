import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class Soldier(models.Model):
    RANK_CHOICES = [
        ('Private', 'Private'),
        ('Corporal', 'Corporal'),
        ('Sergeant', 'Sergeant'),
        ('Lieutenant', 'Lieutenant'),
        ('Captain', 'Captain'),
        ('Major', 'Major'),
        ('Colonel', 'Colonel'),
        ('General', 'General'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text="name of the soldier")
    rank = models.CharField(_("soldier rank"), max_length=20, choices=RANK_CHOICES)
    unit = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return f"{self.rank} {self.name}"
    
    class Meta:
        verbose_name_plural = "`Soldiers"


class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('Weapon', 'Weapon'),
        ('Vehicle', 'Vehicle'),
        ('Communication', 'Communication'),
        ('Medical', 'Medical'),
        ('Other', 'Other'),
    ]

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Good', 'Good'),
        ('Needs Repair', 'Needs Repair'),
        ('Damaged', 'Damaged'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=EQUIPMENT_TYPES)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    assigned_to = models.ForeignKey(Soldier, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name_plural = "`Equipments"
