from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    # return HttpResponse("index")
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories':categories, 'restaurants':restaurants}
    return render(request,'shareRes/index.html', content)

def restaurantDetail(request,res_id):
    # return HttpResponse("restaurantDetail")
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant':restaurant}
    return render(request,'shareRes/restaurantDetail.html',content)

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request,'shareRes/restaurantCreate.html',content)

def categoryCreate(request):
    # return HttpResponse("categoryCreate")
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request,'shareRes/categoryCreate.html',content)

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    categoryId = request.POST['categoryId']
    category = Category.objects.get(id = categoryId)
    category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)

    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category
                         ,restaurant_name = name
                         ,restaurant_link = link
                         ,restaurant_content = content
                         ,restaurant_keyword = keyword )
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantUpdate(request,res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'categories':categories , 'restaurant':restaurant}
    return render(request,'shareRes/restaurantUpdate.html',content)

def Update_restaurant(request):
    res_id = request.POST['resId']
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)

    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    before_res = Restaurant.objects.get(id = res_id)
    before_res.category = category
    before_res.restaurant_name = name
    before_res.restaurant_link = link
    before_res.restaurant_content = content
    before_res.restaurant_keyword = keyword
    before_res.save()

    return HttpResponseRedirect(reverse('resDetailPage',kwargs={'res_id':res_id}))
