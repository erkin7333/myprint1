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
