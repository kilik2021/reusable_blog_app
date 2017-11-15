from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.post_list, name="post_list")
	url(r'^/$', views.post_list, name="post_list"),
	url(r'(?P<id>\d+)/$', views.post_detail),
	url(r'top-5/$', views.top_5_posts, name="top_5"),
	url(r'top-5/(?P<id>\d+)/$', views.post_detail),
	url(r'^post/new/$', views.new_post, name='new_post'),
	url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit'),
]