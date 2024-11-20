from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import signupform,CustomPasswordChangeForm, UserUpdateForm, ProfileUpdateForm  # Assurez-vous que les classes sont correctement nommées

def sign_up(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users-login')  # Redirigez vers où vous voulez après l'inscription
    else:
        form =signupform()

    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)

# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post  # Importez Post depuis l'application blog
from .forms import UserUpdateForm, ProfileUpdateForm  # Importez vos formulaires

@login_required
def profile(request):
    posts = Post.objects.filter(author=request.user)  # Filtrer les posts par l'utilisateur connecté

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    context = {
        'user': request.user,
        'posts': posts,
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Garder l'utilisateur connecté
            messages.success(request, 'Votre mot de passe a été changé avec succès.')
            return redirect('users-login')  # Redirigez vers la page de profil ou une autre page
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()  # Supprimer l'utilisateur
        messages.success(request, 'Votre compte a été supprimé avec succès.')
        return redirect('home')  # Redirigez vers la page d'accueil ou une autre page
    return render(request, 'users/delete_account.html')