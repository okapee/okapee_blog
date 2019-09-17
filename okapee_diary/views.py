from django.shortcuts import render


def post_list(request):
    return render(request, 'okapee_diary/post_list.html', {})
