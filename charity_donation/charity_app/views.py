from django.shortcuts import render
from django.views import View

class LandingPage(View):
    def get(self, request):
        return render(request, "charity_app/index.php")

