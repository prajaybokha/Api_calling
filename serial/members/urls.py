'''from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from members import views

urlpatterns = [
    #path('reg/', views.RegList.as_view()),
    #path('rg/<int:pk>/', views.RegDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)'''

from members.views import UserViewSet
from rest_framework import routers
from members import views

router = routers.DefaultRouter()
router.register(r'reg', views.UserViewSet)
urlpatterns = router.urls




