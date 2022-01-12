from django.shortcuts import render
from django.views import View

from .models import Donation

class LandingPage(View):
    def get(self, request):
        # donations = Donation.objects.fiter(user=request.user)
        donations = Donation.objects.all()
        foundations = []
        quantity = 0
        
        for donation in donations:
            if donation.institution not in foundations:
                foundations.append(donation)
            quantity += int(donation.quantity)
        
        answer = {
            'foundations': len(foundations),
            'quantity': quantity
        }
        return render(request, "charity_app/index.html", answer)


class AddDonation(View):
    def get(self, request):
        return render(request, "charity_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "charity_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "charity_app/register.html")
