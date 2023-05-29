import time
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from core.models import *
from core.forms import *

def dashboard(request):
    return render(request, 'dashboard.html')

def category_list(request):
    return render(request, 'category/list.html', {
        "categories": Category.objects.all(),
    })

def category_add(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Success"))
            return redirect('category_list')
            
    return render(request, 'category/add.html', {
        'form': CategoryAddForm,
    })

def category_edit(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        form = CategoryAddForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, _("Success"))
            return redirect('category_list')
        else:
            messages.error(request, form.errors)
            return redirect('./')
            

    return render(request, 'category/edit.html', {
        'form': CategoryAddForm(request.POST or None, instance=category)
    })

def category_delete(request, pk):
    Category.objects.get(id=pk).delete()
    time.sleep(1)
    return redirect('category_list')

def product_list(request):
    return render(request, 'product/list.html', {
        "products": Product.objects.all(),
    })

def product_add(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Success"))
            return redirect('product_list')
        else:
            messages.error(request, form.errors)
            return redirect('product_add')
            
    return render(request, 'product/add.html', {
        'form': ProductAddForm,
    })

def product_edit(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        form = ProductAddForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, _("Success"))
            return redirect('product_list')
        else:
            messages.error(request, form.errors)
            return redirect('./')
            

    return render(request, 'product/edit.html', {
        'form': ProductAddForm(request.POST or None, instance=product)
    })

def product_delete(request, pk):
    Product.objects.get(id=pk).delete()
    time.sleep(1)
    return redirect('product_list')

def supplier_list(request):
    return render(request, 'supplier/list.html', {
        "suppliers": Supplier.objects.all(),
    })

def supplier_add(request):
    if request.method == 'POST':
        form = SupplierAddForm(request.POST, request.FILES)
        account = request.POST['id_supplier']
        if form.is_valid():
            supplier = form.save()
            user = get_user_model().objects.create(username=account)
            user.set_password(account)
            user.save()
            supplier.account = user
            supplier.save()
            messages.success(request, _("Success"))
            return redirect('supplier_list')
        else:
            messages.error(request, form.errors)
            return redirect('supplier_add')
            
    return render(request, 'supplier/add.html', {
        'form': SupplierAddForm,
    })

def supplier_edit(request, pk):
    supplier = Supplier.objects.get(id=pk)
    user = get_user_model().objects.get(id=supplier.account.id)
    if request.method == 'POST':
        form = SupplierAddForm(request.POST, request.FILES, instance=supplier)
        print(request.POST)
        if form.is_valid():
            supplier = form.save()
            supplier.account = user
            supplier.save()
            messages.success(request, _("Success"))
            return redirect('supplier_list')
        else:
            messages.error(request, form.errors)
            return redirect('./')
            

    return render(request, 'supplier/edit.html', {
        'form': SupplierAddForm(request.POST or None, instance=supplier)
    })

def supplier_delete(request, pk):
    get_user_model().objects.get(id=Supplier.objects.get(id=pk).account.id).delete()
    time.sleep(1)
    return redirect('supplier_list')

def reg_prd_view(request):
    user = get_user_model().objects.get(id=request.user.id)

    if request.method == 'POST':
        product_ids = [int(x) for x in request.POST['product_ids']]
        supplier = Supplier.objects.get(account=user)
        products = [Product.objects.get(id=product_id) for product_id in product_ids]
        for product in supplier.products.all():
            products.append(product)
        supplier.products.set(products)

    return render(request, 'supplier/reg_prd.html', {
        "products": Product.objects.all(),
    })

def un_reg_prd(request, pk):
    user = get_user_model().objects.get(id=request.user.id)

    if request.method == 'POST':
        supplier = Supplier.objects.get(account=user)
        products = supplier.products.all().filter(~Q(id=pk))
        supplier.products.set(products)

    return redirect('reg_prd_view')


def reg_prd(request, pk):
    print('ok')
    user = get_user_model().objects.get(id=request.user.id)

    if request.method == 'POST':
        supplier = Supplier.objects.get(account=user)
        products = [x for x in supplier.products.all()]
        products.append(Product.objects.get(id=pk))
        supplier.products.set(products)

    # time.sleep(1)
    return redirect('reg_prd_view')

def quote_list(request):
    quotes = POrder.objects.all()
    quotes_filter = []
    for quote in quotes:
        if quote.porderdetail_set.all().count() > 0:
            quotes_filter.append(quote)
    return render(request, 'quote/list.html', {
        "quotes": quotes_filter,
    })

def quote_add(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('create_with_supplier')
        if not supplier_id:
            return redirect('quote_add')
        supplier = Supplier.objects.get(id=supplier_id)
        porder = POrder.objects.create(
            supplier = supplier,
        )
        return redirect('quote_edit', pk=porder.id)
            
    return render(request, 'quote/add.html', {
        'form': QuoteAddForm,
        "products": Product.objects.all(),
    })

def quote_edit(request, pk):
    supplier = Supplier.objects.get(account = request.user)
    quote = POrder.objects.get(id=pk)
    product_quote_detail = [x.product for x in quote.porderdetail_set.all()]
    if request.method == 'POST':
        supplier_id = request.POST.get('edit_with_supplier')
        if not supplier_id:
            messages.warning(request, 'Must have a supplier')
            return redirect('quote_edit', quote.id)
        supplier_more = Supplier.objects.get(id=supplier_id)
        quote.supplier = supplier_more
        quote.save()
        return redirect('quote_edit', pk=quote.id)
    
    return render(request, 'quote/edit.html', {
        'quote': quote,
        'product_quote_detail': product_quote_detail,
        'form': QuoteAddForm(request.POST or None, instance=quote),
        'products': quote.supplier.products.all(),
        'quote_details': quote.porderdetail_set.all(),
    })

def quote_detail_edit_save(request, pk):
    quote_detail = POrderDetail.objects.get(id=pk)
    quote = quote_detail.porder
    quote_detail.quantity = request.POST.get('quantity') or 1
    quote_detail.save()
    return redirect('quote_edit', pk=quote.id)


def quote_add_detail(request, quote_id, product_id):
    quantity = request.POST.get('quantity')
    quote = POrder.objects.get(id=quote_id)
    product = Product.objects.get(id=product_id)
    POrderDetail.objects.create(
        porder=quote,
        product=product,
    )
    return redirect('quote_edit', pk=quote.id)

def quote_remove_detail(request, quote_id, product_id):
    quote = POrder.objects.get(id=quote_id)
    product = Product.objects.get(id=product_id)
    POrderDetail.objects.get(porder=quote, product=product).delete()
    return redirect('quote_edit', pk=quote.id)
    

def quote_add_before(request, pk):
    product = Product.objects.get(id=pk)
    supplier_id = request.POST.get('supplier_more')
    if not supplier_id:
        messages.error(request, "Must choose supplier")
        return redirect('quote_add')
    supplier = Supplier.objects.get(id=supplier_id)
    porder = POrder.objects.create(
        supplier = supplier,
    )
    print(porder)
    porder_detail = POrderDetail.objects.create(
        product = product,
        porder = POrder.objects.get(id=porder.id),
        quantity = 1,
    )

    # time.sleep(1)
    return redirect('quote_edit', pk=porder.id)

def quote_s_list(request):
    supplier = Supplier.objects.get(account = request.user)
    return render(request, 'quote/s_list.html', {
        'quotes': POrder.objects.filter(~Q(status='draft'), supplier=supplier).order_by('-id'),
    })

def quote_s_quote(request, pk):
    quote = POrder.objects.get(id=pk)
    return render(request, 'quote/s_quote.html', {
        'quote': quote,
        'quote_details': quote.porderdetail_set.all(),        
    })

def quote_s_quote_update(request, pk):
    quote_detail = POrderDetail.objects.get(id=pk)
    quote_detail.price = request.POST.get('price')
    if quote_detail.price == None or quote_detail.price == "":
        messages.warning(request, _("Enter price befor update it"))
        return redirect('quote_s_quote', quote_detail.porder.id)
    quote_detail.save()
    return redirect('quote_s_quote', quote_detail.porder.id)

def quote_delete(request, pk):
    POrder.objects.get(id=pk).delete()
    time.sleep(1)
    return redirect('quote_list')


def quote_request(request, pk):
    quote = POrder.objects.get(id=pk)
    quote.status = 'new'
    quote.save()
    messages.success(request, _('Send request successfully'))
    return redirect('quote_list')

def quote_reject(request, pk):
    quote = POrder.objects.get(id=pk)
    if request.POST.get('note') is not None:
        quote.note = request.POST.get('note')
    quote.status = 'reject'
    quote.save()
    messages.warning(request, _('Reject request sent'))
    return redirect('quote_s_list')