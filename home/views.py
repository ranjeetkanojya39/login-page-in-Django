
from django.shortcuts import render
from django.http import HttpResponse

# ------------------------------------------
# HOME PAGE (index.html)
# ------------------------------------------
def index(request):
    return render(request, "index.html")


# ------------------------------------------
# CONTACT PAGE (contact.html)
# ------------------------------------------
def contact(request):
    return render(request, "contact.html")


# ------------------------------------------
# LOGIN PAGE (login.html)
# ------------------------------------------
def login_page(request):
    return render(request, "login.html")


# ------------------------------------------
# LOGIN FORM SUBMIT (POST method only)
# ------------------------------------------
def login_submit(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Terminal debugging output
        print("Phone:", phone)
        print("Email:", email)
        print("Message:", message)

        return HttpResponse("Form submitted successfully!")

    return HttpResponse("Invalid request method.")


# ------------------------------------------
# SUBMIT PAGE (submit.html) → shows entered data
# ------------------------------------------
def submit(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Pass data to template
        return render(request, "submit.html", {
            "phone": phone,
            "email": email,
            "message": message
        })

    # When GET request → just load page
    return render(request, "submit.html")
