import streamlit as st

from app.charts import (
    academic_engagement_by_year,
    student_with_mental_issues_by_course,
    study_hours_per_week_cgpa,
)
from app.data import load
from app.utils.translator import (
    get_lang_from_query_params,
    set_lang_query_param,
    t,
)


def main():
    if "lang" not in st.session_state:
        st.session_state.lang = get_lang_from_query_params()

    lang = st.session_state.lang

    with st.sidebar:
        st.markdown("### " + t("nav.lang", lang))
        label_pt = t("lang.pt-BR", lang)
        label_en = t("lang.en", lang)
        shown = st.radio(
            label=t("nav.radio.label", lang),
            options=[label_pt, label_en],
            index=0 if lang == "pt-BR" else 1,
            horizontal=True,
        )
        new_lang = "pt-BR" if shown == label_pt else "en"
        if new_lang != lang:
            st.session_state.lang = new_lang
            set_lang_query_param(new_lang)
            st.rerun()

    st.set_page_config(page_title=t("app.title", lang), layout="wide")
    df = load()

    st.title(t("app.title", lang))
    st.markdown(t("activity.title", lang))
    st.markdown(t("activity.description", lang))

    st.markdown(t("dataset.content", lang))

    st.header("Insights", divider="gray")

    tab1, tab2, tab3 = st.tabs(
        [
            t("insight_one.tab.title", lang),
            t("insight_two.tab.title", lang),
            t("insight_three.tab.title", lang),
        ]
    )

    with tab1:
        st.subheader(t("insight_one.title", lang))
        st.write(t("insight_one.summary", lang))
        st.plotly_chart(study_hours_per_week_cgpa(df, lang))

    with tab2:
        st.subheader(t("insight_two.title", lang))
        st.write(t("insight_two.summary", lang))

        st.plotly_chart(student_with_mental_issues_by_course(df, lang))

    with tab3:
        st.subheader(t("insight_three.title", lang))
        st.write(t("insight_three.summary", lang))

        st.plotly_chart(academic_engagement_by_year(df, lang))


if __name__ == "__main__":
    main()
