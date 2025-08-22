import pandas as pd

def load():
  df = pd.read_csv('assets/data/mentalhealth_dataset.csv')
  normalized_df = normalize(df)

  return normalized_df

def normalize(df):
  # Padronização YearOfStudy
  df['YearOfStudy'] = (
    df['YearOfStudy']
    .str.capitalize()
    .replace({
      "Year 1": "1º Ano",
      "Year 2": "2º Ano",
      "Year 3": "3º Ano",
      "Year 4": "4º Ano"
    })
  )

  df['Course'] = (
      df['Course']
      .str.strip()  # remove espaços em branco extras
      .str.capitalize()  # primeira letra maiúscula
      .replace({
        'Engine': 'Engineering',
        'Engin': 'Engineering',
        'Koe': 'Engineering',
        'Nursing ': 'Diploma nursing',
        'It': 'Bachelor of information technology',
        'Bit': 'Bachelor of information technology',
        'Bcs': 'Bachelor of computer science',
        'Laws': 'Law',
        'Benl': 'Bachelor of English Language and Literature',
        'Irkhs': 'Kulliyyah of Islamic Revealed Knowledge and Human Sciences',
        'Kirkhs': 'Kulliyyah of Islamic Revealed Knowledge and Human Sciences',
        'Usuluddin': 'Kulliyyah of Islamic Revealed Knowledge and Human Sciences',
        'Kenms': 'Kulliyyah of Economics and Management Sciences',
        'Enm': 'Environmental Management',
        'Taasl': 'Teaching Arabic as a Second Language',
        'Cts': 'Communication and Translation Studies',
        'Econs': 'Economics',
        'Mhsc': 'Master of Human Sciences',
        'Malcom': 'Master of Arts (Applied Linguistics and Communication)',
        'Kop': 'Kulliyyah of Pharmacy',
        'Ala': 'Arabic Language and Literature'
    }).replace({
      "Biotechnology": "Biotecnologia",
      "Engineering": "Engenharia",
      "Communication": "Comunicação",
      "Diploma nursing": "Diploma em Enfermagem",
      "Pendidikan islam": "Educação Islâmica",
      "Radiography": "Radiografia",
      "Psychology": "Psicologia",
      "Fiqh fatwa": "Jurisprudência Islâmica",
      "Fiqh": "Jurisprudência Islâmica",
      "Bachelor of information technology": "Bel. em Tecnologia da Informação",
      "Diploma tesl": "Diploma em Ensino de Inglês como Segunda Língua",
      "Islamic education": "Educação Islâmica",
      "Bachelor of computer science": "Bel. em Ciência da Computação",
      "Nursing": "Enfermagem",
      "Biomedical science": "Ciências Biomédicas",
      "Law": "Direito",
      "Mathemathics": "Matemática",
      "Mathematics": "Matemática",
      "Human resources": "Recursos Humanos",
      "Accounting": "Contabilidade",
      "Marine science": "Ciência Marinha",
      "Banking studies": "Estudos Bancários",
      "Business administration": "Administração de Empresas",
      "Human sciences": "Ciências Humanas",
      "Economics": "Economia",
      "Kulliyyah of Islamic Revealed Knowledge and Human Sciences": "Conhecimento Islâmico e Ciências Humanas",
      "Usuluddin": "Conhecimento Islâmico e Ciências Humanas",
      "Islamic revealed knowledge": "Conhecimento Islâmico e Ciências Humanas",
      "Kulliyyah of Economics and Management Sciences": "Economia e Ciências de Gestão",
      "Kulliyyah of Pharmacy": "Farmácia",
      "Bachelor of English Language and Literature": "Bel. em Língua e Literatura Inglesa",
      "Teaching Arabic as a Second Language": "Ensino de Árabe como Segunda Língua",
      "Communication and Translation Studies": "Estudos de Comunicação e Tradução",
      "Master of Human Sciences": "Mestrado em Ciências Humanas",
      "Master of Arts (Applied Linguistics and Communication)": "Mestrado em Artes (Linguística Aplicada e Comunicação)",
      "Arabic Language and Literature": "Língua e Literatura Árabe",
      "Environmental Management": "Gestão Ambiental"
    })
  )
  return df
