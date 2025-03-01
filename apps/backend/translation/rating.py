from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.rating import Rating


@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ("title", "description")
