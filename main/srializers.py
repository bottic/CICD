from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from main.models import Comment, Adv, Message


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    date = serializers.DateTimeField()


class CommentSerializers(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('Вы использовали запрещенное слово')
        return value

    def validate(self, attrs):
        if 'hello' in attrs['text'] or attrs['user'].id == 1:
            raise ValidationError('XXX')
        return attrs


class AdvSerializers(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']
        read_only_fields = ['user']


class MassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'text', 'created_at']