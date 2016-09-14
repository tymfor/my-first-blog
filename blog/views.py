from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django_tables2 import RequestConfig
from .tables import MeasureTable
import numpy as np
import ast
import pickle
from os.path import *;
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import Post, StructuralMeasures
from . forms import Postform, Viewform, Measuresform
#
# def post_list(request):
#     posts = PostTable(Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date'))
#     RequestConfig(request).configure(posts)
#     return render(request, 'blog/index.html', {'posts':posts})

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = Viewform(instance=post)
    return render(request, 'blog/post_detail3.html',{'form':form,'post': post})
    # return render(request, 'blog/post_detail.html', {'post': post})

def post_about(request):
    return render(request, 'blog/about.html')

def AHP_survey(request):
    return render(request, 'blog/ahp_survey.html')

# @login_required
def post_new(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})

def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def sign_up(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('blog.views.signup_ok')
    elif request.method == "GET":
        userform = UserCreationForm()
    return render(request, "registration/signup.html", {
        "userform": userform,
        })
def signup_ok(request):
    return render(request, "registration/signup_ok.html")

def updating_StructuralMeasures(request):
    db_file = normpath(dirname(abspath(__file__)) + 'DB_criteria.txt');
    f = open(db_file,'rb')
    measures = pickle.load(f)
    f.close()
    return redirect('blog.views.post_list')

def mitigation_measures(request,pk):
    post = get_object_or_404(Post, pk=pk)
    selected_failure_mode = [post.TypeOfMovement,post.Material,post.DepthOfMovement,post.RateOfMovementAtTimeOfWorks,post.Groundwater,post.SurfaceWater]   # size of technical criteria
    category_id = []
    sub_id = []
    sum_tech_criteria = []
    measures = StructuralMeasures.objects.all()
    availabe_measures = []
    for measure in measures:
        selected_tech_criteria = []
        for count,tech_index in enumerate(selected_failure_mode):
            list_criteria = ast.literal_eval(measure.tech_criteria_AtoF)
            selected_tech_criteria.append(list_criteria[count][tech_index-1])
        if not 0 in selected_tech_criteria:
            category_id.append(measure.category_id)
            sub_id.append(measure.sub_id)
            sum_tech_criteria.append(sum(selected_tech_criteria))
            availabe_measures.append(measure)
    post.available_measures_category_id = category_id
    post.available_measures_sub_id = sub_id
    post.available_measures_sum_tech_criteria = sum_tech_criteria
    post.save()
    data_selected = []
    for measure,sum_tech in zip(availabe_measures,sum_tech_criteria):
        data_selected.append({'name': measure.title, 'id': measure.id,'category_id': measure.category_id, 'sub_id': measure.sub_id,'sum': sum_tech})

    table = MeasureTable(data_selected)
    RequestConfig(request).configure(table)
    return render(request, 'blog/suggested_measures.html',{'table':table,'post': post})

def measures_list(request):
    measures = StructuralMeasures.objects.all().order_by('category_id','sub_id')
    page = request.GET.get('page', 1)
    paginator = Paginator(measures, 10)
    try:
        measures = paginator.page(page)
    except PageNotAnInteger:
        measures = paginator.page(1)
    except EmptyPage:
        measures = paginator.page(paginator.num_pages)
    return render(request, 'blog/mitigation_measures.html', {'measures':measures})

def measure_detail(request,pk):
    measure = get_object_or_404(StructuralMeasures, pk=pk)
    return render(request, 'blog/measure_detail.html', {'measure': measure})
