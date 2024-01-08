from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic


class ProductList(generic.ListView):
    model = models.Product
    template_name = 'product/product_list.html'

    def get_queryset(self):
        #return self.model.objects.filter().order_by('-id')
        return self.model.objects.filter(tags__name='для семьи')




class ProductDetail(generic.DetailView):
    template_name = 'product/product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)
