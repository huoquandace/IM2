from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from core.views import *

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),

    path('category/list/', category_list, name='category_list'),
    path('category/add/', category_add, name='category_add'),
    path('category/edit/<int:pk>/', category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),

    path('product/list/', product_list, name='product_list'),
    path('product/add/', product_add, name='product_add'),
    path('product/edit/<int:pk>/', product_edit, name='product_edit'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),

    path('supplier/list/', supplier_list, name='supplier_list'),
    path('supplier/add/', supplier_add, name='supplier_add'),
    path('supplier/edit/<int:pk>/', supplier_edit, name='supplier_edit'),
    path('supplier/delete/<int:pk>/', supplier_delete, name='supplier_delete'),
    path('supplier/reg_prd_view/', reg_prd_view, name='reg_prd_view'),
    path('supplier/un_reg_prd/<int:pk>/', un_reg_prd, name='un_reg_prd'),
    path('supplier/reg_prd/<int:pk>/', reg_prd, name='reg_prd'),

    path('quote/add/', quote_add, name='quote_add'),
    path('quote/detail/<int:pk>', quote_detail_edit_save, name='quote_detail_edit_save'),
    path('quote/add/detail/<int:quote_id>/<int:product_id>', quote_add_detail, name='quote_add_detail'),
    path('quote/remove/detail/<int:quote_id>/<int:product_id>', quote_remove_detail, name='quote_remove_detail'),
    path('quote/add/<int:pk>/', quote_add_before, name='quote_add_before'),
    path('quote/edit/<int:pk>/', quote_edit, name='quote_edit'),
    path('quote/s/list', quote_s_list, name='quote_s_list'),
    path('quote/s/quote/<int:pk>', quote_s_quote, name='quote_s_quote'),
    path('quote/s/quote/update/<int:pk>', quote_s_quote_update, name='quote_s_quote_update'),

    # prefix_default_language=False
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)