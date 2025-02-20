from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.cooperation import Cooperation


@register(Cooperation)
class CooperationTranslationOptions(TranslationOptions):
    fields = ("title", "description")
