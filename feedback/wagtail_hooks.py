from django.urls import include, path, reverse

from wagtail import hooks 
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem

from feedback import views

@hooks.register("register_admin_urls")
def register_urls():
    return [
        path("customers-reviews/",
             views.all_reviews,
             name="all-reviews",
            ),
        path("calendar/",
             views.calendar_index,
             name="calendar",
            ),
        path("calendar/month/",
             views.calendar_month,
             name="calendar-month",
            ),
        path("search/calendar/",
             views.search_calendar,
             name="search-calendar",
            ),
    ]

@hooks.register("register_admin_menu_item")
def register_menu():
    return MenuItem(
        'Reviews',
        reverse('all-reviews'),
        classnames="icon icon-image",
        order=40,
    )

@hooks.register("register_admin_menu_item")
def register_calendar_menu_items():
    submenu = Menu(items=[
        MenuItem(
            'Calendar',
            reverse('calendar'),
            classnames="icon icon-user",
            icon_name="date",
            order=10,
        ),
        MenuItem(
            'Current month',
            reverse('calendar-month'),
            icon_name="date",
            order=5,
        ),
        MenuItem(
            'Search calendar',
            reverse('search-calendar'),
            icon_name="search",
            order=2,
        ),
    ])

    return SubmenuMenuItem('Calendar', submenu, order=10, icon_name='date')

"""
reviews_menu = Menu(
    register_hook_name="register_customers_review_menu_item",
    construct_hook_name="construct_customers_review_menu",
)

class ReviewsMenuItem(MenuItem):
    def is_shown(self, request):
        return True

    
@hooks.register("register_customers_review_menu_item")
def register_menu_item():
    return ReviewsMenuItem(
        'Reviews',
        reverse('all_reviews'),
        classnames="icon icon-image",
        order=185,
    )
"""
