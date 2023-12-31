from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import gettext


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['hugomarquiswebsite@gmail.com']
            email = EmailMessage(
                subject,
                message,
                from_email,
                recipients,
                reply_to=[from_email]
            )
            email.send()
            messages.success(request, gettext(
                'Your message was successfully sent.'))
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
