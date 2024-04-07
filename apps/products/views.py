from django.shortcuts import render
from apps.products.models import Product, ProductImage
from apps.base.models import Setting, Giv, Questions, Сonfigurations, СonfigurationsImage

# Create your views here.
def product (request):
    setting = Setting.objects.latest('id')
    product = Product.objects.latest('id')
    productimage = ProductImage.objects.all()[:5]
    giv = Giv.objects.latest('id')
    questions = Questions.objects.all()
    configurations = Сonfigurations.objects.all()
    configurationsimage = СonfigurationsImage.objects.latest('id')
    
    return render(request, 'products.html', locals())
    
    