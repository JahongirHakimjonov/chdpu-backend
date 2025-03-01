from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.admission import Admission


@register(Admission)
class AdmissionTranslationOptions(TranslationOptions):
    fields = ("title", "description")
