from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel


class Place(models.Model):
    room_name = models.CharField(verbose_name='방 이름',
                                 max_length=255)
    room_number = models.CharField(verbose_name='방 호실',
                                   max_length=255)

    class Meta:
        app_label = 'inventory'
        ordering = ('room_number', )
        verbose_name = '방'
        verbose_name_plural = '방들'


class Status(models.Model):
    title = models.CharField(verbose_name='비품 상태',
                             max_length=255)

    class Meta:
        app_label = 'inventory'
        ordering = ('title', )
        verbose_name = '비품 상태'
        verbose_name_plural = '비품 상태들'

    def __str__(self):
        return self.title


class OSType(models.Model):
    # i.e. 윈도우, 리눅스(?), 우분투, 센토스, 맥오에스 등
    major = models.CharField(verbose_name='운영체제 대분류',
                             max_length=255)
    version = models.CharField(verbose_name='운영체제 버전',
                               max_length=255)
    edition = models.CharField(verbose_name='운영체제 에디션',
                               max_length=255)
    bit = models.CharField(verbose_name='운영체제 비트',
                           max_length=255)

    class Meta:
        app_label = 'inventory'
        ordering = ('major', 'version', 'edition', 'bit')
        verbose_name = '운영체제'
        verbose_name_plural = '운영체제들'

    def __str__(self):
        return f'{self.major} {self.version} {self.edition} {self.bit}'


class Stock(PolymorphicModel):
    stock_id = models.CharField(verbose_name='비품 번호',
                                max_length=255)
    stock_type = models.CharField(verbose_name='비품 유형',
                                  max_length=255)
    stock_status = models.ForeignKey('Status',
                                     verbose_name='비품 상태',
                                     on_delete=models.SET_NULL,
                                     null=True)
    stock_position = models.ForeignKey('Place',
                                       verbose_name='비품 위치',
                                       on_delete=models.PROTECT)
    description = models.TextField(verbose_name='세부 설명',
                                   blank=True)
    added_date = models.DateTimeField(verbose_name='비품 구매일',
                                      auto_now_add=timezone.now,
                                      blank=True)
    modified_date = models.DateTimeField(verbose_name='비품 상태 변경일',
                                         auto_now_add=timezone.now,
                                         blank=True)

    class Meta:
        app_label = 'inventory'
        ordering = ('-added_date', )
        verbose_name = '비품'
        verbose_name_plural = '비품들'

    def __str__(self):
        return f'{self.stock_type}/{self.added_date}'

# 만약 다른 형태의 Stock을 커스토마이즈 하고 싶다면
# Stock으로 부터 상속받아서 사용하세요~
# 아래 ComputerStock은 예제입니다~


class ComputerStock(Stock):
    model_name = models.CharField(verbose_name='컴퓨터 모델명',
                                  max_length=255)
    serial_number = models.CharField(verbose_name='컴퓨터 시리얼 번호',
                                     max_length=255)
    os_type = models.ManyToManyField('OSType',
                                     verbose_name='설치된 운영체제')
    # 너무 복잡해지니깐 지웠음.
    # os_serial_number = models.CharField(verbose_name='설치된 운영체제 시리얼')

    class Meta:
        app_label = 'inventory'
        ordering = ('-added_date', )
        verbose_name = '컴퓨터'
        verbose_name_plural = '컴퓨터들'

    def __str__(self):
        return f'{self.model_name}'
