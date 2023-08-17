from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import HomePage, Service, ServicePage, StaticPage

#to change the name "Snippets" to Overview in wagtail admin sidebar
@hooks.register('construct_main_menu')
def change_page_name(request, menu_items):
    for item in menu_items:
        if item.__class__.__name__=='SnippetsMenuItem':
            item.label = 'Snippets'

@hooks.register("construct_settings_menu")
def hide_main_menu_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "main-menu"]

#to change the name "Pages" to Overview in wagtail admin sidebar
@hooks.register('construct_main_menu')
def change_page_name(request, menu_items):
    for item in menu_items:
        if item.__class__.__name__=='ExplorerMenuItem':
            item.label = 'Overview'

class HomePageAdmin(ModelAdmin):
    model = HomePage
    menu_label = 'Homepage'
    menu_icon = 'home'
    menu_order = 90
    add_to_settings_menu = False
    exclude_from_explorer = False

class ServicePageAdmin(ModelAdmin):
    model = Service
    menu_label = 'Services'
    menu_icon = 'plus-inverse'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False

class ServiceDetailPageAdmin(ModelAdmin):
    model = ServicePage
    menu_label = 'Products & Services'
    menu_order = 170
    menu_icon = 'doc-empty-inverse'
    list_display = ('title', 'slug', 'latest_revision_created_at')
    list_filter = ('title', 'latest_revision_created_at')
    search_fields = ('title', 'body', 'latest_revision_created_at')


class StaticPageAdmin(ModelAdmin):
    model = StaticPage
    menu_label = 'Other Pages'
    menu_order = 190
    menu_icon = 'pilcrow'
    list_display = ('title', 'slug', 'latest_revision_created_at')
    list_filter = ('title', 'latest_revision_created_at')
    search_fields = ('title', 'body', 'latest_revision_created_at')

modeladmin_register(HomePageAdmin)
modeladmin_register(ServicePageAdmin)  
modeladmin_register(ServiceDetailPageAdmin)
modeladmin_register(StaticPageAdmin)
