from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    (r'^$', 'blog.views.index'),
url(
    r'^post/(?P<slug>[^\.]+)',
    'blog.views.view_post',
    name='view_blog_post'),
url(
    r'^category/(?P<slug>[^\.]+)',
    'blog.views.view_category',
    name='view_blog_category'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/', 'blog.views.feed'),
)
