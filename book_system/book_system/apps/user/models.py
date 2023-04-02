from django.db import models
from django.contrib.auth.models import AbstractUser
import hashlib


# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'unknown'),
        (1, 'man'),
        (2, 'female')
    )
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='username', help_text='username')
    email = models.EmailField(max_length=255, verbose_name="email", null=True, blank=True, help_text="email")
    avatar = models.CharField(max_length=255, verbose_name="avatar", null=True, blank=True, help_text="avatar")
    # avatar = models.FileField(verbose_name="avatar", upload_to='avatar', default='avatar/default.jpg')
    gender = models.IntegerField(
        choices=GENDER_CHOICES, default=0, verbose_name="gender", null=True, blank=True, help_text="gender"
    )

    def set_password(self, raw_password):
        print("set_password")
        super().set_password(raw_password)
        #super().set_password(hashlib.md5(raw_password.encode(encoding="UTF-8")).hexdigest())

    class Meta:
        # 指定表名（数据库中的表名）
        db_table = "system_users"
        # verbose_name指定在admin管理界面中显示中文；（分字段和表，比如表就是如下所示，字段如上面字段定义所示）
        # verbose_name表示单数形式的显示，verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
        verbose_name = "User"
        verbose_name_plural = verbose_name
        # 对date_joined的字段以升序排列
        ordering = ("date_joined",)