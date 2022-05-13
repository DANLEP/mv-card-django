from django.shortcuts import render, redirect
from django.views.generic import *

from .forms import CreateApplication
from .models import *


# Create your views here.
def phone_is_not_duplicated(phone):
    app = Application.objects.filter(status=1).filter(phone_number=phone)
    if app.count() == 0:
        return True
    else:
        return False


class LandingHome(View):
    template_name = 'landing/index.html'

    def get(self, request):
        context = {
            'form': CreateApplication(),
            'active': True
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = CreateApplication(request.POST)

        if form.is_valid():
            phone = form.instance.phone_number
            context = {
                'status': False
            }
            if phone_is_not_duplicated(phone):
                form.save()
                context['status'] = True
            return render(request, self.template_name, context)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
