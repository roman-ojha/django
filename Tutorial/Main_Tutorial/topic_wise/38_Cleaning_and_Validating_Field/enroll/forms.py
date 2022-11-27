from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # clean_<field_name>()
    def clean_name(self):
        valName = self.cleaned_data['name']
        valName = self.cleaned_data.get('name')

        if len(valName) < 4:
            # if length is less then 4 then we will raise the validation error
            raise forms.ValidationError("Enter more then or equal to 4 char")

        # if field is validated then we will return the value
        return valName
