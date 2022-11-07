from myprint.models import Category, Settings
from myprint.help_model import Type



def all_category(request):
    return {
        "allcategory": Category.objects.filter(parent=None).all(),
        "servicecategory": Type.objects.all(),
        # "phone": Settings.objects.get(key='phone').value,
        # "facebook": Settings.objects.get(key='facebook').value,
        # "instagram": Settings.objects.get(key='instagram').value,
        # "telegram": Settings.objects.get(key='telegram').value
    }


def load_catigories(request):
    categories = Category.objects.filter(parent=None).all()
    children_query = Category.objects.filter(parent_id__in=[k.id for k in categories]).all()
    children = {}

    for child in children_query:
        if child.parent_id not in children:
            children[child.parent_id] = []
        children[child.parent_id].append(child)
    return {
        'categories': categories,
        'categoriy_children': children,
    }
