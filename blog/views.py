from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects    #쿼리셋
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
# 어떤 클래스로부터 몇번째 것을 받을 건지
    return render(request, 'detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'new.html')
#  단순히 new.html 을 띄워주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

# 문자열 형 변환 이유는 path converter에서 url 은 항상 str형이기 때문에 
#  입력받은 내용을 데이터베이스에 넣어주는 함수
#  사용 상황에 따라서(인자를 뭐를 주느냐에 따라서) redirect or render 로 나뉨

def delete(request, blog_id):
    destroy = get_object_or_404(Blog, pk = blog_id)
    destroy.delete()
    return redirect('home')

def update(request, blog_id):
    updates = get_object_or_404(Blog, pk = blog.id)
    return render(request, 'update.html', {'updates': updates})