from django import forms
from .models import ReviewRating

class availabilityForm(forms.Form):
    categories = (
        ('king','KING'),
        ('queen','QUEEN'),
        ('ac','AC'),
        ('non-ac','NON-AC'),
        ('single','SINGLE'),
        ('double','DOUBLE'),
        ('deluxe','DELUXE'),
        ('bridalsuite','BRIDAL SUITE')
    )
    Categories = forms.ChoiceField(choices=categories, required=True) 
    check_in = forms.DateTimeField(required=True, input_formats=["%d-%m-%Y T%h:%M",])
    check_out = forms.DateTimeField(required=True, input_formats=["%d-%m-%Y T%h:%M",])

class ReviewRatingForm(forms.ModelForm):
    STARS_CHOICES = [(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]
    stars = forms.ChoiceField(choices=STARS_CHOICES, label='Rating', required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Comment', required=False)

    class Meta:
        model = ReviewRating
        fields = ['stars', 'comment']
