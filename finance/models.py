from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    created_date = models.DateTimeField(verbose_name='거래일시',
                                        auto_now_add=timezone.now)
    abstract = models.CharField(
        verbose_name='적요',
        max_length=255,
        help_text='어떤 경로로 거래가 이루어졌는지에 대한 설명입니다.\n예를 들어, 체크카드 결제를 했으면 \'체크카드\'라고 적어주세요.\n잘 모르겠으면 은행 내역을 출력한 내용을 넣으면 됩니다.'
    )
    target = models.CharField(
        verbose_name='보낸분/받는분',
        max_length=255
    )
    category_major = models.CharField(verbose_name='계정과목',
                                      max_length=255)
    category_minor = models.CharField(verbose_name='계정과목 소분류',
                                      max_length=255)
    memo = models.TextField(verbose_name='보낸분/받는분',
                            blank=True)
    deposit = models.BigIntegerField(verbose_name='입금액')
    withdraw = models.BigIntegerField(verbose_name='출금액')
    money_left = models.BigIntegerField(verbose_name='잔액', blank=True)
    modified_date = models.DateTimeField(verbose_name='수정일시',
                                         auto_now=timezone.now)

    class Meta:
        app_label = 'finance'
        ordering = ('-created_date', )
        verbose_name = '거래내역'
        verbose_name_plural = '거래내역들'

    def save(self, *args, **kwargs):
        last_left = Transaction.objects.last().money_left
        if not last_left:
            last_left = 0
        last_left += self.deposit
        last_left -= self.withdraw
        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.created_date}: {-self.withdraw if self.withdraw != 0 else self.deposit}'
