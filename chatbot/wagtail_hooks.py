from wagtail import hooks

from .views import chatbot_viewset

@hooks.register("register_admin_viewset")
def register_viewset():
    return chatbot_viewset
