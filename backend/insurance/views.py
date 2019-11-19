from django.shortcuts import render, redirect
from .models import Member, Dependent
from .forms import MemberForm, DependentForm


def member_list(request):
    members = Member.objects.all()
    return render(request, 'insurance/member_list.html', {'members': members})


def member_detail(request, pk):
    member = Member.objects.get(id=pk)
    return render(request, 'insurance/member_detail.html', {'member': member})



def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = MemberForm()
    return render(request, 'insurance/member_form.html', {'form': form})



def member_edit(request, pk):
    member = Member.objects.get(pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)
    return render(request, 'insurance/member_formƒ.html', {'form': form})



def member_delete(request, pk):
    Member.objects.get(id=pk).delete()
    return redirect('member_list')


def dependent_list(request):
    dependents = Dependent.objects.all()
    return render(request, 'insurance/dependent_list.html', {'dependents': dependents})


def dependent_detail(request, pk):
    dependent = Dependent.objects.get(id=pk)
    return render(request, 'insurance/dependent_detail.html', {'dependent': dependent})



def dependent_create(request):
    if request.method == 'POST':
        form = DependentForm(request.POST)
        if form.is_valid():
            dependent = form.save()
            return redirect('dependent_detail', pk=dependent.pk)
    else:
        form = DependentForm()
    return render(request, 'insurance/dependent_form.html', {'form': form})



def dependent_edit(request, pk):
    dependent = Dependent.objects.get(pk=pk)
    if request.method == "POST":
        form = DependentForm(request.POST, instance=dependent)
        if form.is_valid():
            member = form.save()
            return redirect('dependent_detail', pk=dependent.pk)
    else:
        form = DependentForm(instance=dependent)
    return render(request, 'insurance/dependent_form.html', {'form': form})



def dependent_delete(request, pk):
    Dependent.objects.get(id=pk).delete()
    return redirect('dependent_list')


def about(request):
    return render(request, 'insurance/about.html')
