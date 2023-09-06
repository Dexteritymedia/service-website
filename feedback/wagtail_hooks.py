from django.urls import include, path, reverse

from wagtail import hooks 
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem

from feedback import views

reviews_menu = Menu(
    register_hook_name="register_customers_review_menu_item",
    construct_hook_name="construct_customers_review_menu",
)

class ReviewsMenuItem(MenuItem):
    def is_shown(self, request):
        return True


@hooks.register("register_admin_urls")
def register_urls():
    return [
        path("customers-reviews/",
             views.all_reviews,
             name="all_reviews",
            ),
    ]

@hooks.register("register_admin_menu_item")
def register_menu():
    return MenuItem(
        'Reviews',
        reverse('all_reviews'),
        classnames="icon icon-image",
        order=40,
    )

@hooks.register("register_customers_review_menu_item")
def register_menu_item():
    return ReviewsMenuItem(
        'Reviews',
        reverse('all_reviews'),
        classnames="icon icon-image",
        order=185,
    )
