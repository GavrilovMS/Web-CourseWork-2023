from django.views.generic import TemplateView, ListView, DetailView

from .models import HomePage, AboutPage, News, ContactPage

class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = HomePage.objects.first()
        return context

class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_page'] = AboutPage.objects.first()
        return context

class NewsListView(ListView):
    template_name = 'blog/news_list.html'
    model = News

class NewsDetailView(DetailView):
    template_name = 'blog/news_detail.html'
    model = News

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_page'] = ContactPage.objects.first()
        return context
