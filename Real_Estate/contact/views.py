from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    if request.method=='POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        realtor_email=request.POST['realtor_email']

        # check if user 
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already contacted for this property')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing,listing_id=listing_id,
                        name=name,email=email,phone=phone,message=message,
                        user_id=user_id)
        contact.save()

    #     send_mail(
    #     subject = 'Property Listing Inquiry',
    #     from_email = settings.EMAIL_HOST_USER ,
    #     message = 'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #     recipient_list = [realtor_email,'s.ranaei3148@gmail.com'] ,     
    # )
    #     print('Email sent')

        messages.success(request,' your information sent')
        return redirect('/listings/'+listing_id)
        