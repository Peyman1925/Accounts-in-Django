from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name='home'),
    # path('add/', add_question, name='add_question'),
    # path('test', quiz_view, name='quiz_home'),  # مسیر صفحه آزمون
    # path('submit/', submit_quiz, name='submit_quiz'),  # مسیر برای ارسال فرم آزمون
    # path('results/', quiz_results, name='quiz_results'),  # مسیر برای نمایش نتایج آزمون
    
]