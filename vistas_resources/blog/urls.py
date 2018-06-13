from django.conf.urls import url

from blog.views import PostsView


urlpatterns = [
    url(r'^post/$',
        PostsView.as_view(), name='posts'),
    url(r'^post/(?P<pk>[0-9]+|)/$',
        PostsView.as_view(), name='posts'),
]
