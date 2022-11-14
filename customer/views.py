from django.shortcuts import render

# Create your views here.
def jquery1(request):
     return render(request, 'customer_templates/jquery.html')


def test(request):
     return render(request, 'customer_templates/test.html')


def join_now(request):
      return render(request, 'customer_templates/join_now.html')


def sign_in(request):
      return render(request,'customer_templates/sign_in.html')


def post_job(request):
      return render(request,'customer_templates/post_job.html')

def get_started(request):
      return render(request,'customer_templates/get_started.html')