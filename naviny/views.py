from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def naviny_home(request):
    naviny = Articles.objects.order_by('-date')
    return render(request, 'naviny/naviny_home.html', {'naviny': naviny})


class NavinyDetailView(DetailView):
    model = Articles
    template_name = 'naviny/detailes_view.html'
    context_object_name = 'article'


class NavinyUpdateView(UpdateView):
    model = Articles
    template_name = 'naviny/create.html'

    form_class = ArticlesForm


class NavinyDeleteView(DeleteView):
    model = Articles
    success_url = '/naviny/'
    template_name = 'naviny/naviny-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('naviny_home')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()


    data = {'form': form, 'error': error}


    return render(request, 'naviny/create.html', data)
