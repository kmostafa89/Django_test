from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

    #check if user has made an inquiry already
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
        if has_contacted:
            messages.error(request, 'you have already made an inquiry for this listing')
            return redirect('listing',listing_id = listing_id)


    contact = Contact(listing=listing,
                      listing_id = listing_id,
                      name = name, 
                      email= email,
                      phone= phone,
                      message = message,
                      user_id=user_id)
    contact.save()

    send_mail(
        subject=f'Inqueiry about the listing: {listing}',
        message=f'hello sir this is a test',
        from_email='mostafa89k@gmail.com',
        recipient_list=['kmostafa89@gmail.com', realtor_email],
        fail_silently=False
        )
    messages.success(request, 'your request has been submitted we will get back to you shortly!')
    return redirect('listing',listing_id = listing_id)
