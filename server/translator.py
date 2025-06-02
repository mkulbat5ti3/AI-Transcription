import deepl
from server.config import DEEPL_AUTH_KEY

translator = deepl.Translator(DEEPL_AUTH_KEY)

def translate_text(text, target_lang):
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text
