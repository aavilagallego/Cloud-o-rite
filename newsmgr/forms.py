from django import forms

class AddLinkForm(forms.Form):
   ilink = forms.CharField(max_length=300)
   ititle = forms.CharField(max_length=300)
   itags = forms.CharField(max_length=300)


