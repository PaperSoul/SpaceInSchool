from django.db import models
from django.utils import timezone

class Posts(models.Model):
	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	title = models.CharField(max_length=500, verbose_name='Заголовок')
	post_text = models.TextField(verbose_name='Текст статьи')
	pub_date = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
	post_img = models.FileField(upload_to='posts/', verbose_name='Картинка статьи')
	width_img = models.IntegerField(default=0, verbose_name='Ширина картинки')
	height_img = models.IntegerField(default=0, verbose_name='Длинна картинки')
	def __str__(self):
		return self.title

class Questions(models.Model):
	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

	question_text = models.TextField(verbose_name='Текст вопроса')
	question_answer = models.TextField(verbose_name='Ответ', default='')
	question_img = models.FileField(upload_to='questions/',verbose_name='Картинка вопроса')
	pub_date = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
	width_img = models.IntegerField(default=0, verbose_name='Ширина картинки')
	height_img = models.IntegerField(default=0, verbose_name='Длинна картинки')

	def __str__(self):
		return self.question_text
