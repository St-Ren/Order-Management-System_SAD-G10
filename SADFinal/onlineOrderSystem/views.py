import logging # change log level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from onlineOrderSystem.models import Staff, DataSheet, OrderForm, Boss
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .filters import UserFilter

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_staff = Staff.objects.all().count()
    num_datasheet = DataSheet.objects.all().count()
    num_orderform = OrderForm.objects.all().count()
    num_boss = Boss.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_staff': num_staff,
        'num_datasheet': num_datasheet,
        'num_orderform': num_orderform,
        'num_boss': num_boss,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class StaffView(generic.ListView):
    model = Staff
    context_object_name = 'staff_list'
    queryset = Staff.objects.all()  # Get 5
    template_name = 'onlineOrderSystem/Staff_list.html'

class StaffDetailView(generic.DetailView):
    model = Staff
    context_object_name = 'staff'
    template_name = 'onlineOrderSystem/Staff_detail.html'

class StaffListView(generic.ListView):
    model = Staff
    paginate_by = 10

class DataSheetView(generic.ListView):
    model = DataSheet
    context_object_name = 'datasheet_list'
    queryset = DataSheet.objects.all()
    template_name = 'onlineOrderSystem/DataSheet_list.html'

class DataSheetDetailView(generic.DetailView):
    model = DataSheet
    context_object_name = 'data_sheet'
    template_name = 'onlineOrderSystem/DataSheet_detail.html'

class DataSheetListView(generic.ListView):
    model = DataSheet
    paginate_by = 10

class OrderFormView(generic.ListView):
    model = OrderForm
    context_object_name = 'orderform_list'
    queryset = OrderForm.objects.all()  # Get 5
    template_name = 'onlineOrderSystem/OrderForm_list.html'

class OrderFormDetailView(generic.DetailView):
    model = OrderForm
    context_object_name = 'orderform_detail'
    template_name = 'onlineOrderSystem/OrderForm_detail.html'

class OrderFormListView(generic.ListView):
    model = OrderForm
    paginate_by = 10

class BossView(generic.ListView):
    model = Boss
    context_object_name = 'boss_list'
    queryset = Boss.objects.all()  # Get 5
    template_name = 'onlineOrderSystem/Boss_list.html'

class BossDetailView(generic.DetailView):
    model = Boss
    context_object_name = 'boss_detail'
    template_name = 'onlineOrderSystem/Boss_detail.html'

class BossListView(generic.ListView):
    model = Boss
    paginate_by = 10

@login_required
def my_view(request):
    class MyView(LoginRequiredMixin, View):
        login_url = '/login/'
        redirect_field_name = 'redirect_to'


########################### Functions ##############################
from onlineOrderSystem.forms import RenewForm
from django.shortcuts import render

def OrderFormCreate(request):
    if request.method == 'POST':
        if request.POST.get('IDName') and request.POST.get('hasReceivedCash') and request.POST.get('hasShipped') and request.POST.get('deadLine') and request.POST.get('firmName') and request.POST.get('dateReceived') and request.POST.get('dataSheetID'):
            post = OrderForm()
            post.IDName = request.POST.get('IDName')
            post.hasReceivedCash = request.POST.get('hasReceivedCash')
            post.hasShipped = request.POST.get('hasShipped')
            post.deadLine = request.POST.get('deadLine')
            post.firmName = request.POST.get('firmName')
            post.dateReceived = request.POST.get('dateReceived')
            post.dataSheetID = request.POST.get('dataSheetID')
            post.save()

            return render(request, 'onlineOrderSystem/OrderForm_form.html')

    else:
        return render(request, 'onlineOrderSystem/OrderForm_form.html')


def DataSheetCreate(request):
    if request.method == 'POST':
        if request.POST.get('buBien1') and request.POST.get('buBien2') and request.POST.get('buSien') \
                and request.POST.get('weiMi') and request.POST.get('koFu') and request.POST.get('length') \
                and request.POST.get('orderFormID') and request.POST.get('progress') and request.POST.get('staffID') \
                and request.POST.get('IDName') and request.POST.get('arrangement') and request.POST.get('sewingMethod'):
            post = DataSheet()
            post.buBien1 = request.POST.get('buBien1')
            post.buBien2 = request.POST.get('buBien2')
            post.buSien = request.POST.get('buSien')
            post.weiMi = request.POST.get('weiMi')
            post.koFu = request.POST.get('koFu')
            post.length = request.POST.get('length')
            post.orderFormID = request.POST.get('orderFormID')
            post.progress = request.POST.get('progress')
            post.staffID = request.POST.get('staffID')
            post.IDName = request.POST.get('IDName')
            post.arrangement = request.POST.get('arrangement')
            post.sewingMethod = request.POST.get('sewingMethod')
            post.save()

            return render(request, 'onlineOrderSystem/DataSheetCreate_form.html')

    else:
        return render(request, 'onlineOrderSystem/DataSheetCreate_form.html')

def staff_search(request):
    user_list = Staff.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})


class staff_search_DetailView(generic.DetailView):
    # model = Staff
    context_object_name = 'staff_search_detail'
    template_name = 'onlineOrderSystem/Staff_search_detail.html'

    def get_context_data(self,**kwargs):
         context = super(staff_search_DetailView, self).get_context_data(**kwargs)
         context['Staff'] = Staff.objects.all()
         context['DataSheet'] = DataSheet.objects.all()
         return context

    def get_queryset(self):
         return Staff.objects.all()

class orderform_search_DetailView(generic.DetailView):
    # model = Staff
    context_object_name = 'orderform_search_detail'
    template_name = 'onlineOrderSystem/Orderform_search_detail.html'

    def get_context_data(self,**kwargs):
         context = super(orderform_search_DetailView, self).get_context_data(**kwargs)
         context['OrderForm'] = OrderForm.objects.all()
         context['DataSheet'] = DataSheet.objects.all()
         return context

    def get_queryset(self):
         return OrderForm.objects.all()

def orderform_search(request):
    user_list = OrderForm.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'orderform_list.html', {'filter': user_filter})

def datasheet_search(request):
    user_list = DataSheet.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'datasheet_list.html', {'filter': user_filter})

from django.contrib import messages

def DataSheetUpdate(request, pk):
    obj = get_object_or_404(DataSheet, pk=pk)

    form = RenewForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)

        obj.save()

        messages.success(request, "成功更新")

        context = {'form': form}

        return render(request, 'onlineOrderSystem/DataSheet_form.html', context)

    else:
        context = {'form': form,
                   'error': '更新失敗，請重新嘗試。'}
        return render(request, 'onlineOrderSystem/DataSheet_form.html', context)
