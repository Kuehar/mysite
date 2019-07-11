# HttpReponseRedirectの追加
from django.http import HttpResponse,HttpReponseRedirect

#データベースAPIの追加,Choiceの追加
from .models import Question,Choice

# renderをインポートし、templateを呼び出す内容を追加する
from django.shortcuts import render

#404エラーを送出できるようにする
from django.http import Http404

#ショートカット get_object_or_404を追加する
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.views import generic

def index(rewuest):
    return HttpResponse("Hello World!! You're at the polls index.")

# 引数を取るViewを追加する

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    return HttpResponse("You're Voting on Question %s" % question_id)