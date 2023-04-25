from django import forms


class CreateNewList(forms.Form):
    name = forms.CharField(label="New list name", max_length=200)
    check = forms.BooleanField(required=False)
