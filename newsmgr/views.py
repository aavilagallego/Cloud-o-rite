# Create your views here.
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from newsmgr.models import News
from urlparse import urlparse
from newsmgr.forms import AddLinkForm


# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def home(request):
    latest_news = News.objects.all().order_by('-datep')
    print "I'm here"
    return render(request, 'newsmgr/templates/news.html', { 'page_title'   : "This links are my cloudorites!",'latest_news'  : latest_news, })

def addnew(request):
    if request.method == 'POST':
        form = AddLinkForm(request.POST)
        if not form.is_valid():
            return render(request, 'newsmgr/templates/news.html', { 'page_title' : 'Form Not Valid'} )

        n = News(url=form.cleaned_data['ilink'], title=form.cleaned_data['ititle'], taglist=form.cleaned_data['itags']);
        n.date = timezone.now();
        n.votes=1
        n.spam=0
        n.status='N'
        n.datep=None
        n.user_id=0
        n.save()
        
        tags = n.tags.split('.');
        for tag in tags:
            tag = tag.strip()
            if Tags.filter(name=tag).exists():
                continue
            tg = Tags(name=tag)
            tg.save()

        return render(request, 'newsmgr/templates/news.html', { 'page_title' : 'ok'} )
    else:
        return render(request, 'newsmgr/templates/news.html', { 'page_title' : 'No post found'} )


