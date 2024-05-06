from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'home.html')


# def quiz_view(request):
#     questions = Question.objects.all()
#     form = QuestionForm()
#     return render(request, 'quiz_template.html', {'questions': questions, 'form': form})

# def submit_quiz(request):
#     if request.method == 'POST':
#         # Process submitted form data here
#         # مثلا ذخیره پاسخ‌های کاربر در دیتابیس یا انجام محاسبات مورد نیاز
#         return redirect('quiz_results')
#     else:
#         return redirect('quiz_home')

# # def quiz_results(request):
# #     # نمایش نتایج آزمون
# #     return render(request, 'quiz_results_template.html')

# def quiz_results(request):
#     # در اینجا می‌توانید اطلاعات مورد نیاز را از دیتابیس یا سایر منابع دریافت کنید
#     correct_answers_count = 10  # تعداد پاسخ‌های صحیح
#     incorrect_answers_count = 5  # تعداد پاسخ‌های نادرست
#     score = 80  # نمره کسب شده توسط کاربر
    
#     return render(request, 'quiz_results_template.html',
#           {'correct_answers_count': correct_answers_count, 
#               'incorrect_answers_count': incorrect_answers_count, 'score': score})

# from .models import Teacher

# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save()
#             # Assuming the logged in teacher is stored in request.user.teacher
#             teacher = request.user.teacher
#             teacher.questions.add(question)
#             return redirect('home')  # Redirect to home or any other page
#     else:
#         form = QuestionForm()
#     return render(request, 'add_question.html', {'form': form})
# def add_question(request):
    
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save()
#             teacher = request.user
#             teacher.questions.add(question)
#             return redirect('home')
#         else:
#             form = QuestionForm()
#         return render(request, 'add_question.html', {'form': form})
            
        