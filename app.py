import streamlit as st

from app.charts import (
    academic_engagement_by_year,
    student_with_mental_issues_by_course,
    study_hours_per_week_cgpa,
)
from app.data import load


def main():
    st.set_page_config(page_title="Atividade II - Análise de Dados", layout="wide")
    df = load()

    st.title("Atividade II - Análise de Dados")
    st.header(
        "Análise Explanatória do dataset utilizado na Atividade 01", divider="grey"
    )
    st.markdown("""
    *Durante a atividade 01 vocês apresentaram insights e explorações sobre o conjunto de dados, que tal agora apresentar os motivos destas terem acontecidos?*")

    *O desafio desta vez é **EXPLICAR** os motivos de três insights apresentados, baseado em dados e figuras com annotations plots. É uma análise mais detalhada, adicioando motivos à exploração.*
    """)

    st.markdown("""
    ## Informações sobre o Dataset

    O conjunto de dados utilizado neste projeto foi coletado por meio de uma pesquisa realizada no **Google Forms** com estudantes universitários da Malásia. O objetivo da pesquisa foi analisar a situação acadêmica atual dos estudantes e os impactos relacionados à saúde mental.

    As informações abrangem estudantes de diferentes **idades, gêneros, cursos e anos letivos**, incluindo aqueles que apresentam ou não algum tipo de transtorno mental, como **depressão, ansiedade ou ataques de pânico**. Além disso, o dataset traz dados sobre **qualidade do sono, níveis de estresse, engajamento acadêmico, carga horária semanal de estudos** e informações sobre **suporte disponível em episódios de transtornos mentais**, como acompanhamento especializado.

    *Fonte: [https://www.kaggle.com/datasets/junnn0126/university-students-mental-health](https://www.kaggle.com/datasets/junnn0126/university-students-mental-health)*

    ### Estrutura do Dataset

    O dataset é composto por **16 colunas**, distribuídas da seguinte forma:

    - **11 colunas do tipo `int64`**
    - **1 coluna do tipo `float64`**
    - **4 colunas do tipo `string`**

    Em relação à qualidade dos dados, o dataset **não apresenta valores nulos**, mas contém alguns registros **inválidos, duplicados ou com espaços em branco**.

    ### Necessidade de Tratamento dos Dados

    Para possibilitar análises mais consistentes, algumas inconsistências precisam ser corrigidas:

    - **Ano letivo:** há múltiplas formas de representação da mesma informação, como *“Year 3”* e *“year 3”*.
    - **Cursos:** alguns aparecem abreviados, sugerindo indevidamente que se tratam de cursos distintos. Por exemplo, o curso *“Engineering”* também é representado como *“Engine”* e *“Engin”*.

    Esses ajustes são fundamentais para garantir a **padronização** e a **confiabilidade** das análises subsequentes.
    """)

    st.header("Insights", divider="gray")

    tab1, tab2, tab3 = st.tabs(
        [
            "P1. Análise Explanatória Insight #1",
            "P2. Análise Explanatória Insight #2",
            "P3. Análise Explanatória Insight #3",
        ]
    )

    with tab1:
        st.subheader(
            "Impacto da Quantidade de Horas de Estudo Por Semana no Desempenho Estudantil"
        )
        st.write("""
        O gráfico mostra uma relação direta entre a carga semanal de estudos e o desempenho acadêmico. Entre os estudantes que dedicam poucas horas de estudo, a concentração maior ocorre em faixas de notas mais baixas, indicando que a limitação no tempo de dedicação pode comprometer o aproveitamento das disciplinas.

        À medida que avançamos para uma quantidade intermediária de horas, a distribuição de notas torna-se mais variada. Embora ainda haja uma parcela significativa de alunos com desempenho próximo da média, começam a surgir casos que se destacam tanto para cima quanto para baixo.

        Isso sugere que o aumento de horas não garante, por si só, um bom desempenho, mas amplia a possibilidade de resultados diferenciados dependendo da qualidade do estudo, da organização pessoal e de fatores individuais como motivação e hábitos de aprendizagem.
        """)
        st.plotly_chart(study_hours_per_week_cgpa(df))

    with tab2:
        st.subheader("Alunos com Transtornos Mentais Por Cursos")
        st.write("""
        O gráfico evidencia que os cursos da área de exatas concentram a maior proporção de estudantes que relatam algum tipo de transtorno mental. Entre eles, o curso de Engenharia se destaca de forma expressiva, seguido pelo Bacharelado em Ciência da Computação e pelo Bacharelado em Tecnologia da Informação. O artigo [“Mental health in undergraduate engineering students” (Mirabelli et al., publicado na Journal of Engineering Education)](https://onlinelibrary.wiley.com/doi/full/10.1002/jee.20551) mostra que estudantes de engenharia apresentam níveis elevados de  sofrimento     psicológico e enfrentam barreiras significativas para buscar ajuda. Uma das principais conclusões é que a cultura acadêmica em engenharia normaliza o estresse e a sobrecarga, tratando-os como parte natural da formação profissional. Isso faz com que sintomas de ansiedade, depressão ou exaustão muitas vezes não sejam reconhecidos ou tratados adequadamente

        Essa concentração pode estar associada a características típicas desses cursos: maior carga horária, conteúdos de alta complexidade e a exigência de longas jornadas de estudo. Tais fatores funcionam como potenciais gatilhos para quadros de ansiedade, depressão ou ataques de pânico, que são os transtornos identificados no dataset. A intensidade acadêmica, somada à pressão por desempenho, pode amplificar a vulnerabilidade desses estudantes.

        Por outro lado, os cursos da área de humanas e religiosos também apresentam presença de transtornos mentais, mas em proporções mais reduzidas. Isso não significa ausência de desafios psicológicos, mas sugere que a natureza das atividades acadêmicas nesses campos que são frequentemente mais qualitativas e reflexivas e isso pode exercer menor pressão em termos de carga cognitiva intensa e horas de estudo contínuo.
        """)

        st.plotly_chart(student_with_mental_issues_by_course(df))

    with tab3:
        st.subheader("Média de Engajamento Acadêmico por Ano de Estudo")
        st.write("""
        A análise dos cursos selecionados revela que o engajamento acadêmico ao longo dos anos não segue uma trajetória linear de crescimento ou queda. Em vez disso, observam-se flutuações que sugerem a influência de fatores específicos de cada etapa, como mudanças no currículo, características das turmas ou até mesmo a complexidade dos conteúdos oferecidos em cada período.

        No 1º ano, o Bacharelado em Tecnologia da Informação se destaca com a maior média de engajamento, possivelmente impulsionado pelo entusiasmo inicial dos estudantes diante de conteúdos introdutórios e do contato com temas ligados à tecnologia. Em contraste, o curso de Engenharia apresenta o desempenho mais baixo, o que pode refletir tanto a dificuldade de adaptação dos ingressantes às disciplinas básicas quanto a exigência de uma carga horária intensa já no início da graduação.

        No 3º ano, o Bacharelado em Tecnologia da Informação atinge um pico expressivo de engajamento, superando de forma notável os demais cursos. Esse aumento pode estar relacionado ao momento em que os estudantes começam a vivenciar projetos práticos e conteúdos mais aplicados, que fortalecem a conexão entre teoria e prática e elevam o envolvimento.

        Já no 4º ano, ocorre uma inversão interessante: o curso de Engenharia assume a liderança em engajamento médio, sugerindo que os alunos atingem maior maturidade acadêmica e motivação ao se aproximarem da conclusão do curso. Nesse mesmo período, o Bacharelado em Ciência da Computação apresenta o menor resultado, o que pode indicar dificuldades ligadas à complexidade dos conteúdos avançados ou à pressão do mercado de trabalho, que se intensifica no final da graduação.
        """)

        st.plotly_chart(academic_engagement_by_year(df))


if __name__ == "__main__":
    main()
