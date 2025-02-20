from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.leadership import Leadership


@register(Leadership)
class LeadershipTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description")
