from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자 수가 제한된 텍스트 정의 //글제목 등등..
    text = models.TextField() #글자 수에 제한 없음 // 블로그 콘텐츠 등등
    created_date = models.DateTimeField( # 날짜와 시간을 의미
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def Publish(self):
        self.published_date = timezone.now()
        self.save()
        
