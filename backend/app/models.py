from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Client', 'Client'),
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Client')
    reservation_history = models.JSONField(default=list, blank=True)

class VacationOffer(models.Model):
    OFFER_TYPE_CHOICES = [
        ('Accommodation', 'Accommodation'),
        ('Activity', 'Activity'),
        ('Transport', 'Transport'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    offer_type = models.CharField(max_length=20, choices=OFFER_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photos = models.JSONField(default=list, blank=True) 
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.offer_type} - {self.title}"

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('EnCours', 'EnCours'),
        ('Confirmer', 'Confirmer'),
        ('Annuler', 'Annuler'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    offer = models.ForeignKey(VacationOffer, on_delete=models.CASCADE, related_name='reservations')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='EnCours')
    date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Réservation pour {self.offer.title} par {self.user.username}"

class AdminDashboard(models.Model):
    top_destinations = models.JSONField(default=list, blank=True)
    popular_periods = models.JSONField(default=list, blank=True)

class VacationStatistics(models.Model):
    destination = models.CharField(max_length=255)
    total_bookings = models.IntegerField()
    most_popular_period = models.CharField(max_length=50)

    def __str__(self):
        return f"Stats pour {self.destination}"