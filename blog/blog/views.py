from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Product,Category,Review
from blog.forms import ProductForm,CategoryForm,ReviewForm
from django.views.generic import ListView,DetailView

def main_view(request):
    if request.method == 'GET':
        return render(request, 'blok/index.html')
def current_date_view(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(now.strftime('%Y-%m-%d'))
def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('GoodBye my friend/user')

class ProductView(ListView):
    model = Product
    template_name = 'blok/products.html'
    context_object_name = 'product'

def category_view(request):
    category = Category.objects.all()
    contex = {
        'category':category
    }
    if request.method == 'GET':
        return render(request,'blok/categories.html',context=contex)

def post_detail_view(request , pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
            category = Category.objects.all()
            review = Review.objects.all()
        except Product.DoesNotExist:
            return render(request , '404.html')
        context = {
            'product':product,
            'categor':category,
            'review': review

        }
        return render(request,'blok/detail.html',context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm
        }
        return render(request , 'blok/create.html',context=context)

    if request.method == 'POST':
        form = ProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products')
        else:
            context = {
                'form':form

            }
            return render(request, 'blok/create.html', context=context)


def category_product_view(request):
    if request.method == 'GET':
        context = {
            'form1': CategoryForm
        }
        return render(request, 'blok/creates.html', context=context)

    if request.method == 'POST':
        form1 = CategoryForm(request.POST , request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/products')
        else:
            context = {
                'form1':form1

            }
            return render(request, 'blok/creates.html', context=context)

def review_product_view(request):
    if request.method == 'GET':
        context = {
            'form2': ReviewForm
        }
        return render(request, 'blok/detail.html', context=context)

    if request.method == 'POST':
        form2 = ReviewForm(request.POST , request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('/products')
        else:
            context = {
                'form2':form2

            }
            return render(request, 'blok/detail.html', context=context)