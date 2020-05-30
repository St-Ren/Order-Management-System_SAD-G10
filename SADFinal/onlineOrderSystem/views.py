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
    queryset = Staff.objects.all()[:5]  # Get 5
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
    queryset = DataSheet.objects.all()[:5]
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
    queryset = OrderForm.objects.all()[:5]  # Get 5
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
    queryset = Boss.objects.all()[:5]  # Get 5
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

class OrderFormCreate(CreateView):
    model = OrderForm
    fields = '__all__'
    context_object_name = 'orderform_create'
    template_name = 'onlineOrderSystem/OrderForm_form.html'

def OrderFormCreateRenew(request, pk):
    order_form = get_object_or_404(OrderForm, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            order_form.IDName = form.cleaned_data['renewal_data']
            order_form.hasReceivedCash = form.cleaned_data['renewal_data']
            order_form.hasShipped = form.cleaned_data['renewal_data']
            order_form.deadLine = form.cleaned_data['renewal_data']
            order_form.firmName = form.cleaned_data['renewal_data']
            order_form.dateReceived = form.cleaned_data['renewal_data']
            order_form.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('/onlineOrderSystem/orderform/') )
        else:
            form = RenewForm()

    return render(request, 'onlineOrderSystem/OrderForm_form.html')


class DataSheetUpdate(UpdateView):
    model = DataSheet
    context_object_name = 'datasheet_update'
    fields = ['progress']
    template_name = 'onlineOrderSystem/DataSheet_form.html'

def DataSheetUpdateRenew(request, pk):
    data_sheet = get_object_or_404(DataSheet, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            data_sheet.progress = form.cleaned_data['renewal_data']
            data_sheet.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('/onlineOrderSystem/datasheet/') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = RenewForm()

    return render(request, 'onlineOrderSystem/DataSheet_form.html')

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


def orderform_search(request):
    user_list = OrderForm.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'orderform_list.html', {'filter': user_filter})

def datasheet_search(request):
    user_list = DataSheet.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'datasheet_list.html', {'filter': user_filter})

class DataSheetUpdate(UpdateView):
    model = DataSheet
    context_object_name = 'datasheet_update'
    fields = ['progress']
    template_name = 'onlineOrderSystem/DataSheet_form.html'
