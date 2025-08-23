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
          O gráfico mostra uma **relação direta entre a carga semanal de estudos e o desempenho acadêmico**. Entre os estudantes que dedicam **poucas horas de estudo**, a concentração maior ocorre em **faixas de notas mais baixas**, indicando que a **limitação no tempo de dedicação pode comprometer o aproveitamento** das disciplinas.

          À medida que avançamos para uma **quantidade intermediária de horas**, a distribuição de notas torna-se mais variada. Embora ainda haja uma **parcela significativa de alunos com desempenho próximo da média**, começam a surgir casos que se destacam **tanto para cima quanto para baixo**.

          Isso sugere que **o aumento de horas não garante, por si só, um bom desempenho**, mas amplia a possibilidade de **resultados diferenciados** dependendo da **qualidade do estudo**, da **organização pessoal** e de fatores individuais como **motivação** e **hábitos de aprendizagem**.
        """)
        st.plotly_chart(study_hours_per_week_cgpa(df))

    with tab2:
        st.subheader("Alunos com Transtornos Mentais Por Cursos")
        st.write("""
          O gráfico evidencia que os cursos da área de **exatas concentram a maior proporção de estudantes que relatam algum tipo de transtorno mental**. Entre eles, o curso de **Engenharia** se destaca de forma expressiva, com **235 registros**, seguido pelo **Bacharelado em Ciência da Computação** (**143**) e pelo **Bacharelado em Tecnologia da Informação** (**92**). Esses números confirmam a tendência já descrita na literatura acadêmica, como no artigo [“Mental health in undergraduate engineering students” (Mirabelli et al., *Journal of Engineering Education*)](https://onlinelibrary.wiley.com/doi/full/10.1002/jee.20551), que aponta elevados níveis de sofrimento psicológico entre estudantes de engenharia, além de barreiras significativas para buscar ajuda. Uma das principais conclusões desse estudo é que a cultura acadêmica em Engenharia tende a **normalizar o estresse e a sobrecarga**, tratando-os como parte natural da formação profissional. Isso contribui para que sintomas de ansiedade, depressão ou exaustão muitas vezes não sejam reconhecidos ou tratados adequadamente.

          Essa concentração nos cursos de exatas pode estar associada a **características típicas desses programas**, como maior carga horária, conteúdos de alta complexidade e longas jornadas de estudo. Tais fatores funcionam como potenciais gatilhos para quadros de ansiedade, depressão e ataques de pânico, transtornos que aparecem com maior frequência no dataset. A intensidade acadêmica, somada à pressão por desempenho, amplia a vulnerabilidade desses estudantes.

          Por outro lado, cursos da área de **humanas e religiosos** também registram transtornos mentais, ainda que em proporções mais reduzidas. Destacam-se **Conhecimento Islâmico e Ciências Humanas** (**39 casos**), **Educação Islâmica** (**37**), **Direito** (**27**), **Ciências Biomédicas** (**26**), **Psicologia** (**26**) e **Jurisprudência Islâmica** (**17**). Embora esses números indiquem menor incidência, não significam ausência de desafios psicológicos. O que se observa é que a **natureza das atividades acadêmicas nesses cursos mais qualitativas e reflexivas pode exercer menor pressão cognitiva e reduzir a intensidade de horas contínuas de estudo**, funcionando como fator atenuante.
        """)

        st.plotly_chart(student_with_mental_issues_by_course(df))

    with tab3:
        st.subheader("Média de Engajamento Acadêmico por Ano de Estudo")
        st.write("""
          A análise dos cursos selecionados revela que o engajamento acadêmico ao longo dos anos não segue uma trajetória linear de crescimento ou queda. Em vez disso, observam-se flutuações que sugerem a influência de fatores específicos de cada etapa, como mudanças no currículo, características das turmas ou até mesmo a complexidade dos conteúdos oferecidos em cada período.

          No **1º ano**, o **Bacharelado em Tecnologia da Informação** apresenta a maior média de engajamento (**3,33**), possivelmente impulsionado pelo entusiasmo inicial dos estudantes diante de conteúdos introdutórios e do contato com temas ligados à tecnologia. Em contraste, o curso de **Engenharia** registra o desempenho mais baixo (**2,85**), o que pode refletir tanto a dificuldade de adaptação dos ingressantes às disciplinas básicas quanto a exigência de uma carga horária intensa já no início da graduação.

          No **2º ano**, observa-se uma melhora significativa no curso de **Engenharia**, com aumento de aproximadamente **12%** em relação ao primeiro ano (**de 2,85 para 3,19**). Esse avanço pode estar associado a um processo de adaptação dos estudantes, que passam a lidar de forma mais estruturada com as demandas do curso, além de terem acesso a matérias mais específicas da área de Engenharia. Já o **Bacharelado em Tecnologia da Informação** mantém uma média elevada (**3,30**), enquanto a **Ciência da Computação** apresenta um leve crescimento (**3,17** em relação a 3,16 no 1º ano).

          No **3º ano**, o **Bacharelado em Tecnologia da Informação** atinge um pico expressivo de engajamento (**3,57**), superando de forma clara os demais cursos. Esse aumento pode estar relacionado ao momento em que os estudantes começam a vivenciar projetos práticos e conteúdos mais aplicados, fortalecendo a conexão entre teoria e prática. Já o curso de **Ciência da Computação** apresenta queda acentuada (**2,77**), o que sugere possíveis dificuldades diante da complexidade dos conteúdos intermediários. A **Engenharia** mantém crescimento moderado (**3,12**).

          No **4º ano**, ocorre uma inversão interessante: a **Engenharia** assume a liderança com engajamento médio de **3,28**, sugerindo que os alunos atingem maior maturidade acadêmica e motivação ao se aproximarem da conclusão do curso. Nesse mesmo período, a **Ciência da Computação** apresenta novamente o resultado mais baixo (**2,77**), o que pode indicar desafios ligados à alta exigência dos conteúdos avançados e à pressão do mercado de trabalho. O **Bacharelado em Tecnologia da Informação** não possui registros no 4º ano nos dados analisados, impossibilitando comparações diretas nesse estágio.
        """)

        st.plotly_chart(academic_engagement_by_year(df))


if __name__ == "__main__":
    main()
