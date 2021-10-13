from datetime import datetime

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Class Based View (LoginView)
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# Class Based View (LogoutView)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

# Class Based View (CreateView)


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


# Class Based View


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# Function Based
# def home(request):
#    return render(request,'home/welcome.html',{
#        'today':datetime.today()
#    })

# @login_required(login_url='/admin')
# def authorized(request):
#    return render(request,'home/authorized.html',{})
