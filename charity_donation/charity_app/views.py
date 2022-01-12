from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from .models import FOUNDATION, LOCAL_COLLECTION, NG_ORGANIZATION, Donation, Institution

class LandingPage(View):
    def get(self, request):
        # donations = Donation.objects.fiter(user=request.user)
        donations = Donation.objects.all()
        found_exemples = Institution.objects.filter(type=FOUNDATION)
        ng_org_exemples = Institution.objects.filter(type=NG_ORGANIZATION)
        local_coll_exemples = Institution.objects.filter(type=LOCAL_COLLECTION)
        foundations = []
        quantity = 0
        
        for donation in donations:
            if donation.institution not in foundations:
                foundations.append(donation)
            quantity += int(donation.quantity)

        
        found_paginator = Paginator(found_exemples, 2)
        found_page = request.GET.get('found_page')
        found_exemples = found_paginator.get_page(found_page)

        print(ng_org_exemples)
        org_paginator = Paginator(ng_org_exemples, 2)
        org_page = request.GET.get('org_page')
        ng_org_exemples = org_paginator.get_page(org_page)
        print(org_page)
        answer = {
            'foundations': len(foundations),
            'quantity': quantity,
            'found_exemples': found_exemples,
            'ng_org_exemples': ng_org_exemples,
            'local_coll_exemples': local_coll_exemples
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
