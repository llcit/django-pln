from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *

def index(request):
    try:
        apps = App.objects.all().order_by('id')
        types = AppType.objects.all().order_by('id')
        formats = AppFormat.objects.all().order_by('id')
        functions = AppFunction.objects.all().order_by('id')
        prices = AppPrice.objects.all().order_by('id')
        supports = AppSupport.objects.all().order_by('id')
    except App.DoesNotExist:
        raise Http404("Application does not exist.")

    return render(
                request,
                'pln/index.html', {
                    'apps': apps,
                    'types':types,
                    'functions':functions,
                    'formats':formats,
                    'prices':prices,
                    'supports':supports
                }
            )

class AppListView(ListView):
    model = App
    queryset = App.objects.all()

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('pln-list-menu', 'PLN App')
            menu.add_sideframe_item(u'Type List', url=reverse('admin:pln_type_changelist'))
            menu.add_modal_item('Add New PLN App Type', url="%s" % (reverse('admin:pln_type_add'), ))
            menu.add_break()
            menu.add_sideframe_item(u'PLN App List', url=reverse('admin:pln_app_changelist'))
            menu.add_modal_item('Add New App', url="%s" % (reverse('admin:pln_app_add'), ))

        return super(AppListView, self).render_to_response(context, **response_kwargs)

class AppDetailView(DetailView):
    model = App
    context_object_name = 'pln'

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar and self.request.toolbar.edit_mode:
            menu = self.request.toolbar.get_or_create_menu('pln-app-menu', self.object.full_name)
            menu.add_modal_item('Edit %s' % self.object.full_name, url=reverse('admin:pln_app_change', args=[self.object.id]), )
            menu.add_break()

        return super(AppDetailView, self).render_to_response(context, **response_kwargs)
