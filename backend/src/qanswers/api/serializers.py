from rest_framework import serializers
from qanswers.models import Question, Answer
from users.api.serializers import ProfileShortSerializer


class AnswerSerializer(serializers.ModelSerializer):    
    profile = ProfileShortSerializer(many=False, read_only = True)
    
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    profile = ProfileShortSerializer(many=False, read_only = True)

    class Meta:
        model = Question
        fields = ('pk', 'profile', 'question', 'creation_date', 'likes', 'dislikes', 'answers')

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['creation_date', 'likes', 'dislikes']





class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['creation_date']


