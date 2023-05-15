from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        label="Enter Name", label_suffix=' ', initial="Roman", required=True, disabled=False, help_text="Limit 70 char", max_length="70", min_length="5")
    # Output:
    # <label for="id_name">Enter Name </label>
    # <input type="text" name="name" maxlength="70" minlength="5" required id="id_name">
    # <span class="helptext">Limit 70 char</span>
