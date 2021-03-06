import spacy
import re

nlp = spacy.load('de_core_news_sm')

def clean_text(x):
    puncts = [',', '.', '"', ':', ')', '(', '-', '!', '?', '|', ';', "'", '$', '&', '/', '[', ']', '>', '%', '=', '#',
              '*', '+', '\\', '•', '~', '@', '£',
              '·', '_', '{', '}', '©', '^', '®', '`', '<', '→', '°', '€', '™', '›', '♥', '←', '×', '§', '″', '′', 'Â',
              '█', '½', 'à', '…',
              '“', '★', '”', '–', '●', 'â', '►', '−', '¢', '²', '¬', '░', '¶', '↑', '±', '¿', '▾', '═', '¦', '║', '―',
              '¥', '▓', '—', '‹', '─',
              '▒', '：', '¼', '⊕', '▼', '▪', '†', '■', '’', '▀', '¨', '▄', '♫', '☆', 'é', '¯', '♦', '¤', '▲', 'è', '¸',
              '¾', 'Ã', '⋅', '‘', '∞',
              '∙', '）', '↓', '、', '│', '（', '»', '，', '♪', '╩', '╚', '³', '・', '╦', '╣', '╔', '╗', '▬', '❤', 'ï', 'Ø',
              '¹', '≤', '‡', '√', ]

    x = str(x)
    for punct in puncts:
        x = x.replace(punct, f' {punct} ')
    return x


def remove_names(x):
    for word in x.split():
        if word[0] == "@":
            x = x.replace(word, "")
    return x


def entity_recognizing(x):
    doc = nlp(x)
    for ent in doc.ents:
        if ent.label_ == 'PER':
            print(ent.text)
            x = x.replace(ent.text, "name")

    return x


def remove_url(x):
    result = re.sub(r"http\S+", "", x)
    return result


def handle_unicode(x):
    x = x.decode('utf-8')
    return x
