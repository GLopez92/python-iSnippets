from django import forms

class UserForm(forms.Form):

    title = forms.CharField(label='Title', max_length=256)
    
    language = forms.CharField(label='Language', max_length=256)

    snippet = forms.CharField(label='Snippet', widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))

