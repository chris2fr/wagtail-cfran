from content_manager.models import MegaMenu


def skiplinks(request) -> dict:
    return {
        "skiplinks": [
            {"link": "#content", "label": "Contenu"},
            {"link": "#webfastoche-navigation", "label": "Menu"},
        ]
    }


def mega_menus(request) -> dict:
    menus = list(MegaMenu.objects.all().values_list("parent_menu_item_id", flat=True))

    return {"mega_menus": menus}
