from modeltranslation.translator import register, TranslationOptions

from .models import ExamModel


@register(ExamModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
