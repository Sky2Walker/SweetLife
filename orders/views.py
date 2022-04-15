from django.http import JsonResponse
from .models import ProductInOrder

# Create your views here.


def basket_adding(request):
    return_dict = dict
    ProductInOrder = request.session.session_key
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    data = request.POST
    product_id = data.get("product_id")
    num = data.get("num")

    products_total_num = ProductInOrder.objects.filter(session_key=session_key, is_active=True).count()
    new_product = ProductInOrder.objects.create(session_key=session_key, product_id=product_id, nub=num)
    return_dict['products_total_num'] = products_total_num
    print(request.POST)
    return JsonResponse(return_dict)
