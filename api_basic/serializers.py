from .models import Article
from rest_framework import serializers

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:

        model = Article
        fields = ['title','id','author','password']
        #fields = "__all__"