import re
import spacy
from transformers import pipeline

# 1. SpaCy modelini yuklab olamiz (masalan, "en_core_web_sm" yoki o'zingizga mos model)
# Agar siz boshqa til uchun model kerak bo'lsa, shunga mos modelni yuklab oling.
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    # Agar model mavjud bo'lmasa, avtomatik yuklab olish mumkin
    import os

    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# 2. Hugging Face dan maxsus haqorat aniqlash modelini yuklab olamiz.
# model_name o'zingizning maxsus model ismingiz bo'lishi mumkin.
model_name = "your-custom-insult-model"  # O'zingizning modelingizni kiriting
classifier = pipeline("text-classification", model=model_name, tokenizer=model_name)


def extract_context_spacy(text, target_word, window=5):
    """
    SpaCy yordamida matnni tokenlarga ajratib, target_word atrofidagi kontekstni oladi.
    window parametri target_word dan oldin va keyin nechta token olishni belgilaydi.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc]

    # Target so'zni aniq moslash uchun pastki harflarga o'tkazamiz
    target_lower = target_word.lower()
    contexts = []

    for i, token in enumerate(doc):
        # To'liq so'z tengligi: punktuatsiya va boshqa belgilar hisobga olinmagan holda
        if token.text.lower() == target_lower:
            start = max(i - window, 0)
            end = min(i + window + 1, len(doc))
            # Kontekstni qayta tiklash: asl matn shaklida
            context = " ".join([doc[j].text for j in range(start, end)])
            contexts.append(context)
    return contexts


def is_insult_usage(text, target_word="ko't", threshold=0.5, window=5):
    """
    Matnda target_word ning haqoratli ma'noda ishlatilganligini aniqlaydi.
    1. Regex bilan matnda target_word mavjudligini tekshiradi.
    2. SpaCy tokenizatsiyasi yordamida target_word atrofidagi kontekstlarni ajratib oladi.
    3. Har bir kontekst uchun NLP model yordamida baholaydi.
    Agar model hech bo'lmaganda bitta kontekstda "INSULT" yorlig'ini threshold dan yuqori ishonch bilan qaytarsa, True qaytaradi.
    """
    # Regex: so‘z chegaralari (\b) bilan tekshirish
    pattern = re.compile(r"\b" + re.escape(target_word) + r"\b", re.IGNORECASE)
    if not pattern.search(text):
        return False  # target_word matnda mavjud emas

    contexts = extract_context_spacy(text, target_word, window=window)
    for context in contexts:
        result = classifier(context)[0]
        label = result.get("label", "")
        score = result.get("score", 0)

        # Model "INSULT" yorlig'ini qaytargan holatda va yuqori ishonch bo'lsa haqorat deb hisoblaymiz.
        if label.upper() == "INSULT" and score >= threshold:
            return True
    return False


# Misol matnlar:
texts = [
    "Uning gaplari juda ko't, hech kimga yoqmaydi.",  # Ehtimol haqoratli kontekst
    "Bu mashina ko'tarilish jarayonini tezlashtiradi.",  # Boshqa ma'noda
]

for txt in texts:
    result = is_insult_usage(txt)
    print(f"Matn: {txt}\nHaqqoratli: {result}\n{'-' * 60}")
