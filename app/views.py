from django.views.generic import (ListView,DetailView,CreateView,
    UpdateView,DeleteView,TemplateView,)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import EcoConnect, Article, Project, Event, GreenBusiness


class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class EcoConnectListView(ListView):
    model = EcoConnect
    template_name = 'app/ecoConnect_list.html'
    context_object_name = 'ecoconnects'
    ordering = ['-created_at']

class EcoConnectDetailView(DetailView):
    model = EcoConnect
    template_name = 'app/ecoConnect_detail.html'
    context_object_name = 'ecoconnect'


class EcoConnectCreateView(LoginRequiredMixin, CreateView):
    model = EcoConnect
    template_name = 'app/ecoConnect_create.html'
    fields = ['title', 'category', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ecoConnect_detail', kwargs={'pk': self.object.pk})


class EcoConnectUpdateView(LoginRequiredMixin, UpdateView):
    model = EcoConnect
    template_name = 'app/ecoConnect_update.html'
    fields = ['title', 'category', 'content']

    def get_success_url(self):
        return reverse_lazy('ecoConnect_detail', kwargs={'pk': self.object.pk})


class EcoConnectDeleteView(LoginRequiredMixin, DeleteView):
    model = EcoConnect
    template_name = 'app/ecoConnect_delete.html'
    success_url = reverse_lazy('ecoConnect_list')


@login_required
def toggle_like(request, pk):
    post = get_object_or_404(EcoConnect, pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('ecoConnect_list')

class ArticleListView(ListView):
    model = Article
    template_name = 'app/article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

class ProjectListView(ListView):
    model = Project
    template_name = 'app/project_list.html'
    context_object_name = 'projects'
    ordering = ['-created_at']

class EventListView(ListView):
    model = Event
    template_name = 'app/event_list.html'
    context_object_name = 'events'
    ordering = ['-event_date']

class GreenBusinessListView(ListView):
    model = GreenBusiness
    template_name = 'app/greenbusiness_list.html'
    context_object_name = 'businesses'
    ordering = ['name']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'category', 'content']
    template_name = 'app/article_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'app/project_detail.html'
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'location']
    template_name = 'app/project_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

class EventDetailView(DetailView):
    model = Event
    template_name = 'app/event_detail.html'
    context_object_name = 'event'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'description', 'event_date', 'location']
    template_name = 'app/event_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.pk})

class GreenBusinessDetailView(DetailView):
    model = GreenBusiness
    template_name = 'app/greenbusiness_detail.html'
    context_object_name = 'business'


class GreenBusinessCreateView(LoginRequiredMixin, CreateView):
    model = GreenBusiness
    fields = ['name', 'description', 'address', 'contact_info']
    template_name = 'app/greenbusiness_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('business_detail', kwargs={'pk': self.object.pk})
