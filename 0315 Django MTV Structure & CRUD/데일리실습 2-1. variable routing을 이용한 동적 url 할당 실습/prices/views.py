from django.shortcuts import render

# Create your views here.

def index(request, thing, cnt):

    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

    if not (thing in product_price.keys()):
        context = {'message': f'{thing}은/는 없어용'}
    else:
        context = {'message': f'{thing} {cnt}개의 가격은 {cnt*product_price[thing]}원 입니다.'}

    return render(request, 'prices/price.html', context)
