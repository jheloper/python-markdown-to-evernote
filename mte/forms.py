from django import forms


class TestInputForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    view_format = forms.ChoiceField(choices=(('json', 'json'), ('other', 'other')))
