from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    # validation for all form field
    def clean(self):
        cleaned_data = super().clean()

        # getting field value
        valName = self.cleaned_data['name']
        valEmail = self.cleaned_data['email']
        print(len(valEmail))

        # validation for 'name'
        if len(valName) < 4:
            raise forms.ValidationError(
                'Name should be more then or equal to 4')

        # validation for 'email'
        if len(valEmail) < 10:
            raise forms.ValidationError(
                "Email should be more than or equal to 10")
