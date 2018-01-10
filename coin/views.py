from django.shortcuts import render
from .models import Coin
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from .utils import scrypec


class CoinIndexView(generic.ListView):
    template_name = 'coin/coins_list.html'
    context_object_name = 'coins_list'
    paginate_by = 15
    def get_queryset(self):
        return Coin.objects.all().order_by("coin")


class CoinDetailView(generic.DetailView):
    model = Coin
    template_name = 'coin/coins_detail.html'


class CoinUpdateView(generic.ListView):
    template_name = 'coin/update.html'
    context_object_name = 'new_coins_list'
    def post(self, request, *args, **kwargs):
        scrypec.scrype_new_coins()
        scrypec.import_new_coins()
        return HttpResponseRedirect(reverse('update_list'))
    def get_queryset(self):
        return Coin.objects.filter(fl_added="True")

class CoinUpdate(generic.UpdateView):
    model = Coin
    template_name = 'coin/coin_edit.html'
    # pk_url_kwarg = 'coin'
    # fields = ['coin', 'name', 'datePrice', 'fl_added']
    fields = '__all__'
    # def get_context_data(self, **kwargs):
    #     context = super(CoinUpdate, self).get_context_data(**kwargs)
    #     print('method get_context_data in CoinUpdate')
    #     print(' context:', context)
    #     return context

    def get(self, request, *args, **kwargs):
        print('method get in CoinUpdate')
        print(args, kwargs, self.fields)
        print(self.success_url, self.request)
        # pk_url_kwarg = 'coin'
        return super(CoinUpdate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("update_list")
        return super(CoinUpdate, self).post(request, *args, **kwargs)
