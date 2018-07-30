from django.views.generic import View, TemplateView
from django.http import HttpResponse


class PostListView1(View):
    def get(self, request):
        name = '공유'
        return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬/장고 페이스메이커가 되어드리겠습니다.</p>
        '''.format(name=name))

    def get_templates_string(self, name):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>열심히 하겠습니다.</p>
        '''.format(name=name)


post_list1 = PostListView1.as_view()


class PostList2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context


post_list2 = PostList2.as_view()


class PostList3(View):
    pass


class ExcelDownload(View):
    pass
