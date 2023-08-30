from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import WorkPage, WorkIndexPage

class WorkPageAdmin(ModelAdmin):
    model = WorkPage
    menu_label = 'Partners Work'
    menu_icon = 'cogs'
    menu_order = 80
    add_to_settings_menu = False
    exclude_from_explorer = False

    
class WorkIndexPageAdmin(ModelAdmin):
    model = WorkIndexPage
    menu_label = 'Work'
    menu_icon = 'cog'
    menu_order = 75
    add_to_settings_menu = False
    exclude_from_explorer = False

    
modeladmin_register(WorkPageAdmin)
modeladmin_register(WorkIndexPageAdmin)

