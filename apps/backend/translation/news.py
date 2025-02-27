from modeltranslation.translator import TranslationOptions, register

from apps.backend.models.news import News, NewsCategory


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)
