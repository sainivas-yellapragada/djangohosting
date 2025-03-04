from django.shortcuts import render, redirect
from .models import Contact

def home(request):
    if request.method == "POST":
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone-number')

        # Save contact to database
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )

        return redirect('home')  # Redirect to clear the form

    contacts = Contact.objects.all()  # Retrieve all saved contacts
    return render(request, 'contactapp/index.html', {'contacts': contacts})
