from langdetect import detect
import langcodes
from transformers import MarianMTModel, MarianTokenizer
from tqdm import tqdm

def detect_and_translate(text):
    lang_code = detect(text)
    lang_name = langcodes.get(lang_code).display_name()
    print(f"Detected Language: {lang_name} ({lang_code})")

    if lang_code == "en":
        print("Already in English. No translation needed.")
        return text

    model_name = f"Helsinki-NLP/opus-mt-{lang_code}-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    chunks = [text[i:i+400] for i in range(0, len(text), 400)]
    translated_chunks = []
    for chunk in tqdm(chunks, desc="Translating"):
        tokens = tokenizer([chunk], return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**tokens)
        translated_chunks.append(tokenizer.decode(translated[0], skip_special_tokens=True))

    translated = " ".join(translated_chunks)
    print(f"Translated: {translated}")
    return translated

a = detect_and_translate(full_text)
print(a)
