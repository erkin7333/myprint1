from modeltranslation.translator import TranslationOptions, register
from .models import (Category, Product, About, AboutImage,
                     TypeService, MenuService)
from .help_model import (Designe, DigitalPrint, LargeFormat, TextPrint,
                         LaserPrint, Type)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(AboutImage)
class AboutImageTranslationOptions(TranslationOptions):
    fields = ('name', )



@register(TypeService)
class TypeServiceTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(MenuService)
class MenuServiceTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Designe)
class DesigneTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(DigitalPrint)
class DigitalPrintTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(LargeFormat)
class LargeFormatTranslationOptions(TranslationOptions):
    fields = ('description', 'product_name')



@register(TextPrint)
class TextPrintTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(LaserPrint)
class LaserPrintTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ('name', )





