from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import (main_view , current_date_view , goodbye_view,ProductView,category_view,create_product_view,
                        post_detail_view,category_product_view)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', main_view, name='main'),
    path('current_date/',current_date_view),
    path('goodbye/',goodbye_view),
    path('product/',ProductView.as_view(), name='product'),
    path('product/create/',create_product_view, name='create'),
    path('category/', category_view, name='category'),
    path('category/creates/',category_product_view, name='category1'),
    path('product/<int:pk>',post_detail_view,name='post')
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)