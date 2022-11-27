from django import forms


class StudentRegistration(forms.Form):
    # if wa have to defined django form field then we don't need to use django form widget
    # but if we don't have form field like for 'password' then we have to use widget
    age = forms.IntegerField()
    name = forms.CharField()
    # type password
    password = forms.CharField(widget=forms.PasswordInput())

    # hidden input
    hidden = forms.CharField(widget=forms.HiddenInput())

    # textarea
    textarea = forms.CharField(widget=forms.Textarea())

    # checkbox input
    checkbox = forms.CharField(widget=forms.CheckboxInput())

    # file input
    file = forms.CharField(widget=forms.FileInput())

    # passing custom attribute
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter name', 'name': 'name', 'id': 'id_name', 'class': 'input_field', 'required': ''}))
