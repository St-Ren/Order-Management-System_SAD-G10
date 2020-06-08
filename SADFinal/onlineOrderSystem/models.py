from django.db import models

class Staff(models.Model):
    account = models.CharField('帳號', max_length=20)
    password = models.CharField('密碼', max_length=20)
    gender = models.CharField('性別', max_length=6)
    birthdate = models.CharField('出生年月日', max_length=10, help_text='2020/12/12')
    id = models.AutoField(primary_key=True)
    address = models.CharField('地址', max_length=20)
    tel = models.CharField('電話', max_length=20)
    name = models.CharField('姓名', max_length=20)
    IDName = models.CharField('員工ID', max_length=10)
    ...

    class Meta:
        db_table = "員工"
        ordering = ['IDName']

    def __str__(self):
        return self.IDName

class DataSheet(models.Model):
    buBien1 = models.CharField('布邊1', max_length=30, help_text='布邊x/穿筘x根入/x根')
    buBien2 = models.CharField('布邊2', max_length=30, help_text='布邊x/穿筘x根入/x根')
    buSien = models.CharField('布身', max_length=30, help_text='布邊x/穿筘x根入/x根')
    weiMi = models.CharField('機上緯密', max_length=20, help_text='根/吋')
    koFu = models.CharField('筘幅', max_length=10, help_text='寸')
    length = models.CharField('整經長', max_length=10, help_text='y')
    id = models.AutoField(primary_key=True)
    orderFormID = models.CharField('訂單ID', max_length=20)
    progress = models.CharField('進度', max_length=100)
    staffID = models.CharField('員工ID', max_length=10)
    IDName = models.CharField('規格單ID', max_length=10)
    arrangement = models.CharField('經紗排列', max_length=100)
    sewingMethod = models.CharField('穿法', max_length=100)
    ...

    class Meta:
        db_table = "規格單"
        ordering = ['IDName']

    def __str__(self):
        return self.IDName

class OrderForm(models.Model):
    id = models.AutoField(primary_key=True)
    IDName = models.CharField('訂單ID', max_length=20)
    hasReceivedCash = models.CharField('收費', max_length=2, help_text='1/0')
    hasShipped = models.CharField('出貨', max_length=2, help_text='1/0')
    deadLine = models.CharField('期限', max_length=10, help_text='2020/12/12')
    firmName = models.CharField('廠商名字', max_length=20)
    dateReceived = models.CharField('接單日期', max_length=10, help_text='2020/12/12')
    dataSheetID = models.CharField('規格單', max_length=1000, default='none')
    ...

    class Meta:
        db_table = "訂單"
        ordering = ['IDName']

    def __str__(self):
        return self.IDName

class Boss(models.Model):
    account = models.CharField('帳號', max_length=20)
    password = models.CharField('密碼', max_length=20)
    id = models.AutoField(primary_key=True)
    tel = models.CharField('電話', max_length=20)
    name = models.CharField('姓名', max_length=20)
    ...

    def __str__(self):
        return self.name

    class Meta:
        db_table = "老闆"
        ordering = ['name']

