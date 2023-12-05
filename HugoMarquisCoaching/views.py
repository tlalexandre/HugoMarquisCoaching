from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = EmailMessage(subject, message, from_email, ['hugomarquiswebsite@gmail.com'], reply_to=[from_email])
            email.send()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})