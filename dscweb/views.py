from django.shortcuts import render, get_object_or_404
from .forms import MemberForm
from .models import Member
from .models import Head


def home_view(request):
    members = Member.objects.all()
    heads = Head.objects.all()
    context = {"title": "DSC", "members": members, "heads": heads}
    return render(request, 'home.html', context)


def about_view(request):
    context = {"title": 'About Us'}
    return render(request, 'about.html', context)


def member_detailView(request, first_name):
    member = get_object_or_404(Member, first_name=first_name)
    context = {"member": member}
    return render(request, 'member-view.html', context)
