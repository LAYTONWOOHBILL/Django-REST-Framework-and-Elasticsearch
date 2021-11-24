from  django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Article,Category

class  UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username','first_name','last_name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializers()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'