from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
#from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserProfileForm
from .models import UserProfile


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'signup.html'


@login_required
def user_profile_view(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = CustomUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            #messages.success(request, 'Данные были успешно изменены!')

            return redirect('user_profile')

    else:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = CustomUserProfileForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_profile.html', context=context)


#class UserProfileView(generic.View):
#    model = UserProfile
#    template_name = 'user_profile.html'
