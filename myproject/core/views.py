from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'object_list': users}
    template_name = 'index.html'
    return render(request, template_name, context)
