from django.urls import path

from .views import (
    QuestionListView,
    QuestionCreateView,
    AnswerListView,
    AnswerCreateView,
    AnswerBookListView
)

urlpatterns = [
    path('question/<fk>', QuestionListView.as_view(), name="questionlist"),
    path('question/create/', QuestionCreateView.as_view(), name='questioncreate'),
    path('answer/<fk>', AnswerBookListView.as_view(), name="answerlist"),
    path('answer/create/', AnswerCreateView.as_view(), name='answercreate')
]