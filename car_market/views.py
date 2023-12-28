from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.urls import reverse
from django.http import HttpResponse, request
from django.views import generic


##############################READ#############
# не полная информация

class CarListView(generic.ListView):
    template_name = 'cars/car_list.html'
    model = models.Car

    def get_queryset(self):
        return self.model.objects.all()


# def car_list(request):
#     if request.method == 'GET':
#         cars = models.Car.objects.all()
#         return render(request, template_name='cars/car_list.html',
#                       context={'cars': cars})

class CarDetailView(generic.DetailView):
    template_name = 'cars/car_detail.html'
    context_object_name = 'car_id'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)


# def car_detail(request, id):
#     if request.method == "GET":
#         car_id = get_object_or_404(models.Car, id=id)
#         return render(request, template_name='cars/car_detail.html',
#                       context={'car_id': car_id})


############CREATE POST ###################

class CarCreateView(generic.CreateView):
    template_name = 'crud/create_car.html'
    model = models.Car
    form_class = forms.CarForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CarCreateView, self).form_valid(form=form)


# def car_create_view(request):
#     if request.method == "POST":
#         form = forms.CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('car_list'))
#     else:
#         form = forms.CarForm()
#         return render(request, template_name='crud/create_car.html',
#                       context={'form': form})


####DELETE####################
def car_list_delete_view(request):
    if request.method == 'GET':
        cars_delete = models.Car.objects.all()
        return render(request, template_name='crud/delete/car_list_delete.html',
                      context={'car_delete': cars_delete})


class CarDropView(generic.DeleteView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = '/car_list_delete/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)


# def car_drop_view(request, id):
#     car_id = get_object_or_404(models.Car, id=id)
#     car_id.delete()
#     # return HttpResponse('Успешно удален')
#     return redirect(reverse('car_list_delete'))


########UPDATE#####################################
def car_list_edit_view(request):
    if request.method == 'GET':
        car_update = models.Car.objects.all()
        return render(request, template_name='crud/update/car_list_update.html',
                      context={'car_update': car_update})


class CarUpdateView(generic.UpdateView):
    template_name = 'crud/update/car_update.html'
    form_class = forms.CarForm
    success_url = '/car_list_update/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CarUpdateView, self).form_valid(form=form)


# def car_update(request, id):
#     car_id = get_object_or_404(models.Car, id=id)
#     if request.method == 'POST':
#         form = forms.CarForm(instance=car_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('car_list_update'))
#     else:
#         form = forms.CarForm(instance=car_id)
#         return render(request, template_name='crud/update/car_update.html',
#                       context={
#                           "form": form,
#                           "car_id": car_id
#                       })

class SearchView(generic.ListView):
    template_name = 'cars/car_list.html'
    paginate_by = 5

    def get_queryset(self):
        return models.Car.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
