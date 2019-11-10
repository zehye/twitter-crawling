from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    CHOICE_GENDER = (
        ('f', '여성'),
        ('m', '남성'),
        ('x', '선택안함')
    )
    name = models.CharField(verbose_name='이름', max_length=10)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=CHOICE_GENDER)
    phone_number = models.IntegerField(verbose_name='핸드폰번호', blank=True, null=True)
    is_social_user = models.BooleanField(verbose_name='소셜유저여부', null=True)
