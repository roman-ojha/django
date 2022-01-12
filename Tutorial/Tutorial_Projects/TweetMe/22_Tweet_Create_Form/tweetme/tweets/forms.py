from django import forms


from .models import Tweet

MAX_TWEET_LENGTH = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        # here meta class is describing the entire form itself

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            # if tweet will exced the the max length then we will throw an error
            raise forms.ValidationError("This tweet is too long")
        return content
