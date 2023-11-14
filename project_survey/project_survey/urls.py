"""
URL configuration for project_survey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from survey_app.views import func,func1,func2,func3,delete,del_ques,get_answer
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',func),
    path('answer/<int:question_id>',func1),
    path('get_ques/',func2),
    path('get_ans/',get_answer),
    path('update/<int:surveyid>',func3),
    path('del_ans/<int:surveyid_id>',delete),
    path('del_ques/<int:question_id>',del_ques),
    
]
