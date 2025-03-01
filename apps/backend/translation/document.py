from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.document import Document


@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ("title", "description")
