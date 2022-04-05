from django.urls import path,include
from . import views



urlpatterns = [


    path('',views.index,name = ''),
    path('news',views.news,name = 'news'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path(r'<int:id>/<slug:slug>',
        views.detail,
        name='detail'),

    path('store',views.store,name = 'store'),

]