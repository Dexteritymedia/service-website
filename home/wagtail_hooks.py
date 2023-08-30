from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import HomePage, Service, ServicePage, StaticPage, FormPage

#to change the name "Snippets" to Overview in wagtail admin sidebar
@hooks.register('construct_main_menu')
def change_page_name(request, menu_items):
    for item in menu_items:
        if item.__class__.__name__=='SnippetsMenuItem':
            item.label = 'Snippets'

#hide the help page from main menu
@hooks.register("construct_main_menu")
def hide_help_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "help"]

#hide the explorer/pages/overview page from main menu
@hooks.register("construct_main_menu")
def hide_help_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "explorer"]

#hide the locked page from reports submenu
@hooks.register("construct_reports_menu")
def hide_help_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "locked-pages"]

#hide the sites page from settings submenu
@hooks.register("construct_settings_menu")
def hide_help_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "sites"]

#hide the redirect page from settings submenu
@hooks.register("construct_settings_menu")
def hide_help_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "redirects"]
    
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

class FormPageAdmin(ModelAdmin):
    model = FormPage
    menu_label = 'Testimonial & Contact'
    menu_icon = 'list-ul'
    menu_order = 150
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

from wagtail.admin.views.account import BaseSettingsPanel
from .forms import CustomProfileSettingsForm

@hooks.register('register_account_settings_panel')
class CustomSettingsPanel(BaseSettingsPanel):
    name = 'custom'
    title = "Additional Info"
    order = 500
    form_class = CustomProfileSettingsForm
    form_object = 'profile'

modeladmin_register(HomePageAdmin)
modeladmin_register(ServicePageAdmin)
modeladmin_register(FormPageAdmin)
modeladmin_register(ServiceDetailPageAdmin)
modeladmin_register(StaticPageAdmin)
