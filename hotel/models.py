from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    

    def __str__(self):
        return self.name




class room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    categories=(
        ('king','KING'),
        ('queen','QUEEN'),
        ('ac','AC'),
        ('non-ac','NON-AC'),  # Note: Removed the trailing comma
        ('single','SINGLE'),
        ('double','DOUBLE'),
        ('deluxe','DELUXE'),
        ('bridalsuite','BRIDAL SUITE'),
    )
    number= models.IntegerField()
    type= models.CharField(max_length=50, choices=categories)
    bed=models.IntegerField()
    capacity=models.IntegerField()
    def __str__(self) :
        return f'{self.number}. {self.type} with {self.bed} bed[s] for {self.capacity} people'

class booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rooms = models.ForeignKey(room, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in= models.DateTimeField()
    check_out=models.DateTimeField()
    rated = models.BooleanField(default=False)
    def __str__(self) :
        return f'{self.user} has booked {self.rooms} from {self.check_in} to {self.check_out}'
    
class ReviewRating(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    booking = models.OneToOneField(booking, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(room, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=250)
    is_review = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Review' if self.is_review else 'Rating'} for {self.hotel} by {self.user}"