import plotly.express as px


def study_hours_per_week_cgpa(df):
    fig = px.scatter(
        df,
        x="StudyHoursPerWeek",
        y="CGPA",
        color="CGPA",
        color_continuous_scale=px.colors.sequential.RdBu,
        size="CGPA",
        height=800,
        title="Horas de Estudo × Desempenho Acadêmico",
    )

    fig.update_traces(hovertemplate="Horas de Estudo Semanal: %{x}<br>CGPA: %{y}")

    fig.update_layout(xaxis_title="Horas Estudo Semanais", yaxis_title="CGPA")

    return fig


def student_with_mental_issues_by_course(df):
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
        title="Quantidade de Alunos com Transtornos Mentais Por Cursos",
    )

    fig.update_traces(hovertemplate="Quantidade de Alunos: %{x}<br>Curso: %{y}")

    fig.update_layout(
        xaxis_title="Quantidade de Alunos",
        yaxis_title="Curso",
        showlegend=False,
    )

    return fig


def academic_engagement_by_year(df):
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
        title="Engajamento acadêmico: média por ano nos cursos de tecnologia",
        barmode="group",
        custom_data=["Course"],
        height=800,
        color_discrete_sequence=px.colors.cyclical.IceFire,
    )

    fig.update_layout(
        xaxis_title="Ano de Estudo",
        yaxis_title="Média de Engajamento Acadêmico",
        legend_title_text="Curso",
    )

    fig.update_traces(
        hovertemplate="Ano de Estudo: %{x}<br>Média de Engajamento Acadêmico: %{y:.2f}"
    )

    return fig
