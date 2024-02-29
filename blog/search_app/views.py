from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from blogapp.models import Product
# Create your views here.


# Create your views here.
def SearchResult(request):
    query = request.GET.get('q')

    if query and query.strip():
        products = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
        return render(request, 'search.html', {'query': query, 'products': products})

    return render(request, 'index.html', {'query': query})