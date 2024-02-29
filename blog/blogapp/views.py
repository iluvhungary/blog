from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product  # importing the DB Product from models.py
from . form import ProductForm  # importing the form ProductForm from form.py

# Create your views here.
def product_list(request):
    products = Product.objects.all()

    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'products': products})
def product_detail(request,pk):
    products = Product.objects.get(pk=pk)
    return render(request, 'index2.html', {'product': products})
def edit(request, pk):
    # Retrieve the product with the given primary key (pk), If the product does not exist, it returns a 404 error page.
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # If the request method is POST (i.e., form submission),
        # Creates a ProductForm instance with the submitted data and the existing product (instance=product).
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()          # If valid, saves the changes to the product and
            return redirect('blogapp:product_list')        # redirects to the product list page.
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})


def delete(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('blogapp:product_list')
    return render(request, 'delete.html', {'product': product})

def home(request):
    return HttpResponse('Hello welcome to my Blog')
