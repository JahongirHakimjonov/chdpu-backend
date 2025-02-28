from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.chair import Chair, ChairMember


@register(Chair)
class ChairTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description")


@register(ChairMember)
class ChairMemberTranslationOptions(TranslationOptions):
    fields = ("name", "title", "description")
