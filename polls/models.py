from django.db import models

# QuestionクラスとChoiceクラスの作成

# Questionには投票項目が存在する

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')

# Choiceには選択肢のテキストと投票数が存在する

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.InteferField(default=0)

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now