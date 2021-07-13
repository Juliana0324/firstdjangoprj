from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from .models import Post
from django.utils import timezone
from blog.forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request,pk): 
    # 글을 수정해야하기 떄문에 기존에 입력되어 있는 자료를 가져오는게 먼저임
    post = get_object_or_404(Post, pk=pk)    
    # get 방식 post방식 구분
    if request.method == "POST":
        # post방식인 경우는 기존 자료 post에 새로들어온 정보를 덮어 씌움
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            # published_date를 다시 현재 서버시간으로 변경
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #만약 post방식이 아닌 경우라면 get방식임으로 수정직전임
        # 따라서 폼으로 다시 연결해줘야함, 이때의 폼은 수정용 폼이고 
        # 수정용 폼에는 기존에 써놨던 글이 먼저 입력되어 있어야함으로
        # 감안해서 기존 글의 내용이 담겨있는 post를 촘에 instance로 넘겨줌
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html',{'form':form})