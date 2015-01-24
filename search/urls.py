from django.conf.urls import patterns, url, include
#import blog.views

urlpatterns = patterns('',
   url(r'^$', 'search.views.isbn'),
   url(r'^isbn/', 'search.views.search_isbn'),
)