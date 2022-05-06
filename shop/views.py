from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import  ContactForm
# Create your views here.


def store(request):
    pstore = Product.objects.all()
    cstore = Category.objects.all()
    paginator = Paginator(pstore, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)
    return render(request, 'shop/product/list.html',{'pstore':pstore,'cstore':cstore,'posts':posts})


def index(request):
    prods = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(prods, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)
    return render(request, 'shop/index.html',{'prods':prods,'categories':categories,'posts':posts})


def news(request):
    return render(request, 'shop/blog/blog.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    form_class = ContactForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
        # Заполняем форму
        form = ContactForm()
    # Отправляем форму на страницу
    return render(request, 'shop/contact.html',{'form': form})

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