from django.shortcuts import get_object_or_404, render

from .models import Category, Products

# Create your views here.




def categories(request):
    return {
        "categories": Category.objects.all()
    }
    

def all_products(request):
    
    #It is an SQL query. SELECT * from Products table
    productList = Products.objects.all()
    
    return render(request,  'store/home.html', {'product': productList})


#for detailview
def product_details(request, slug):
    # select row from table Products where slug = slug and in_stock = True
    # store this row or object in the variable product
    product= get_object_or_404(Products, slug =slug, in_stock = True)

    return render(request, 'store/product/productdetail.html', {"product": product})


def categories_list(request, category_slug):
    #used to find one object in the category table
    category= get_object_or_404(Category, slug=category_slug)

    #query the database for all objects in a specific category
    products =Products.objects.filter(category= category)

    return render(request, 'store/product/category.html', {'products':products, 'category':category})

