from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from cast import views


urlpatterns = [
    url(r'^$', views.index), #처음에 r'$' 공백페이지를 연결하는 코드 없어서 임시로 추가함.
    url(r'^admin/', admin.site.urls),
    url(r'^cast/', include('cast.urls', namespace='cast')),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('allauth.urls')),
    #comment edit ajax
    url(r'^comment/edit/(?P<comment_pk>\d+)/$', views.comment_editform),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)), ]
