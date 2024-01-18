
from django.views.generic import ListView, DetailView


from User_module.models import User
from product_module.models import Product
from utils.convarter import group_list_product


class MasterListView(ListView):
    template_name = 'master/master.html'
    model = User
    context_object_name = 'Users'
    def get_queryset(self):
        base_query = super(MasterListView, self).get_queryset()
        masters=base_query.filter(is_staff=True)
        return masters
class Master_profileDetailView(DetailView):
    template_name = 'master/Master_porofile.html'
    model = User

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        Files_product = list(Product.objects.filter(author_id=loaded_product.id).all())
        context['Products'] = group_list_product(Files_product)
        return context



