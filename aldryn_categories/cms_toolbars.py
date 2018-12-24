from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils.urlutils import admin_reverse
from .models import Category

class CategoryToolbar(CMSToolbar):
    supported_apps = (
        'aldryn_categories',
    )

    watch_models = [Category]

    def populate(self):

        menu = self.toolbar.get_or_create_menu('aldryn_categorie-app', _('Categories'))

        menu.add_modal_item(
            name=_('Add new Category'),
            url=admin_reverse('aldryn_categories_category_add'),
        )

        menu.add_sideframe_item(
            name=_('Categories list'),
            url=admin_reverse('aldryn_categories_category_changelist'),
        )



toolbar_pool.register(CategoryToolbar)
