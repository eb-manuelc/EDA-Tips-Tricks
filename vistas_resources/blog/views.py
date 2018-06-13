# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Post
from django.views import View
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
import json


@method_decorator(csrf_exempt, name='post')
class PostsView(View):

    def get(self, request, *args, **kwargs):
        if kwargs and kwargs['pk']:
            post_list = Post.objects.filter(id=kwargs['pk'])
        else:
            post_list = list(Post.objects.all())
        post_list = serializers.serialize("json", post_list)
        return HttpResponse(post_list)

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        created_post = Post.objects.create(
            author=User.objects.get(id=body['fields']['author']),
            title=body['fields']['title'],
            text=body['fields']['text'],
            created_date=body['fields']['created_date'],
            published_date=body['fields']['published_date'],
        )
        return HttpResponse(created_post)
