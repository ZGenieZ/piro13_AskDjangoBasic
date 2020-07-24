from django.conf import settings
from django.conf.urls.static import static
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


# settings.MEDIA_URL로 부터 요청이 오면 document_root에서 파일을 찾는다
# settings의 DEBUG = True일때만 작동, False일 때는 빈 리스트 반환
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 