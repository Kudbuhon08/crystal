from django.shortcuts import render
from apps.products.models import Product, ProductImage, ProductCard
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

def view_product_cards(request, product_id):
    product = ProductCard.objects.get(id=product_id)
    product_cards = product.product_card.all()

    return render(request, 'products.html', locals())
