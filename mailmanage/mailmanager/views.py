from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Mail

from .forms import Mail_Form
from django.urls import reverse


def index(request):
	return render(request, 'mailmanager/index.html')


class Home(ListView):
	model = Mail
	template_name = 'home.html'
	context_object_name = 'mails'
	paginate_by = 10

class GetMail(DetailView):
	model = Mail
	template_name = 'single_mail.html'
	context_object_name = 'item'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object.save()
		self.object.refresh_from_db()
		return context

class MailForm(CreateView):
	form_class = Mail_Form
	template_name = 'form.html'
	raise_exception = True

	def get_success_url(self):
		return reverse('mail', kwargs={'slug': self.object.slug})

	
