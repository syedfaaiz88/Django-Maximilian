from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm
# Create your views here.


class StartingPagePosts(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        querySet = super().get_queryset()
        data = querySet[:3]
        return data


class PostsView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class PostDetailView(View):

    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-date"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/read-later-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
