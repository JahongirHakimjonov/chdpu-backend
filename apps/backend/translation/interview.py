from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.interview import Interview


@register(Interview)
class InterviewTranslationOptions(TranslationOptions):
    fields = ("title", "description")
