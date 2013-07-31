from django.conf import settings


class BasePaginationMixin(object):

    class Meta:
        abstract = True

    def dispatch(self, request, *args, **kwargs):
        self.max_id = int(request.GET.get('max_id', '0'))
        return super(BasePaginationMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BasePaginationMixin, self).get_context_data(**kwargs)
        if self.max_id == 0:
            context['first_page'] = True
        return context


class MicroBlogPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['MICROBLOG']


class NoteBoardPaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['NOTEBOARD']


class NotePaginationMixin(BasePaginationMixin):

    PAGE_SIZE = settings.PAGE_SIZE['NOTE']
