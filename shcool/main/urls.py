from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UsersModelViewSet, ProductModelViewSet, LessonsModelViewSet, UserProductList, UserLessonList

router = DefaultRouter()

router.register("users", UsersModelViewSet)
router.register("products", ProductModelViewSet)
router.register("lessons", LessonsModelViewSet)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path('users/<int:user_id>/products/', UserProductList.as_view(), name='user-product-list'),
    path('users/<int:user_id>/lessons/', UserLessonList.as_view(), name='user-lesson-list'),

]
