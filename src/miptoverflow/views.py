from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
	template_name = "home.html"

class UserSettings(TemplateView):
	template_name = "settings.html"

class SearchQuestion(TemplateView):
	template_name = "search.html"

class AskQuestion(TemplateView):
	template_name = "ask.html"

class UserQuestion(TemplateView):
	template_name = "question.html"

class SignIn(TemplateView):
	template_name = "signin.html"

class SignUp(TemplateView):
	template_name = "signup.html"

class TagSearch(TemplateView):
	template_name = "tagsearch.html" 

class AboutPage(TemplateView):
	template_name = "about.html"
# Create your views here.
