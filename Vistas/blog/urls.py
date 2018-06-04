from django.conf.urls import url
from blog.views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete


urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',
        PostDetail.as_view(), name='post_detail'),
    url(r'^post/delete/(?P<pk>[0-9]+)/$',
        PostDelete.as_view(), name='post_delete'),
    url(r'^post/new/$', PostCreate.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',
        PostUpdate.as_view(), name='post_edit'),
]
