from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.chair import Chair


@register(Chair)
class ChairTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description")
