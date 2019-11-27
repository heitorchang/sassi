from django.contrib import admin
from django.urls import path, include
from ui.views import index as ui_index
from fridge.views import index as fridge_index
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(url="/fridge/", permanent=False), name="index"),
    path('', fridge_index, name="index"),
    path('menu/', ui_index, name="menu"),
    path('ui/', include('ui.urls')),
    path('admin/', admin.site.urls),
    path('tesdir/', include('tesdir.urls')),
    path('fridge/', include('fridge.urls')),
    path('extrato/', include('extrato.urls')),
]
