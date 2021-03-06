import json

from django.contrib import messages
from django import templatetags
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage, FAQ, PAY, PRODINFO
from product.models import Category, Product, Images, Variants
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def order_confirmation(request):
    return render(request, 'email_confirmation.html')


def home(request):
    setting = Setting.objects.get(pk=1)
    #category = Category.objects.all().order_by('?')[:1]
    current_user = request.user
    products_slider = Product.objects.all().order_by('?')[:1]
    products = Product.objects.all().order_by('?')[:8]
    products_slider1 = Product.objects.all().order_by('?')[:3]
    products_slider2 = Product.objects.all().order_by('?')[:3]
    products_latest = Product.objects.all().order_by('?')[:3]
    products_picked = Product.objects.all().order_by('?')[:8]
    products_top = Product.objects.all().order_by('?')[:3]
    products_review = Product.objects.all().order_by('?')[:1]
    products_top2 = Product.objects.all().order_by('?')[:3]
    products_review2 = Product.objects.all().order_by('?')[:3]
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    page = "home"
    context = {
               'setting': setting,
               
        'shopcart': shopcart,
               'total': total,
               'page': page,
               'products': products,
               'products_slider': products_slider,
               'products_slider1': products_slider1,
               'products_slider2': products_slider2,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'products_top': products_top,
               'products_top2': products_top2,
               'products_review2': products_review2,
               'products_review': products_review,
               #'category': category  
    }
    return render(request, 'home.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    products_top2 = Product.objects.all().order_by('?')[:3]
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    context = {
        'products_top2': products_top2,
        'shopcart': shopcart,
               'total': total,
        'setting': setting,
        'category': category,

    }
    return render(request, 'about.html', context)


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent. We will Get back to static as soon as possible")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    #category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    form = ContactForm
    context = {'setting': setting, 'form': form,
               'shopcart': shopcart,
               'total': total,
               #'category': category
              }
    return render(request, 'contact.html', context)


def shop(request):
    setting = Setting.objects.get(pk=1)
    #category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    products_slider = Product.objects.all().order_by('?')[:1]
    products = Product.objects.all().order_by('?')
    products_slider1 = Product.objects.all().order_by('?')[:3]
    products_slider2 = Product.objects.all().order_by('?')[:3]
    products_latest = Product.objects.all().order_by('?')[:3]
    products_picked = Product.objects.all().order_by('?')[:8]
    products_top = Product.objects.all().order_by('?')[:3]
    products_review = Product.objects.all().order_by('?')[:3]
    products_top2 = Product.objects.all().order_by('?')[:3]
    products_review2 = Product.objects.all().order_by('?')[:3]
    page = "home"
    context = {'setting': setting,
               'shopcart': shopcart,
               'total': total,
               'page': page,
               'products': products,
               'products_slider': products_slider,
               'products_slider1': products_slider1,
               'products_slider2': products_slider2,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'products_top': products_top,
               'products_top2': products_top2,
               'products_review2': products_review2,
               'products_review': products_review,
               #'category': category
              }
    return render(request, 'category.html', context)




def category_products(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    products = Product.objects.filter(category_id=id)
    products_slider1 = Product.objects.all().order_by('?')[:3]
    products_slider = Product.objects.all().order_by('?')[:1]
    products_slider2 = Product.objects.all().order_by('?')[:3]
    products_latest = Product.objects.all().order_by('?')[:3]
    products_picked = Product.objects.all().order_by('?')[:8]
    products_top = Product.objects.all().order_by('?')[:3]
    products_top1 = Product.objects.all().order_by('?')[:4]
    products_review = Product.objects.all().order_by('?')[:3]
    products_top2 = Product.objects.all().order_by('?')
    products_review2 = Product.objects.all().order_by('?')[:3]

    context = {'products': products,
               'setting': setting,
               'shopcart': shopcart,
               'total': total,
               'products_slider': products_slider,
               'products_slider1': products_slider1,
               'products_slider2': products_slider2,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'products_top': products_top,
               'products_top1': products_top1,
               'products_top2': products_top2,
               'products_review2': products_review2,
               'products_review': products_review,
               'category': category}

    return render(request, 'category.html', context)


def category(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_list = Product.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    #products = Product.objects.filter(category_id=id)
    products_slider1 = Product.objects.all().order_by('?')[:3]
    products_slider = Product.objects.all().order_by('?')[:1]
    products_slider2 = Product.objects.all().order_by('?')[:3]
    products_latest = Product.objects.all().order_by('?')[:3]
    products_picked = Product.objects.all().order_by('?')[:8]
    products_top = Product.objects.all().order_by('?')[:3]
    products_top1 = Product.objects.all().order_by('?')[:4]
    products_review = Product.objects.all().order_by('?')[:3]
    products_top2 = Product.objects.all().order_by('?')[:3]
    products_review2 = Product.objects.all().order_by('?')[:3]
    paginator = Paginator(products_list, 9)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {'products': products,
               'setting': setting,
               'shopcart': shopcart,
               'total': total,
               'products_slider': products_slider,
               'products_slider1': products_slider1,
               'products_slider2': products_slider2,
               'products_latest': products_latest,
               'products_picked': products_picked,
               'products_top': products_top,
               'products_top1': products_top1,
               'products_top2': products_top2,
               'products_review2': products_review2,
               'products_review': products_review,
               'category': category}

    return render(request, 'category.html', context)

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            products = Product.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)
            current_user = request.user
            shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
            category = Category.objects.all()
            context = {'products': products,
                       'shopcart': shopcart,
                        'total': total,
                       'query': query,
                       'setting': setting,
                       'category': category}

            return render(request, 'search_products.html', context)

        return HttpResponseRedirect('/')


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request,id,slug):
    query = request.GET.get('q')
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        if rs.product.variant == 'None':
            total += rs.product.price * rs.quantity
        else:
            total += rs.variant.price * rs.quantity
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    products_top1 = Product.objects.all().order_by('?')[:4]
    # comments = Comment.objects.filter(product_id=id,status='True')
    context = {'product': product,
               'products_top1': products_top1,
               'shopcart': shopcart,
               'total': total,
               'images': images,
               'setting': setting,
               'category': category,
               # 'comments': comments,
               }

    if product.variant != "None":
        if request.method == 'POST':
            variant_id = request.POST.get('variantid')
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw('SELECT * FROM product_variants WHERE product_id=%s GROUP BY size_id', [id])
            query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)

        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw('SELECT * FROM product_variants WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variants.objects.get(id=variants[0].id)
        context.update({
            'sizes': sizes,
            'colors': colors,
            'variant': variant,
            'query': query

        }),

    return render(request, 'product_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)


def faq(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")
    products_top2 = Product.objects.all().order_by('?')[:4]
    context = {'faq': faq,
               'setting': setting,
               'category': category,
               'products_top2': products_top2,
               }

    return render(request, 'faq.html', context)


def pay(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    pay = PAY.objects.filter(status="True").order_by("ordernumber")
    products_top2 = Product.objects.all().order_by('?')[:4]
    context = {'pay': pay,
               'setting': setting,
               'category': category,
               'products_top2': products_top2,
               }

    return render(request, 'faq.html', context)


def prodinfo(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    prodinfo = PRODINFO.objects.filter(status="True").order_by("ordernumber")
    products_top2 = Product.objects.all().order_by('?')[:4]
    context = {'prodinfo': prodinfo,
               'setting': setting,
               'category': category,
               'products_top2': products_top2,
               }

    return render(request, 'faq.html', context)
