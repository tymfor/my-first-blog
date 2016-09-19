from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django_tables2 import RequestConfig
from .tables import MeasureTable_wo_constraints,MeasureTable_w_constraints

import numpy as np
import pickle
import json

from os.path import *;
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decision_making import *
from .ahp_process_for_constrains import *

from . models import Post, StructuralMeasures
from . forms import Postform, Viewform, Measuresform, Constraintform


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

def mitigation_measures(request,pk):
    post = get_object_or_404(Post, pk=pk)
    selected_failure_mode = [post.TypeOfMovement,post.Material,post.DepthOfMovement,post.RateOfMovementAtTimeOfWorks,post.Groundwater,post.SurfaceWater]   # size of technical criteria
    measures = StructuralMeasures.objects.all()
    post = available_measures(selected_failure_mode,measures,post)
    post.save()
    criteria_weights = weights_of_criteria(post)
    weight_sum_constraints = AHP_process(post.available_measures.all(),criteria_weights)
    post.available_measures_ahp_sume_peform_criteria = weight_sum_constraints
    post.save()
    data_selected = []
    name = []
    tech_score = []
    constraints_score = []
    for measure,weight_sum in zip(post.available_measures.all(),weight_sum_constraints):
        score = scores(selected_failure_mode,measure)
        name.append( measure.title)
        tech_score.append(sum(score))
        data_selected.append({'name': measure.title, 'id': measure.id,'category_id': measure.category_id,'sum': sum(score),'constraints_score': "{0:.3f}".format(round(weight_sum,2))})
    if all(x==criteria_weights[0] for x in criteria_weights):
        table = MeasureTable_wo_constraints(data_selected)
    else:
        table = MeasureTable_w_constraints(data_selected)
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

def constraints_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Constraintform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.mitigation_measures',pk=post.pk)
    else:
        form = Constraintform(instance=post)
    return render(request, 'blog/add_constraints.html',{'form':form})
