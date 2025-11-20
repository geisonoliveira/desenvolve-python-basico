import sys

import importlib

# Try to import the external 'emoji' package; if unavailable, use a small local fallback.
emoji = None
try:
    emoji = importlib.import_module('emoji')
except ImportError:
    # Minimal fallback implementation supporting the codes used in this script.
    class _FallbackEmoji:
        def __init__(self):
            self._map = {
                ":joy:": "😂",
                ":heart:": "❤️",
                ":heart_eyes:": "😍",
                ":smile:": "😄",
                ":thumbs_up:": "👍",
            }

        def emojize(self, text, language='alias'):
            # Replace known codes with actual emoji characters.
            for code, ch in self._map.items():
                text = text.replace(code, ch)
            return text

    emoji = _FallbackEmoji()

codes = [":joy:", ":heart:", ":heart_eyes:", ":smile:", ":thumbs_up:"]
print("Lista de emojis disponíveis (código -> emoji):")
for code in codes:
    print(f"{code} -> {emoji.emojize(code, language='alias')}")

frase = input("\nDigite uma frase codificada usando os códigos acima (ex.: Estou feliz :joy:): ").strip()
decodificada = emoji.emojize(frase, language='alias')
print("\nFrase emojizada:")
print(decodificada)
# filepath: c:\Users\Computador\Documents\Projeto Desenvolve\Python\modulo 5\aula1_questao5.py