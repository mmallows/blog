from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Post
from .forms import CommentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentGet(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        post = self.get_object
        return reverse("post_detail", kwargs={"pk": post.pk})

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)