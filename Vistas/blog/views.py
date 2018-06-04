# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


# url('/contacts', MyContactsView.view())



# class MyContactsView(ClassView):

#     def get(self, *kwargs):
#         pass

#     def post(self, *kwargs):
#         pass

#     def delete(self):
#         pass


# def handle_request_test(self):