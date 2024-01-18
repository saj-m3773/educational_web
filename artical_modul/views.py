from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from artical_modul.models import Article, ArticleComment, ArticaleTag


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'article_module/articles_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        tags = self.kwargs.get('tags')
        if tags is not None:
            query = query.filter(tags__slug__iexact=tags)
        return query


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_module/article_pag_detale.html'

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query

    def get_context_data(self, **kwargs):  

        context = super(ArticleDetailView, self).get_context_data()
        article: Article = kwargs.get('object')
        context['comments'] = ArticleComment.objects.filter(article_id=article.id, parent=None).order_by(
            '-create_date').prefetch_related('articlecomment_set')
        context['comments_count'] = ArticleComment.objects.filter(article_id=article.id).count()
        context['tags'] = ArticaleTag.objects.all().filter(articales=article)
        return context


def add_article_comment(request: HttpRequest):
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = ArticleComment(article_id=article_id, text=article_comment, user_id=request.user.id,
                                     parent_id=parent_id, is_active=False)
        new_comment.save()
        context = {
            'comments': ArticleComment.objects.filter(article_id=article_id, parent=None, is_active=False).order_by(
                '-create_date').prefetch_related('articlecomment_set'),
            'comments_count': ArticleComment.objects.filter(article_id=article_id, is_active=True).count()
        }

        return render(request, 'article_module/article_pag_detale.html', context)

    return JsonResponse({
        'status': 'success',
        'text': ' نظر شما پس از تایید نمایش داده می شود',
        'confirm_button_text': 'باشه ممنونم',
        'icon': 'success'
    })
