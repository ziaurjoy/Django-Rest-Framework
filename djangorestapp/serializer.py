from djangorestapp.models import Article

from rest_framework import serializers

# class ArticleSirializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     auther = serializers.CharField(max_length=50)
#     email = serializers.EmailField()
#     date_time = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.auther = validated_data.get('auther', instance.auther)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date_time = validated_data.get('date_time', instance.date_time)
#         instance.save()
#         return instance



class ArticleSirializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        

    