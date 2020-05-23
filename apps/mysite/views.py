from django.shortcuts import render, HttpResponse, redirect
from ..message import models as message_models
from . import models as mysite_models


# Create your views here.
def index(request):
    """
    is_index: 是否为首页
    indexes：首页索引

    :param request:
    :return:
    """
    is_index = True
    indexes = 1

    index_page = mysite_models.Page.objects.all()[:6]
    page_num = len(index_page)
    page_dict = dict()
    for i, o in enumerate(index_page, start=1):
        page_dict[i] = o

    return render(request, 'mysite/index.html', locals())


def index_indexes(request, indexes):
    """
    is_index: 是否为首页
    indexes：首页索引

    :param request:
    :return:
    """
    is_index = True

    index_page = mysite_models.Page.objects.all()[indexes * 6 - 6:indexes * 6]
    page_num = len(index_page)
    page_dict = dict()
    for i, o in enumerate(index_page, start=1):
        page_dict[i] = o

    return render(request, 'mysite/index.html', locals())


def last_index(request, indexes):
    if indexes == 1:
        return redirect('/')
    return redirect('/indexes={0}'.format(indexes - 1))


def next_index(request, indexes):
    return redirect('/indexes={0}'.format(indexes + 1))


def page(request, slug):
    pages = mysite_models.Page.objects.get(slug=slug)
    return render(request, 'mysite/page.html', locals())


def message(request):
    messages = message_models.Message.objects.all()
    return render(request, 'mysite/message.html', locals())


def add_message(request):
    username = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    content = request.POST.get('message')
    message_models.Message.objects.create(username=username, email=email, subject=subject, content=content)
    return redirect('/message')
