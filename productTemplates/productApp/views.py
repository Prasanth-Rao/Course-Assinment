from django.shortcuts import render

# Create your views here.
def electronics(request):
     product_dict = {
          'heading':'Electronics',
          'product1':'Mac',
          'product2':'Dell',
          'product3':'lenova',
          'type':'e'
     }

     return render(request, 'productApp/products.html', context=product_dict)

def toys(request):
     product_dict = {
          'heading':'Toys',
          'product1':'Car',
          'product2':'Doll',
          'product3':'Teddy',
          'type':'t'
     }

     return render(request, 'productApp/products.html', context=product_dict)

def shoes(request):
     product_dict = {
          'heading': 'Shoes',
          'product1':'Nike',
          'product2':'Bata',
          'product3':'Paragon',
          'type':'s'
     }

     return render(request, 'productApp/products.html', context=product_dict)


def index(request):
    return render(request, 'productApp/index.html')
