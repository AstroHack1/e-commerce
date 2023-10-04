from django.db.models import Sum, F

from products.models import Basket


def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}

# , 'basekets_summ': Basket.objects.filter(user=user).aggregate(Sum(sum))}