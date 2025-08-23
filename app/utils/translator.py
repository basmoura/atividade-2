import glob
import os

import streamlit as st
import yaml

SUPPORTED_LANGS = ["pt-BR", "en"]
DEFAULT_LANG = "pt-BR"


@st.cache_data(show_spinner=False)
def load_translations():
    translations = {}
    for path in glob.glob(os.path.join("app", "utils", "i18n", "*.yml")):
        lang = os.path.splitext(os.path.basename(path))[0]
        with open(path, "r", encoding="utf-8") as f:
            translations[lang] = yaml.safe_load(f) or {}

    return translations


TRANSLATIONS = load_translations()


def t(key: str, lang: str) -> str:
    def deep_get(d, dotted_key):
        cur = d
        for part in dotted_key.split("."):
            if not isinstance(cur, dict) or part not in cur:
                return None
            cur = cur[part]
        return cur

    return (
        (deep_get(TRANSLATIONS.get(lang, {}), key))
        or (deep_get(TRANSLATIONS.get("en", {}), key))
        or key
    )


def get_lang_from_query_params():
    qp = st.query_params
    lang = qp.get("lang", DEFAULT_LANG)

    if isinstance(lang, list):
        lang = lang[0] if lang else DEFAULT_LANG
    return lang if lang in SUPPORTED_LANGS else DEFAULT_LANG


def set_lang_query_param(lang: str):
    st.query_params.update({"lang": lang})
