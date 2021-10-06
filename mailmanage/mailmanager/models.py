from django.db import models
from django.urls import reverse
from slugify import slugify


# Create your models here.

class Mail(models.Model):
	title = models.CharField(max_length=255, blank=False, verbose_name='Тема письма')
	slug = models.SlugField(max_length=255, verbose_name='Url_mail', unique=True)
	email = models.EmailField(max_length=100, blank=False, verbose_name='E-mail')
	name = models.CharField(max_length=100, blank=False, verbose_name='Имя')
	text = models.TextField(blank=True, verbose_name='Текст письма')
	allow_data_process = models.BooleanField(default=True, verbose_name='Разрешение на обработку персональных данных', blank=False)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Отправлено')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('mail', kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
			return super().save(*args, **kwargs)


	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Письмо'
		verbose_name_plural = 'Письма'