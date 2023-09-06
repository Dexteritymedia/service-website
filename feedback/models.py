import datetime

from django.db import models

# Create your models here.

RATINGS = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)

class FeedBack(models.Model):
    name = models.CharField(max_length=500, blank=False, help_text="Enter your first name and surname")
    message = models.TextField(blank=False, help_text="Write your message")
    ratings = models.CharField(max_length=50, choices=RATINGS, blank=False, help_text="Please rate our services between 1 to 5")
    picture = models.ImageField(upload_to="reviews/", blank=True, help_text="Please upload a picture you would love to appear on the review")
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
