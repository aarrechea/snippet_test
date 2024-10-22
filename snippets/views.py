from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from pygments import lexers, highlight
from pygments.formatters import HtmlFormatter
from snippets.forms import SnippetForm
from snippets.models import Snippet, Language
from celery import shared_task
from celery.utils.log import get_task_logger



""" ----------------------------------------------------------------------
Create snippet 
---------------------------------------------------------------------- """
@method_decorator(login_required, name='dispatch')
class SnippetAdd(View):
    # TODO: Implement this class to handle snippet creation, only for authenticated users.
    
    def get(self, request):
        form = SnippetForm()
        return render(request, "snippets/snippet_add.html", {'form':form, 'action':"Crear"})
    
    
    def post(self, request):                
        form = SnippetForm(request.POST)
        
        if form.is_valid():            
            user = User.objects.get(id=request.user.id)
                        
            obj = Snippet()
            obj.user = user
            obj.snippet = form.cleaned_data['snippet']
            obj.name = form.cleaned_data['name']
            obj.language = form.cleaned_data['language']
            obj.description = form.cleaned_data['description']
            obj.public = form.cleaned_data['public']
            
            obj.save()                                    
        else:
            return render(request, "snippets/snippet_add.html", {'form':form, 'action':"Crear"})
                        
        return redirect('index')




""" ----------------------------------------------------------------------
Edit snippet 
---------------------------------------------------------------------- """
@method_decorator(login_required, name='dispatch')
class SnippetEdit(View):
#    TODO: Implement this class to handle snippet editing. Allow editing only for the owner.
    def get(self, request, **kwargs):
        snippet = Snippet.objects.get(id=kwargs['id'])                
        
        if snippet.user == request.user:        
            form = SnippetForm()
            form.initial['name'] = snippet.name
            form.initial['description'] = snippet.description
            form.initial['snippet'] = snippet.snippet
            form.initial['language'] = snippet.language
            form.initial['public'] = snippet.public
            
            return render(request, "snippets/snippet_add.html", {'form':form, 'action':"Editar"})
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    
    
    def post(self, request, **kwargs):
        form = SnippetForm(request.POST)
        
        if form.is_valid():            
            obj = Snippet.objects.get(id=kwargs['id'])
            
            obj.snippet = form.cleaned_data['snippet']
            obj.name = form.cleaned_data['name']
            obj.language = form.cleaned_data['language']
            obj.description = form.cleaned_data['description']
            obj.public = form.cleaned_data['public']
            
            obj.save()
            
            queryset = Snippet.objects.filter(public=True)
            return render(request, "index.html", {"snippets": queryset})  # Placeholder
        else:
            return redirect(request.META.get('HTTP_REFERER'))


""" ----------------------------------------------------------------------
Delete snippet 
---------------------------------------------------------------------- """
@method_decorator(login_required, name='dispatch')
class SnippetDelete(View):
#    TODO: Implement this class to handle snippet deletion. Allow deletion only for the owner.
    def get(self, request, **kwargs):        
        snippet = Snippet.objects.get(id=kwargs['id'])
        
        if request.user == snippet.user:
            snippet.delete()
                
            return redirect('index')
        else:
            return redirect(request.META.get('HTTP_REFERER'))



""" ----------------------------------------------------------------------
Snippet detail
---------------------------------------------------------------------- """
class SnippetDetails(View):
    def get(self, request, *args, **kwargs):
        snippet_id = self.kwargs["id"]
        
        # TODO: Implement logic to get snippet by ID
        snippet = Snippet.objects.get(id=snippet_id)
        
        # Add conditions for private snippets
        if snippet.user == request.user or snippet.public == True:
            lexer = lexers.get_lexer_by_name(snippet.language.slug)
            formatter = HtmlFormatter()
            code = snippet.snippet            
            snippet.snippet = highlight(code, formatter=formatter, lexer=lexer)
            
            return render(
                request, "snippets/snippet.html", {"snippet": snippet}
            )  # Placeholder
        else:
            return redirect(request.META.get('HTTP_REFERER'))
            



""" ----------------------------------------------------------------------
List of user snippets
---------------------------------------------------------------------- """
@method_decorator(login_required, name='dispatch')
class UserSnippets(View):
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs["user_id"]
        # TODO: Fetch user snippets based on username and public/private logic                
        user = User.objects.get(id=user_id)
        
        if user == request.user:
                                
            snippets = Snippet.objects.filter(user=user_id)
                
            return render(
                request,
                "snippets/user_snippets.html",
                {"snippetUsername": user, "snippets": snippets},
            )  # Placeholder
        else:
            return redirect('index')



""" ----------------------------------------------------------------------
List of snippets by languages
---------------------------------------------------------------------- """
class SnippetsByLanguage(View):
    def get(self, request, *args, **kwargs):                
        lang = self.kwargs["language"]
        # TODO: Fetch snippets based on language
        lang_obj = Language.objects.get(slug=lang)                        
        queryset = Snippet.objects.filter(Q(language=lang_obj.id) & Q(public=True))
        
        return render(request, "index.html", {"snippets": queryset})  # Placeholder



""" ----------------------------------------------------------------------
Login
---------------------------------------------------------------------- """
class Login(View):
#    TODO: Implement login view logic with AuthenticationForm and login handling.
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():            
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:            
            return render(request, 'login.html', {'form':form})



""" ----------------------------------------------------------------------
Logout
---------------------------------------------------------------------- """
class Logout(View):
#    TODO: Implement logout view logic.
    def get(self, request):        
        logout(request)        
        return redirect('index')



""" ----------------------------------------------------------------------
Index
---------------------------------------------------------------------- """
class Index(View):    
    def get(self, request, *args, **kwargs):
        # TODO: Fetch and display all public snippets                
        if request.user.is_authenticated:
            queryset = Snippet.objects.filter(Q(public=True) | Q(user=request.user))
        else:            
            queryset = Snippet.objects.filter(public=True)
                                
        return render(request, "index.html", {"snippets": queryset})  # Placeholder
        
