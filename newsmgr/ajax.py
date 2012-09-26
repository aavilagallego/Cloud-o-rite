from django.template import Context, loader
from django.http import HttpResponse
from django.utils import simplejson
from newsmgr.models import Links, Users


def voteForNew(request, newid, user ):
    u = Users.objects.get(name=user)
    n = Links.objects.get(id=newid)
    v = Votes(n.id, n.newid)
    v.save()
    n.votes = n.votes+1;
    n.save()
    return simplejson.dumps({'votes':n.votes, 'action':'ok'})

#def addNew(request, userid):

