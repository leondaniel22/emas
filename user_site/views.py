from django.shortcuts import render, redirect
import datetime
from datetime import datetime
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from .forms import *
from nlp_component.models import *
# Create your views here.


def error_category(request):
    """Renders the home page."""
    error_categories = ErrorCategory.objects.all()
    error_appearances = ErrorAppearance.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'user_site/error_category.html',
        {
            'error_categories': error_categories,
            'error_appearances': error_appearances,
            'title': 'Error category',
            'date': datetime.now().date,
        }
    )


def error_appearance(request, location):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    error_appearances = ErrorAppearance.objects.filter(location=location)

    return render(
        request,
        'user_site/error_appearance.html',
        {
            'error_appearances': error_appearances,
            'title': 'Error appearance',
            'date': datetime.now().date,
        }
    )


def solution(request):
    """Renders the home page."""
    solutions = []
    comment_form = RequestCommentForm()
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solutions = Solution.objects.filter(error_appearance=request.POST.get('err_app'))
    else:
        form = SolutionForm()
    return render(
        request,
        'user_site/solution.html',
        {
            'solutions': solutions,
            'comment_form': comment_form,
            'title': 'Solution',
            'date': datetime.now().date,
        }
    )


def success(request):
    if request.method == 'POST':
        form = SuccessForm(request.POST)
        if form.is_valid():
            sol = Solution.objects.get(pk=request.POST.get('sol'))
            sol.rating += 1
            sol.save()
    else:
        form = SuccessForm()
    return redirect('error_category')


def request_comment(request):
    if request.method == 'POST':
        comment_form = RequestCommentForm(request.POST)
        if comment_form.is_valid():
            content = request.POST.get('content')
            err_app = ErrorAppearance.objects.get(pk=request.POST.get('err_app'))
            comment = RequestComment(content=content, error_appearance=err_app)
            comment.save()
    else:
        comment_form = RequestCommentForm()
    return redirect('error_category')


def edit_comment(request):
    if request.method == 'POST':
        comment_form = EditCommentForm(request.POST)
        if comment_form.is_valid():
            content = request.POST.get('content')
            sol = Solution.objects.get(pk=request.POST.get('sol'))
            comment = EditComment(content=content, solution=sol)
            comment.save()
    else:
        comment_form = EditCommentForm()
    return redirect('error_category')