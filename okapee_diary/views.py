from django.utils import timezone
from .models import Post, Comment #Comment追加
from . import forms #この行追加
from django.shortcuts import render, redirect  # redirect追加

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'okapee_diary/post_list.html', {
        'posts': posts
    })

def article(request, pk):
    article = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=article)

    if request.method == "POST": #入力フォームはPOSTなので
        form = forms.CommentForm(request.POST)
        if form.is_valid(): #もし、formの内容が正しい時は
            comment = form.save(commit=False) #formの内容はまだセーブしません！
            comment.post = article
            comment.author = request.user
            comment.save() #ユーザーを追加したのちにセーブ
    else:
        form = forms.CommentForm()

    print(article)
    return render(request, 'okapee_diary/article.html', {
        'article': article,
        'form': form,
        'comments': comments
    }) #form と comment　を追加

def create_article(request):
    form = forms.PostForm()
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('okapee_diary:article', pk=post.id)

    return render(request, 'okapee_diary/create_article.html', {
        'form': form
    })

def delete_comment(request, pk, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    post_id = pk
    if request.user.id == comment.author.id or \
       request.user.id == comment.post.author.id:
        comment.delete()
    return redirect('okapee_diary:article', pk=post_id)
