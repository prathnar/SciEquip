from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . models import Product

def home(request):
    products = Product.objects.all()[:4]   # show 4 products
    return render(request, 'home.html', {"products": products})


def product_list(request):
    query = request.GET.get('q')

    products = Product.objects.all()

    if query:
        products = products.filter(
            name__icontains=query
        ) | products.filter(
            machine_function__icontains=query
        )

    # Pagination
    paginator = Paginator(products, 4)  # 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query
    }
    return render(request, "products/product_list.html", context)
    

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'products/product_detail.html', {'product': product})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')