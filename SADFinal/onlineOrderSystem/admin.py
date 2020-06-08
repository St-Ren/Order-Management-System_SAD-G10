from django.contrib import admin
from onlineOrderSystem.models import Staff, DataSheet, OrderForm, Boss

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('IDName', 'name', 'account', 'password', 'gender', 'birthdate', 'address', 'tel')
    fields = ['IDName', 'name', 'account', 'password', 'gender', 'birthdate', 'address', 'tel']

@admin.register(DataSheet)
class DataSheetAdmin(admin.ModelAdmin):
    list_display = ('IDName', 'orderFormID','staffID', 'progress', 'length', 'koFu','weiMi','buBien1', 'buSien', 'buBien2', 'arrangement','sewingMethod')
    fields = ['IDName', 'orderFormID','staffID', 'progress', ('length', 'koFu','weiMi','buBien1', 'buSien', 'buBien2'), ('arrangement','sewingMethod')]

@admin.register(OrderForm)
class OrderFormAdmin(admin.ModelAdmin):
    list_display = ('IDName', 'firmName', 'hasReceivedCash', 'hasShipped', 'deadLine', 'dateReceived','dataSheetID')
    fields = ['IDName', 'firmName', 'hasReceivedCash', 'hasShipped', 'deadLine', 'dateReceived','dataSheetID']

@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    list_display = ('name', 'account', 'password', 'tel')
    fields = ['name', 'account', 'password', 'tel']

