from django.conf import settings


class BasePaginationMixin(object):

    class Meta:
        abstract = True

    def dispatch(self, request, *args, **kwargs):
        self.page_base = int(request.GET.get('page', '1')) - 1
        self.start_index = self.page_base * self.PAGE_SIZE
        self.end_index = self.start_index + self.PAGE_SIZE
        return super(BasePaginationMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BasePaginationMixin, self).get_context_data(**kwargs)
        if self.page_base == 0:
            context['first_page'] = True
        return context


class MicroBlogPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['MICROBLOG']
