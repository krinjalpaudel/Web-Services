from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from college_api import department_api, course_api, student_api, teacher_api

router = DefaultRouter()
router.register(r'departments', department_api.DepartmentViewSet)
router.register(r'courses', course_api.CourseViewSet)
router.register(r'students', student_api.StudentViewSet)
router.register(r'teachers', teacher_api.TeacherViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
