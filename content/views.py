from django.shortcuts import render
from .models import Posts, Questions
from django.views.generic import (View, TemplateView, ListView,
	DetailView, CreateView, UpdateView, DeleteView)

class IndexView(TemplateView):
	template_name = 'content/index.html'

class HomeView(ListView):
	queryset = Posts.objects.order_by('-pub_date')
	template_name = 'content/home.html'
	context_object_name = 'all_posts'

class PostView(DetailView):
	model = Posts
	template_name = 'content/post_detail.html'

class QuestionsView(ListView):
	queryset = Questions.objects.order_by('-pub_date')
	context_object_name = 'all_questions'
	template_name = 'content/questions.html'

class QuestionDetailView(DetailView):
	model = Questions
	template_name = 'content/question_detail.html'