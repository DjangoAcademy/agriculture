
from django.shortcuts import render, redirect
from.models import Contact

def contact(request):

    if request.method == 'POST':
        name_form = request.POST.get('name')
        email_form = request.POST.get('email')
        message_form = request.POST.get('message')

        contact_from = Contact(name=name_form, email=email_form, message=message_form)
        contact_from.save()
        return redirect('home')

    else:
        return render(request, 'contact/contact.html')