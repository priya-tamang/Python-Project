from googletrans import Translator, constants
from pprint import pprint

translator = Translator()

translation = translator.translate("Hello", dest="ne")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
