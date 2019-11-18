from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.http import JsonResponse
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home.html', {})


# def new(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/crud/show/')
#             except:
#                 pass
#     else:
#         form = EmployeeForm()
#     return render(request, 'form.html', {'form': form})


def saveData(request, form, template):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            queryset = Employee.objects.all()
            data['table_data'] = render_to_string('list_table.html', {'queryset': queryset})
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template, context, request=request)
    return JsonResponse(data)


def newEmp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    return saveData(request, form, 'formNew.html')


def empList(request):
    queryset = Employee.objects.all().order_by('id')
    context = {
        'queryset': queryset,
    }
    return render(request, 'list.html', context)


def empUpdate(request, id):
    instance = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=instance)
    else:
        form = EmployeeForm(instance=instance)
    return saveData(request, form, 'formUpdate.html')


# def edit(request, id):
#     instance = Employee.objects.get(id=id)
#     form = EmployeeForm(instance=instance)
#     action = '/crud/update/' + str(id) + '/'
#     return render(request, 'form.html', {'form': form, 'action': action})
#
#
# def update(request, id):
#     instance = Employee.objects.get(id=id)
#     form = EmployeeForm(request.POST, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('/crud/show/')
#     else:
#         form = EmployeeForm(instance=instance)
#         return render(request, 'form.html', {'form': form})


def delData(request, instance, template):
    data = {}
    if request.method == 'POST':
        if instance is not None:
            instance.delete()
            data['form_is_valid'] = True
            queryset = Employee.objects.all()
            data['table_data'] = render_to_string('list_table.html', {'queryset': queryset})
        else:
            data['form_is_valid'] = False
    context = {
        'instance': instance,
    }
    data['html_form'] = render_to_string(template, context, request=request)
    return JsonResponse(data)


def empDel(request, id):
    data = {}
    instance = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        instance.delete()
        data['form_is_valid'] = True
        queryset = Employee.objects.all()
        data['table_data'] = render_to_string('list_table.html', {'queryset': queryset})
    else:
        context = {
            'instance': instance,
        }
        data['html_form'] = render_to_string('formDel.html', context, request=request)
    return JsonResponse(data)
# def empDel(request, id):
#     data = {}
#     instance = get_object_or_404(Employee, id=id)
#     # instance = Employee.objects.get(id=id)
#     if request.method == 'POST':
#         instance.delete()
#         data['form_is_valid'] = True
#         queryset = Employee.objects.all()
#         data['table_data'] = render_to_string('list_table.html', {'queryset': queryset})
#
#     context = {
#         'instance': instance,
#     }
#     data['html_form'] = render_to_string('formDel.html', context, request=request)
#     return JsonResponse(data)
