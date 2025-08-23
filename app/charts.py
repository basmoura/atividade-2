import plotly.express as px

from app.utils.translator import t


def study_hours_per_week_cgpa(df, lang):
    fig = px.scatter(
        df,
        x="StudyHoursPerWeek",
        y="CGPA",
        color="CGPA",
        color_continuous_scale=px.colors.sequential.RdBu,
        size="CGPA",
        height=800,
        title=t("insight_one.chart.title", lang),
    )

    fig.update_traces(hovertemplate=t("insight_one.chart.hover_template", lang))

    fig.update_layout(
        xaxis_title=t("insight_one.chart.xaxis_title", lang),
        yaxis_title=t("insight_one.chart.yaxis_title", lang),
    )

    return fig


def student_with_mental_issues_by_course(df, lang):
    mental_health_issues = df[
        (df["Depression"] == 1) | (df["Anxiety"] == 1) | (df["PanicAttack"] == 1)
    ]
    mental_health_counts = (
        mental_health_issues.groupby("Course").size().reset_index(name="Count")
    )

    data = mental_health_counts.sort_values(by="Count", ascending=False).head(10)

    fig = px.bar(
        data,
        x="Count",
        y="Course",
        orientation="h",
        color="Course",
        color_discrete_sequence=px.colors.cyclical.IceFire,
        text="Count",
        height=800,
        title=t("insight_two.chart.title", lang),
    )

    fig.update_traces(hovertemplate=t("insight_two.chart.hover_template", lang))

    fig.update_layout(
        xaxis_title=t("insight_two.chart.xaxis_title", lang),
        yaxis_title=t("insight_two.chart.xaxis_title", lang),
        showlegend=False,
    )

    return fig


def academic_engagement_by_year(df, lang):
    selected_courses = [
        "Engenharia",
        "Bel. em Tecnologia da Informação",
        "Bel. em Ciência da Computação",
    ]
    filtered_dt = df[df["Course"].isin(selected_courses)]

    avg_academic_engagement_filtered = (
        filtered_dt.groupby(["YearOfStudy", "Course"])["AcademicEngagement"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        avg_academic_engagement_filtered,
        x="YearOfStudy",
        y="AcademicEngagement",
        color="Course",
        title=t("insight_three.chart.title", lang),
        barmode="group",
        custom_data=["Course"],
        height=800,
        color_discrete_sequence=px.colors.cyclical.IceFire,
    )

    fig.update_traces(hovertemplate=t("insight_three.chart.hover_template", lang))

    fig.update_layout(
        xaxis_title=t("insight_three.chart.xaxis_title", lang),
        yaxis_title=t("insight_three.chart.yaxis_title", lang),
        legend_title_text=t("insight_three.chart.legend_title_text", lang),
    )

    return fig
