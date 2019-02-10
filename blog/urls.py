from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
 # 문자열이 아무것도 없을때,매칭 // views.post_list
  # // name='post_list'url에 이름을 붙여 뷰를 식
    url(r'^post/(?P<pk>\d+)/$', views.post_detail,name='post_detail')
]
