
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('addcoursedetails',views.addcoursedetails,name='addcoursedetails'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('addstudentdetails',views.addstudentdetails,name='addstudentdetails'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('editdetails/<int:id>',views.editdetails,name='editdetails'),
    path('delete/<int:id>',views.delete,name='delete'),
]