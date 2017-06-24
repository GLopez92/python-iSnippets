from django.http import Http404, HttpResponse

from django.shortcuts import redirect, render

from django.views.generic import DetailView, ListView

from .forms import UserForm

from .models import User

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)

        # In real life we'd retrieve this from the session.
        context['name'] = 'Guillermo'
        
        return context

class UserDetailView(DetailView):
    model = User
    template_name = 'users/detail.html'

def add(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        print '================================', form

        if form.is_valid():
            # Create and save directly.

            User(
             title=form.cleaned_data['title'].encode("utf8"), 
             language=form.cleaned_data['language'],
             description=form.cleaned_data['description'],
             snippet=form.cleaned_data['snippet']).save()
        
            return redirect('users:index')

        else:
            # Render form with errors.
            return render(request, 'users/add.html', { 'form' : form })

    else:
        # If the user sends a GET request...

        context = { 'header' : 'GET', 'form' : UserForm() }

        return render(request, 'users/add.html', context)
