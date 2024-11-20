from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm, PostUpdateForm#CommentForm
from django.contrib.auth.decorators import login_required





def accueil(request):
    return render(request, 'blog/accueil.html')
@login_required
def index(request):
     # Récupérer tous les posts
    posts = Post.objects.all()
    return render(request, 'blog/index.html',{'posts': posts})
from django.shortcuts import render
from .forms import PostForm  # Assurez-vous d'importer votre formulaire

def poster(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
          instance = form.save(commit=False)
          instance.author = request.user
          instance.save()
        return redirect('blog-index')
    else:
       form = PostForm() 
    posts = Post.objects.all()  # Récupérer tous les posts
    return render(request, 'blog/post.html', {'form': form, 'posts': posts})
# users/views.py
from django.shortcuts import get_object_or_404

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('users-profile')  # Redirigez vers la page de profil
from django.shortcuts import render
from .models import Post

def recherche(request):
    # Récupérer le paramètre de recherche
    query = request.GET.get('item-name', '')  # Assurez-vous que le nom corresponde à celui de votre formulaire
    posts = []  # Initialiser une liste vide pour les posts

    if query:  # Vérifier si une requête a été faite
        posts = Post.objects.filter(location__icontains=query)  # Chercher dans la base de données

    context = {
        'posts': posts,
        'query': query,
        'return_url': 'blog-index',  # Mettre le nom de l'URL de votre page principale ici
    }
    
    return render(request, 'blog/index.html', context)
     # Passez le formulaire au template

def post_edit(request,pk):
   post=Post.objects.get(id=pk)
   if request.method == 'POST':
      form = PostUpdateForm(request.POST,instance=post)
      if form.is_valid():
         form.save()
         return redirect('blog-post-detail' ,pk=post.id) 
      
         
   else:
      form=PostUpdateForm(instance=post)   
   context ={
      'post': post,
      'form':form,
   }
   return render (request,'blog/post_edit.html',context)

def post_delete(request,pk):
   post = Post.objects.get(id=pk)
   if request.method == 'POST':
      post.delete()
      return redirect('blog-index')
   context = {
      'post':post
   }
   return render(request,'blog/post_delete.html',context)

# blog/views.py
from django.shortcuts import render
from .forms import SuggestionForm
from .models import Suggestion
from django.contrib.auth.decorators import login_required

@login_required
def suggestions(request):
    success_message = None
    suggestions_list = Suggestion.objects.all()  # Récupérer toutes les suggestions

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user  # Assignez l'utilisateur actuel
            suggestion.save()
            success_message = f'Merci pour votre suggestion, {request.user.username} !'
    else:
        form = SuggestionForm()

    return render(request, 'blog/suggestions.html', {
        'form': form,
        'success_message': success_message,
        'suggestions_list': suggestions_list,  # Passer la liste des suggestions au template
    })
# blog/views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Suggestion
from django.contrib.auth.decorators import login_required

@login_required
def delete_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(Suggestion, id=suggestion_id, user=request.user)
    suggestion.delete()
    return redirect('suggestions')  # Redirigez vers la page des suggestions