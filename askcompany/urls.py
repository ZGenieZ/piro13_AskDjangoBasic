from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include

def mysum(request,x,y):
    result = x + y
    return HttpResponse('result = {}'.format(result))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysum/<int:x>/<int:y>/',mysum),
    path('shop/',include('shop.urls')),
    path('blog/',include('blog.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 