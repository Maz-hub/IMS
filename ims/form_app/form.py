from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")

    def send_email(self):
        print(f"sending email from {self.cleaned_data 
        ['email']} with message: {self.cleaned_data ['message']}")