from django.shortcuts import render_to_response
from Main.models import DeathBlog


def index(request):
      return render_to_response('C:/Users/Drew/sites/DrewGraham/Main/templates/index.html', {
        'post': DeathBlog.objects.all()[:5]
    })