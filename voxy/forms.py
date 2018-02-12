from django import forms

class WordCounterForm(forms.Form):
    text_block = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))