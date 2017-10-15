"""jiten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from words.views import TitleView, SubWordsView, LevelView, KanjiByLevel, KanjiDetail, KanjiDetail2, get_kanji_data

urlpatterns = [
    url(r'^$', TitleView.as_view(), name='title'),
    url(r'^kanji/level/(?P<level>[0-9]+)/$', KanjiByLevel.as_view(), name='kanji_by_level'),
    url(r'^kanji/(?P<id>[0-9]+)/$', KanjiDetail.as_view(), name='kanji'),
    url(r'^kanji2/(?P<name>\w+)/$', KanjiDetail2.as_view(), name='kanji2'),
    url(r'^subwords/$', SubWordsView.as_view(), name='subwords'),
    url(r'^level/(?P<level>[0-9]+)/$', LevelView.as_view(), name='level'),
    url(r'^admin/', admin.site.urls),
    url(r'^getkanji/', get_kanji_data),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
