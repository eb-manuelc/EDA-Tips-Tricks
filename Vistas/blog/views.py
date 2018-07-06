# -*- coding: utf-8 -*-
from django.utils import timezone
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
import datetime


class PostMixin(object):
    model = Post
    fields = ['title', 'text']


class PostList(PostMixin, ListView):
    queryset = Post.objects.filter().order_by('published_date')


class PostDetail(PostMixin, DetailView):
    pass


class PostCreate(PostMixin, CreateView):
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = datetime.datetime.now()
        return super(PostCreate, self).form_valid(form)


class PostUpdate(PostMixin, UpdateView):
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = datetime.datetime.now()
        return super(PostUpdate, self).form_valid(form)


class PostDelete(PostMixin, DeleteView):
    success_url = reverse_lazy('post_list')
