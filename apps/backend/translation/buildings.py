from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.buildings import Building


@register(Building)
class BuildingTranslationOptions(TranslationOptions):
    fields = ("title", "description")
