from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

Pro_CHOICES=[
    ('0', 'Select Province'),
    ('1', 'Punjab'),
    ('2', 'Sindh'),
    ('3', 'KPK'),
    ('4', 'Balochistan'),
    ('5', 'Gilgit Baltistan'),
    ('6', 'Islamabad')
    ]   


Month_CHOICES = [
    ('0', 'Select Month'),
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
    ]

class PredForm(forms.Form):
    year = forms.IntegerField(label="Year:", 
                              validators=[MinValueValidator(2021, message="Year is invalid!"), 
                              MaxValueValidator(2050, message="Please provide Year Between 2000 to 2050!")],)
    Month = forms.IntegerField( label="",widget=forms.Select(choices=Month_CHOICES),
                              validators=[MinValueValidator(1, message="Please Select Month"), 
                              MaxValueValidator(12, message="Please Select Month!")],)
    Pro = forms.IntegerField(label="Province", widget=forms.Select(choices=Pro_CHOICES),
                              validators=[MinValueValidator(1, message="Please Select Province"), 
                              MaxValueValidator(6, message="Please Select Province!")],)
    
    
