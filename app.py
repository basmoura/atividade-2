import streamlit as st
import plotly.express as px

from lib.data import load

def main():
  st.set_page_config(page_title="Meu App", layout="wide")
  df = load()

  st.title("Atividade II - Análise de Dados")
  st.header("Análise Explanatória do dataset utilizado na Atividade 01", divider="grey")
  st.markdown('''
    *Durante a atividade 01 vocês apresentaram insights e explorações sobre o conjunto de dados, que tal agora apresentar os motivos destas terem acontecidos?*")

    *O desafio desta vez é **EXPLICAR** os motivos de três insights apresentados, baseado em dados e figuras com annotations plots. É uma análise mais detalhada, adicioando motivos à exploração.*
  ''')

  st.markdown('''
    ## Informações sobre o Dataset

    O conjunto de dados utilizado neste projeto foi coletado por meio de uma pesquisa realizada no **Google Forms** com estudantes universitários da Malásia. O objetivo da pesquisa foi analisar a situação acadêmica atual dos estudantes e os impactos relacionados à saúde mental.

    As informações abrangem estudantes de diferentes **idades, gêneros, cursos e anos letivos**, incluindo aqueles que apresentam ou não algum tipo de transtorno mental, como **depressão, ansiedade ou ataques de pânico**. Além disso, o dataset traz dados sobre **qualidade do sono, níveis de estresse, engajamento acadêmico, carga horária semanal de estudos** e informações sobre **suporte disponível em episódios de transtornos mentais**, como acompanhamento especializado.

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

    *Fonte: [https://www.kaggle.com/datasets/junnn0126/university-students-mental-health](https://www.kaggle.com/datasets/junnn0126/university-students-mental-health)*
    ''')

  st.header("Insights", divider="gray")
  st.subheader("P1. Análise Explanatória Insight #1")
  st.write("**Impacto da Quantidade de Horas de Estudo Por Semana no Desempenho Estudantil**")
  st.write('''
    O gráfico mostra uma relação direta entre a carga semanal de estudos e o desempenho acadêmico. Entre os estudantes que dedicam poucas horas de estudo, a concentração maior ocorre em faixas de notas mais baixas, indicando que a limitação no tempo de dedicação pode comprometer o aproveitamento das disciplinas.

    À medida que avançamos para uma quantidade intermediária de horas, a distribuição de notas torna-se mais variada. Embora ainda haja uma parcela significativa de alunos com desempenho próximo da média, começam a surgir casos que se destacam tanto para cima quanto para baixo.

    Isso sugere que o aumento de horas não garante, por si só, um bom desempenho, mas amplia a possibilidade de resultados diferenciados dependendo da qualidade do estudo, da organização pessoal e de fatores individuais como motivação e hábitos de aprendizagem.
    ''')
  fig = px.scatter(df, x="StudyHoursPerWeek", y="CGPA", color="CGPA",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size='CGPA',
    height=800,
    title="Horas de Estudo × Desempenho Acadêmico")

  fig.update_traces(hovertemplate='Horas de Estudo Semanal: %{x}<br>CGPA: %{y}')

  fig.update_layout(
    xaxis_title="Horas Estudo Semanais",
    yaxis_title="CGPA"
  )

  st.plotly_chart(fig, theme=None)

  st.subheader("P2. Análise Explanatória Insight #2")
  st.write("**Alunos com Transtornos Mentais Por Cursos**")
  st.write('''
    O gráfico evidencia que os cursos da área de exatas concentram a maior proporção de estudantes que relatam algum tipo de transtorno mental. Entre eles, o curso de Engenharia se destaca de forma expressiva, seguido pelo Bacharelado em Ciência da Computação e pelo Bacharelado em Tecnologia da Informação. O artigo “Mental health in undergraduate engineering students” (Mirabelli et al., publicado na Journal of Engineering Education) mostra que estudantes de engenharia apresentam níveis elevados de sofrimento     psicológico e enfrentam barreiras significativas para buscar ajuda. Uma das principais conclusões é que a cultura acadêmica em engenharia normaliza o estresse e a sobrecarga, tratando-os como parte natural da formação profissional. Isso faz com que sintomas de ansiedade, depressão ou exaustão muitas vezes não sejam reconhecidos ou tratados adequadamente

    Essa concentração pode estar associada a características típicas desses cursos: maior carga horária, conteúdos de alta complexidade e a exigência de longas jornadas de estudo. Tais fatores funcionam como potenciais gatilhos para quadros de ansiedade, depressão ou ataques de pânico, que são os transtornos identificados no dataset. A intensidade acadêmica, somada à pressão por desempenho, pode amplificar a vulnerabilidade desses estudantes.

    Por outro lado, os cursos da área de humanas e religiosos também apresentam presença de transtornos mentais, mas em proporções mais reduzidas. Isso não significa ausência de desafios psicológicos, mas sugere que a natureza das atividades acadêmicas nesses campos que são frequentemente mais qualitativas e reflexivas e isso pode exercer menor pressão em termos de carga cognitiva intensa e horas de estudo contínuo.
    ''')

  mental_health_issues = df[(df['Depression'] == 1) | (df['Anxiety'] == 1) | (df['PanicAttack'] == 1)]
  mental_health_counts = mental_health_issues.groupby('Course').size().reset_index(name='Count')

  data = mental_health_counts.sort_values(by='Count', ascending=False).head(10)

  fig2 = px.bar(data, x='Count', y='Course', orientation='h',
    color='Course',
    color_discrete_sequence=px.colors.cyclical.IceFire,
    text='Count',
    height=800,
    title='Quantidade de Alunos com Transtornos Mentais Por Cursos')


  fig2.update_traces(hovertemplate='Quantidade de Alunos: %{x}<br>Curso: %{y}')

  fig2.update_layout(
    xaxis_title="Quantidade de Alunos",
    yaxis_title="Curso",
    showlegend=False
  )

  st.plotly_chart(fig2, theme=None)

  st.subheader("P3. Análise Explanatória Insight #3")
  st.write("**Média de Engajamento Acadêmico por Ano de Estudo**")
  st.write('''
    A análise dos cursos selecionados revela que o engajamento acadêmico ao longo dos anos não segue uma trajetória linear de crescimento ou queda. Em vez disso, observam-se flutuações que sugerem a influência de fatores específicos de cada etapa, como mudanças no currículo, características das turmas ou até mesmo a complexidade dos conteúdos oferecidos em cada período.

    No 1º ano, o Bacharelado em Tecnologia da Informação se destaca com a maior média de engajamento, possivelmente impulsionado pelo entusiasmo inicial dos estudantes diante de conteúdos introdutórios e do contato com temas ligados à tecnologia. Em contraste, o curso de Engenharia apresenta o desempenho mais baixo, o que pode refletir tanto a dificuldade de adaptação dos ingressantes às disciplinas básicas quanto a exigência de uma carga horária intensa já no início da graduação.

    No 3º ano, o Bacharelado em Tecnologia da Informação atinge um pico expressivo de engajamento, superando de forma notável os demais cursos. Esse aumento pode estar relacionado ao momento em que os estudantes começam a vivenciar projetos práticos e conteúdos mais aplicados, que fortalecem a conexão entre teoria e prática e elevam o envolvimento.

    Já no 4º ano, ocorre uma inversão interessante: o curso de Engenharia assume a liderança em engajamento médio, sugerindo que os alunos atingem maior maturidade acadêmica e motivação ao se aproximarem da conclusão do curso. Nesse mesmo período, o Bacharelado em Ciência da Computação apresenta o menor resultado, o que pode indicar dificuldades ligadas à complexidade dos conteúdos avançados ou à pressão do mercado de trabalho, que se intensifica no final da graduação.
    ''')

  selected_courses = ['Engenharia', 'Bel. em Tecnologia da Informação', 'Bel. em Ciência da Computação']
  filtered_dt = df[df['Course'].isin(selected_courses)]

  avg_academic_engagement_filtered = filtered_dt.groupby(['YearOfStudy', 'Course'])['AcademicEngagement'].mean().reset_index()

  fig3 = px.bar(avg_academic_engagement_filtered, x='YearOfStudy', y='AcademicEngagement', color='Course',
    title='Engajamento acadêmico: média por ano nos cursos de tecnologia',
    barmode='group',
    custom_data=['Course'],
    height=500,
    color_discrete_sequence=px.colors.cyclical.IceFire)

  fig3.update_layout(
    xaxis_title="Ano de Estudo",
    yaxis_title="Média de Engajamento Acadêmico",
    legend_title_text='Curso'
  )

  fig3.update_traces(hovertemplate='Ano de Estudo: %{x}<br>Média de Engajamento Acadêmico: %{y:.2f}')
  st.plotly_chart(fig3, theme=None)

if __name__ == "__main__":
  main()
