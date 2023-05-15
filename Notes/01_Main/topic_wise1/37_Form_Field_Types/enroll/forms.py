from django import forms


class StudentRegistration(forms.Form):
    # adding 'min_length' & 'max_length' validator
    name = forms.CharField(min_length=5, max_length=20,
                           strip=True, empty_value='', error_messages={'required': 'Name field is required', 'min_length': 'char length should be greater then 4'})
    # strip=True (white space will get removed)
    # strip=False (white space will not get removed)
    # empty_value (is the default value of use didn't get passed, now required will not throw an error)
    # error_message (change default error message)

    roll = forms.IntegerField(min_value=5, max_value=100)
    price = forms.DecimalField(
        min_value=5, max_value=40, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=40)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField(min_length=5, max_length=100)
    password = forms.CharField(
        min_length=5, max_length=50, widget=forms.PasswordInput())
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(
        min_length=5, max_length=50, widget=forms.TextInput())
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'cols': 50}))
    agree = forms.BooleanField(label="Agreed terms and condition?")
