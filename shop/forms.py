from django import forms


class ContactForm(forms.Form):
    sender = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea(attrs = {'class':'stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25' }))
