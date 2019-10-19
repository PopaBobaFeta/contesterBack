from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.user.is_authenticated:
        ctx = {"name": "123"}
        return render(request, 'index.html', ctx)
    else:
        return render(request, 'index.html', {})


def test(request):
    return HttpResponse("Hello test")


class RegistrationView(FormView):
    form_class = UserCreationForm
    success_url = '/'

    template_name = 'registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationView, self).form_invalid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/'

    template_name = 'login.html'

    def form_valid(self, form):
        authenticate(self.request)
        login(self.request, form.get_user())
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        # if self.request.session.test_cookie_worked():
        #     self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    # def get_success_url(self):
    #     import ipdb; ipdb.set_trace()
    #     redirect_to = self.request.GET.get(self.redirect_field_name)
    #     if not is_safe_url(url=redirect_to, host=self.request.get_host()):
    #         redirect_to = self.success_url
    #     return redirect_to


def logout1(request):
    logout(request)
    return render(request, 'index.html', {})
