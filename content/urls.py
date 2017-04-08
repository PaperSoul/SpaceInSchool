from django.conf.urls import url
from . import views

app_name = 'content'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^home$', views.HomeView.as_view(), name='home'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
	url(r'^questions$', views.QuestionsView.as_view(), name='questions'),
	url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view(), name='question-detail'),
]