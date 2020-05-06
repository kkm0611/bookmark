from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5 #한페이지에 5개만
    #template_name_suffix = '_list" 가 자동으로 되어있음

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') #북마크 추가 후 이동 할 페이지 :listView
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

# Create your views here.
