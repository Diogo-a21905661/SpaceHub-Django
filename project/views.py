from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.

def index_page_view(request):
    return render(request, 'project/index.html')

def about_page_view(request):
    return render(request, 'project/about.html')

def contactsAdd_page_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('contactsView'))

    context = {'form': form}
    return render(request, 'project/contactsAdd.html', context)

def contactsView_page_view(request):
    context = {'users': User.objects.all()}

    return render(request, 'project/contactsView.html', context)

def contactsEdit_page_view(request, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('contactsView')

    context = {'form': form, 'user_id': user_id}

    return render(request, 'project/contactsEdit.html', context)

def contactsDelete_page_view(request, user_id):
    User.objects.get(pk=user_id).delete()
    return HttpResponseRedirect(reverse('contactsView'))

def quizAdd_page_view(request):
    form = Quiz(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('quizView')

    context = {'form': form}
    return render(request, 'project/quizAdd.html', context)

def quizView_page_view(request):
    context = {'answers': Answer.objects.all()}

    return render(request, 'project/quizView.html', context)

def quizAnswer_page_view(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    form = Quiz(request.POST or None, instance=answer)
    context = {'form': form, 'answer_id': answer_id, 'answer': answer}

    return render(request, 'project/quizAnswer.html', context)

def answerCheck_page_view(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    form = Quiz(request.POST or None, instance=answer)
    context = {'form': form, 'answer_id': answer_id}

    return render(request, 'project/answerCheck.html', context)

def commentsView_page_view(request):
    context = {'comments': Comment.objects.all()}

    return render(request, 'project/commentsView.html', context)

def commentsAdd_page_view(request):
    form = Commentary(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('commentsView'))

    context = {'form': form}
    return render(request, 'project/commentsAdd.html', context)

def earth_page_view(request):
    return render(request, 'project/planets/earth.html')

def jupiter_page_view(request):
    return render(request, 'project/planets/jupiter.html')

def mars_page_view(request):
    return render(request, 'project/planets/mars.html')

def mercury_page_view(request):
    return render(request, 'project/planets/mercury.html')

def neptune_page_view(request):
    return render(request, 'project/planets/neptune.html')

def saturn_page_view(request):
    return render(request, 'project/planets/saturn.html')

def sun_page_view(request):
    return render(request, 'project/planets/sun.html')

def uranus_page_view(request):
    return render(request, 'project/planets/uranus.html')

def venus_page_view(request):
    return render(request, 'project/planets/venus.html')
