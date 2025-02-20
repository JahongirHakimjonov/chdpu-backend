from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.laboratory import Laboratory


@register(Laboratory)
class LaboratoryTranslationOptions(TranslationOptions):
    fields = ("title", "description")
