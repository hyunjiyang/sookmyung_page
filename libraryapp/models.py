from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    CATEGORY = (
        ('fiction', '소설'),
        ('society/culture', '사회/문화'),
        ('IT', 'IT'),
    )

    title= models.CharField(max_length=255)  ##책 제목 
    author= models.CharField(max_length=255)  ## 책 저자
    category=models.CharField(max_length=255, choices=CATEGORY)  ##책 카테고리
    publisher= models.CharField(max_length=255)  ## 책 출판사
    pub_year= models.IntegerField()  ##책 출판년도
    location= models.CharField(max_length=255)  ##책 소장위치
    describe = models.TextField()  ##책 소개
    photo = models.ImageField(null=True,blank=True, upload_to='library/') ##책 사진

    def __str__(self):
        return self.title    


class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    

