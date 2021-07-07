from django.contrib import admin
from django.urls import path, include
#from .views import helloworldfunc,HelloWorldClass
"""
ブラウザから来たrequest とpath()内のオレンジ文字に書かれたURLに合致したさいに、view.pyにかかれている中身の
class,functionを実行するように指示をする
"""
urlpatterns = [
    path('admin/', admin.site.urls), 
    #path('helloworldurl/', helloworldfunc),
    #path('helloworldurl2/',HelloWorldClass.as_view()),
    path('',include('helloworldapp.urls')),
]
