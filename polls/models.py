from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('问题描述', max_length=200)
    pub_date = models.DateTimeField('date published')

    # 定义Question显示的名字
    class Meta:
        verbose_name = '问题'
        # 模型的复数形式
        verbose_name_plural = '问题'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 定义class显示的名字
    class Meta:
        verbose_name = '选项'
        # 模型的复数形式
        verbose_name_plural = '选项'

    def __str__(self):
        return self.choice_test