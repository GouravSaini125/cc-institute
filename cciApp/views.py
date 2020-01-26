from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Blog
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounts.models import Testimonial


def index(request):
    testimonials = Testimonial.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses, 'testimonials': testimonials})


def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})


@login_required
def detail(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'detail.html', {'course': course})


def contact(request):
    if request.method == "POST":
        try:
            sub = request.POST['subject']
            email = request.POST['email']
            msg = request.POST['comment']
            name = request.POST['author']

            msg = name + \
                f' has sent you an email.\nE-mail -> {email}\n\nSubject -> {sub}\n' + msg

            send_mail('E-mail from Website', msg, email,
                      ['ccieducation1@gmail.com'])

            response_data = {'Message': 'Email has been sent successfully!'}
        except:
            response_data = {'Message': 'Failed to send Email!'}

        return JsonResponse(response_data)
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def category(request, name):
    courses = Course.objects.all().filter(category=name)
    return render(request, 'course.html', {'courses': courses})


def blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blogs.html', {'blogs': blogs})
