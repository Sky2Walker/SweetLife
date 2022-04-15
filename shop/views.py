from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# Create your views here.


def store(request):
    pstore = Product.objects.all()
    cstore = Category.objects.all()
    return render(request, 'shop/product/list.html',{'pstore':pstore,'cstore':cstore})


def index(request):
    prods = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'shop/index.html',{'prods':prods,'categories':categories,})


def news(request):
    return render(request, 'shop/blog/blog.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')

def detail(request, id ,slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    category = Category.objects.all()
    cart_product_form = CartAddProductForm()
    session_key=request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,'category':category,'cart_product_form':cart_product_form})