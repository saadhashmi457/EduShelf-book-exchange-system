from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from contactform.models import ContactMessage
from accounts.models import CustomUser

# Create your views here.
def home(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

# def contact(request):
#     return render(request,"main/contact.html")

def browsebook(request):
    return render(request,"main/browse_page.html")

@login_required
def mylisting(request):
    return render(request,"main/mylisting.html")

@login_required
def addbook(request):
    return render(request,"main/add_book.html")

def manage_user(request):
    # ✅ Show all registered users
    all_users = CustomUser.objects.all().order_by('-university_roll_no')

    # ✅ Show all contact form submissions

    context = {
        'all_users': all_users,
    }
    
    return render(request, 'main/manage_user.html', context)


def manage_contacter(request):
    contact_messages = ContactMessage.objects.all().order_by('-date_sent')
    context = {
        'contact_messages': contact_messages
    }
    
    return render(request,"main/manage_contacter.html",context)
    

def editprofile(request):
    return render(request,"main/edit_profile.html")

def passwordreset(request):
    return render(request,"main/password_reset.html")

def FAQ_view(request):
    return render(request,"main/FAQ_S.html")


