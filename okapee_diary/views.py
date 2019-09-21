from django.utils import timezone
from .models import Post, Comment #Comment追加
from . import forms #この行追加
from django.shortcuts import render, redirect  # redirect追加

def post_list(request):
    posts = Post.objects.all()
    form = forms.SearchForm()
    print(request.GET)

    if request.GET.get('q'):
        posts = posts.filter(title__contains = request.GET.get('q')) #titleにqを含む、部分一致検索が可能

    return render(request, 'okapee_diary/post_list.html', {
        'posts': posts,
        'form': form
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

def edit_article(request, pk):
    article = Post.objects.get(id=pk)

    if request.user.id == article.author.id: #if記事の投稿者
        if request.method == "POST":
            form = forms.PostForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
            return redirect('okapee_diary:article', pk=article.id)
        else:
            form = forms.PostForm(instance=article)
            print(form)
    else: #記事の投稿者でないのならば、記事のページに強制的に戻る
        return redirect('okapee_diary:article', pk=article.id)

    return render(request, 'okapee_diary/edit_article.html', {
        'article':article, 'form':form
    })

def delete_article(request, pk):
    article = Post.objects.get(id=pk)

    if request.user.id == article.author.id: #記事の投稿者だけ削除実行できる。
        article.delete()
    return redirect('okapee_diary:post_list')

def delete_comment(request, pk, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    post_id = pk
    if request.user.id == comment.author.id or \
       request.user.id == comment.post.author.id:
        comment.delete()
    return redirect('okapee_diary:article', pk=post_id)
