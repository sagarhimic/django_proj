from django.shortcuts import render, redirect
from testapp.models import Employee
from django.urls import reverse_lazy

def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

from django.views.generic import ListView
class EmployeeListView(ListView):
    model = Employee
    template_name = 'testapp/employee_list.html'
    context_object_name = 'emp_list'

    def get_queryset(self):
        queryset = Employee.objects.all()  # Base filter
        # Get search parameter from request
        search_query = self.request.session.get('search_key', None)
        select_query = self.request.session.get('salary_key', None)

        if search_query:
            queryset = queryset.filter(ename__icontains=search_query)  # Case-insensitive name search

        if select_query:
            queryset = queryset.filter(esal__gt=select_query)  # Case-insensitive name search

        return queryset

    def post(self,request, *args, **kwargs):
        if "clear" in request.POST:
            request.session.pop('search_key', None)
            request.session.pop('salary_key', None)
        else:
            request.session['search_key'] = request.POST.get('search_key', '')
            request.session['salary_key'] = request.POST.get('salary_key', '')
        return redirect('list')


from django.views.generic import DetailView
class EmployeeDetailView(DetailView):
    model = Employee
    template_name  ='testapp/employee_detail.html'
    context_object_name = 'employee'

from django.views.generic import CreateView
class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'testapp/employee_form.html'
    success_url = reverse_lazy('list')

from django.views.generic import UpdateView
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'testapp/employee_form.html'
    success_url = reverse_lazy('list')

from django.views.generic import DeleteView
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'testapp/employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('list')

from testapp.forms import EmployeeForm
def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})
