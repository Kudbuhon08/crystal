from django.shortcuts import render
from apps.base.models import Setting, Giv, Questions, Сonfigurations, СonfigurationsImage
from apps.products.models import Product, ProductImage

# Create your views here.

def index (request):
    setting = Setting.objects.latest('id')
    giv = Giv.objects.latest('id')
    questions = Questions.objects.all()
    configurations = Сonfigurations.objects.all()
    configurationsimage = СonfigurationsImage.objects.latest('id')
    product = Product.objects.latest('id')
    productimage = ProductImage.objects.all()[:5]
    return render(request, 'index.html', locals())


