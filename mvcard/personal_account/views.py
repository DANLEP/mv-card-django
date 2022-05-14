from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from landing.models import Application, Status


class ApplicationsListView(View):
    template_name = 'personal_account/main.html'

    def get(self, request):
        if request.user.is_anonymous:
            return redirect('login')

        applications = Application.objects.filter(status=1)
        context = {
            'applications': applications,
            'app_count': applications.count(),
        }
        return render(request, self.template_name, context=context)


class ApplicationsHistoryListView(View):
    template_name = 'personal_account/history.html'

    def get(self, request):
        if request.user.is_anonymous:
            return redirect('login')

        applications = Application.objects.exclude(status=1)
        context = {
            'applications': reversed(list(applications)),
            'app_count': applications.count(),
        }
        return render(request, self.template_name, context=context)


def accept_application(request, id):
    if request.user.is_anonymous:
        return redirect('login')

    app = Application.objects.get(pk=id)
    app.status = Status.objects.get(pk=2)
    app.save()
    return redirect('account')


def decline_application(request, id):
    if request.user.is_anonymous:
        return redirect('login')

    app = Application.objects.get(pk=id)
    app.status = Status.objects.get(pk=3)
    app.save()
    return redirect('account')


def remove_application(request, id):
    if request.user.is_anonymous:
        return redirect('login')

    app = Application.objects.get(pk=id)
    app.delete()
    return redirect('account')
