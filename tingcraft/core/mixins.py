class OwnerContextMixin(object):

    def dispatch(self, request, *args, **kwargs):
        self.owner_username = kwargs['username']
        return super(OwnerContextMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OwnerContextMixin, self).get_context_data(**kwargs)
        context['owner_username'] = self.owner_username
        return context
