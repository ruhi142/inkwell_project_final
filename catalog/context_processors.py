from .registry import MENU


def categories_menu(request):
    """Makes the Categories mega-menu data available to every template."""
    return {
        "menu_columns": [c for c in MENU if c["subs"]],
        "menu_links": [c for c in MENU if not c["subs"]],
    }
