from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.students import Student


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ("title", "description")
