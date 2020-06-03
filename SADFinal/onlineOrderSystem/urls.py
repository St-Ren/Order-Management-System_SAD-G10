from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('staff/', views.StaffView.as_view(), name='staff'),
    path('staff/<int:pk>', views.StaffDetailView.as_view(), name='staff-detail'),

    path('datasheet/', views.DataSheetView.as_view(), name='datasheet'),
    path('datasheet/<int:pk>', views.DataSheetDetailView.as_view(), name='datasheet-detail'),

    path('orderform/', views.OrderFormView.as_view(), name='orderform'),
    path('orderform/<int:pk>', views.OrderFormDetailView.as_view(), name='orderform-detail'),

    path('boss/', views.BossView.as_view(), name='boss'),
    path('boss/<int:pk>', views.BossDetailView.as_view(), name='boss-detail'),

    ############################################

    path('orderform/create/', views.OrderFormCreate.as_view(), name='orderform_create'),
    path('orderform/<int:pk>/create/submission_complete/', views.OrderFormCreateRenew, name='order_form_create_ok'),

    path('datasheet/<int:pk>/update/', views.DataSheetUpdate.as_view(), name='datasheet_update'),
    path('datasheet/<int:pk>/update/submission_complete/', views.DataSheetUpdateRenew, name='data_sheet_update_ok'),

    path('orderform_search/', views.orderform_search, name='orderform_search'),

    path('staff_search/', views.staff_search, name='staff_search'),
    path('staff_search/<int:pk>', views.staff_search_DetailView.as_view(), name='staff_search_detail'),

    path('datasheet_search/', views.datasheet_search, name='datasheet_search'),

    path('datasheet/<int:pk>/update/', views.DataSheetUpdate.as_view(), name='datasheet_update'),
]
