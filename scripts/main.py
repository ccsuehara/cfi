import streamlit as st
import altair as alt
import pandas as pd

new_df = pd.read_excel('../datos/eidata.xlsx')

t1 = new_df[['toma_decisiones',
    'grit', 'escrupulosidad', 'amabilidad', 'apertura','extroversion', 'estabilidad', 'index_igualdad', 'moment'
        ]].groupby(['moment']).mean().round(2).reset_index()


t2 = new_df[['tablet', 'toma_decisiones',
    'grit', 'escrupulosidad', 'amabilidad', 'apertura','extroversion', 'estabilidad', 'index_igualdad', 'moment'
        ]].groupby(['tablet','moment']).mean().round(2).reset_index()


t3 = new_df[['tablet', 'toma_decisiones',
    'grit', 'escrupulosidad', 'amabilidad', 'apertura','extroversion', 'estabilidad', 'index_igualdad', 'moment', 'sexo'
        ]].groupby(['sexo', 'moment']).mean().round(2).reset_index()

t4 = new_df[['tablet', 'toma_decisiones',
    'grit', 'escrupulosidad', 'amabilidad', 'apertura','extroversion', 'estabilidad', 'index_igualdad', 'moment','sexo'
        ]].groupby(['tablet','sexo', 'moment']).mean().round(2).reset_index()

t2_1 = new_df[[ 'Estar al tanto', 'Redes Sociales', 'Comunicación',
       'Aprender para el colegio', 'Aprendizaje propio', 'Ed. Financiera',
       'Prevención desastres', 'Resolver problemas', 'Juegos', 'Youtube', 'moment']].groupby(['moment']).mean().round(2).reset_index()

t2_2 = new_df[[ 'Estar al tanto', 'Redes Sociales', 'Comunicación',
       'Aprender para el colegio', 'Aprendizaje propio', 'Ed. Financiera',
       'Prevención desastres', 'Resolver problemas', 'Juegos', 'Youtube', 'moment', 'tablet']].groupby(['tablet','moment']).mean().round(2).reset_index()

t2_3 = new_df[[ 'Estar al tanto', 'Redes Sociales', 'Comunicación',
       'Aprender para el colegio', 'Aprendizaje propio', 'Ed. Financiera',
       'Prevención desastres', 'Resolver problemas', 'Juegos', 'Youtube', 'moment', 'sexo']].groupby(['sexo','moment']).mean().round(2).reset_index()

t2_4 = new_df[[ 'Estar al tanto', 'Redes Sociales', 'Comunicación',
       'Aprender para el colegio', 'Aprendizaje propio', 'Ed. Financiera',
       'Prevención desastres', 'Resolver problemas', 'Juegos', 'Youtube', 'moment', 'sexo', 'tablet']].groupby(['tablet','sexo','moment']).mean().round(2).reset_index()


t3_1 = new_df.pivot_table(index='proyeccion_clean', columns='moment',values='uno', aggfunc='sum').fillna(0).apply(lambda x:100 * x / float(x.sum())).round(2)

a = new_df[new_df['moment'] == 'LB'].pivot_table(index='proyeccion_clean', columns='tablet',values='uno', aggfunc='sum'
                                           ).fillna(0).apply(lambda x:100 * x / float(x.sum())).round(2)
b = new_df[new_df['moment'] == 'Fin'].pivot_table(index='proyeccion_clean', columns='tablet',values='uno', aggfunc='sum'
                                           ).fillna(0).apply(lambda x:100 * x / float(x.sum())).round(2)
           
t3_2 =  pd.concat([a, b], axis=1, keys=['lb', 'fin']).fillna(0)
t3_2.columns.names = [None, 'tablet' ]


fin = new_df[new_df['moment'] == 'Fin'].pivot_table(index='proyeccion_clean', columns='sexo',values='uno',
                                                    aggfunc='sum').fillna(0).apply(lambda x:100 * x / float(x.sum())).round(2)

lb = new_df[new_df['moment'] == 'LB'].pivot_table(index='proyeccion_clean', columns='sexo',values='uno',
                                                  aggfunc='sum').fillna(0).apply(lambda x:100 * x / float(x.sum())).round(2)

t3_3 = pd.concat([lb, fin], axis=1, keys=['lb', 'fin']).fillna(0)
t3_3.columns.names = [None, None]


st.set_page_config(page_title="cfi",layout='wide')

header = st.container()

sec1 = st.container()
exp1 = st.container()

sec2 = st.container()
exp2 = st.container()

sec3 = st.container()
exp3 = st.container()


with header:
    st.title("Resumen de resultados del proyecto CFI")
    
    st.markdown('''Reporte de resultados de línea de base del proyecto CFI

- Estudiantes que contestaron el cuestionario de LB: 67
- Estudiantes que contestaron el cuestionario de Egreso: 50

- Grupo de estudiantes que recibieron tablets:  42 , en adelante, grupo 1  
- Grupo de estudiantes que no recibieron tablets:  25, en adelante, grupo 0

- Grupo de estudiantes que recibieron tablets:  38 , en adelante, grupo 1  
- Grupo de estudiantes que no recibieron tablets:  12, en adelante, grupo 0

## Resumen de indicadores computados: 

- 1. Habilidades socioemocionales  
6 habilidades socioemocionales fueron evaluadas: 
- Toma de decisiones    
- Perserverancia (grit)  
- Escrupulosidad  
- Amabilidad  
- Apertura  
- Extroversión  
- Estabilidad
- 2.  Indice de igualdad (index igualdad, o II), donde las evaluaciones de género son condensadas en un número.  
- 3.  Uso del internet  
- 4.  Proyección profesional 
''')
    
    st.markdown(''' #### Resumen de indicadores computados: ''')



with sec1:
    st.markdown('''#### Habilidades socioemocionales e II ''')
    st.dataframe(t1)
    
    st.markdown('''#### Habilidades socioemocionales e II, por receptores de tablet''')
    st.dataframe(t2)
    
    st.markdown('''#### Habilidades socioemocionales e II, por género ''')
    st.dataframe(t3)
    
    st.markdown('''#### Habilidades socioemocionales e I, por receptores de tablet y género ''')
    st.dataframe(t4)

    
with sec2:
    st.markdown('''#### Uso del internet (horas) ''')
    st.dataframe(t2_1)
    
    st.markdown('''#### Uso del internet (horas), por receptores de tablet''')
    st.dataframe(t2_2)
    
    st.markdown('''#### Uso del internet (horas), por género ''')
    st.dataframe(t2_3)
    
    st.markdown('''#### Uso del internet (horas), por receptores de tablet y género ''')
    st.dataframe(t2_4)
    
    
with sec3:
    st.markdown('''#### Proyección profesional ''')
    st.dataframe(t3_1)
    
    st.markdown('''#### Proyección profesional, por receptores de tablet''')
    st.dataframe(t3_2)
    
    st.markdown('''#### Proyección profesional, por género ''')
    st.dataframe(t3_3)
    
    # st.markdown('''#### Proyección profesional, por receptores de tablet y género ''')
    # st.dataframe(t3_4)