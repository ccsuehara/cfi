import streamlit as st
import altair as alt
import pandas as pd

new_df = pd.read_excel('./eidata.xlsx')

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
    

Se computaron los indicadores de 1) línea de base $T_0$,  y de 2) egreso, $T_1$ para los siguientes grupos de interés: 
1. Estudiantes que entraron al programa educativo y recibieron tablets e internet. ($G1$).  
2. Estudiantes que entraron al programa educativo y no recibieron tablets ni internet. ($G0$).  

Se pueden elaborar una serie de comparaciones:
a. Diferencia entre el egreso y la línea de base de todos los indicadores, para ambos grupos. 
b. Diferencia entre el egreso y la línea de base de todos los indicadores, para cada uno de los grupos. 
c. Doble diferencia, entre el egreso y la línea de base, y entre los receptores/no receptores de tablets e internet. 

## Resultado de las encuestas: 
1. Estudiantes que contestaron el cuestionario de LB: 67

    1.1. Grupo de estudiantes que recibieron tablets:  42 , en adelante, $G1$.  
    1.2. Grupo de estudiantes que no recibieron tablets:  25, en adelante, $G0$.  

2. Estudiantes que contestaron el cuestionario de Egreso: 50

    2.1. Grupo de estudiantes que recibieron tablets:  38 , en adelante, $G1$.  
    2.2. Grupo de estudiantes que no recibieron tablets:  12, en adelante, $G0$.  

## Resumen de indicadores computados:
A continuación se muestra un resumen de los indicadores 

| Medida        | Descripción   |
| ------------- |:-------------:|
| Toma de decisiones       | Mide el nivel de **toma de decisiones** los grupos definidos  |
| Perserverancia      | Mide el nivel de **perseverancia** los grupos definidos      |
| Otras habilidades socioemocionales      |  Habilidades socioemocionales que componen el _big 5_    |
| Indice de igualdad (II) | Indice que resume actitudes hacia la igualdad de género      |
| Uso del internet | Promedio de horas semanales dedicadas a diferentes usos del internet      |
| Proyección profesional | Distribución porcentual de cada grupo definido respecto a lo que estarán haciendo después de terminar el colegio.      |


## Pequeña nota metodológica: 

Las habilidades socioemocionales y el índice de igualdad han sido normalizados, es decir, el promedio de este índice es 0. Los resultados son expresados en desviaciones estándar. 


## Advertencia al interpretar los resultados: 
- Esta no es una evaluación de impacto, por lo que los efectos totales no se pueden leer como resultados causales, sino como indicadores de seguimiento que establecen un retrato de la situación antes/después del programa, ignorando causas externas a este programa que podrían haber incidido en estos resultados.  
- El grupo de no receptores tiene muy pocas observaciones para el egreso (solo 11), por lo que hay que tener mucho cuidado al interpretar los resultados de dicho grupo, así como los resultados con respecto a dicho grupo.  
- Por ello, los resultados tendrán una mejor lectura si sólo utilizamos el del grupo de receptores de tablet, así como los resultados totales.  


''')
    
    st.markdown(''' #### Resumen de indicadores computados: ''')



with sec1:
    st.markdown('''#### Habilidades socioemocionales e II ''')
    st.markdown("Estos son los resultados totales entre el fin y la LB: Ha habido una mejora en toma de decisiones (.11) y perseverancia (.17),     mientras que ha habido una pequeña disminución en ii (-.01). En cuanto a habilidades SE, los mayores incrementos se observan en extroversion (.32), estabilidad (.24) y escrupulosidad.")
    st.dataframe(t1)
    
    
    st.markdown('''#### Habilidades socioemocionales e II, por receptores de tablet''')
    st.markdown("Estos son los resultados, por grupo receptor de tablet. Hace la comparación entre la diferencia de resultados entre ambos grupos. Una mejor lectura sugiere que los efectos fueron casi los mismos en el grupo de receptores de tablet.")
    st.dataframe(t2)
    
    
    st.markdown('''#### Habilidades socioemocionales e II, por género ''')
    st.markdown(''' Estos son los resultados, por género, de los resultados totales entre principio/fin. Observamos que el grupo de hombres inició con una "menor" dotación de este index (en casi todos los casos, pero por lo mismo, tuvo un mayor "crecimiento" que el grupo de mujeres (por ejemplo amabilidad, o extroversion). Las mujeres también mostraron mejores resultados al fin del programa, sobre todo en toma de decisiones (.09 a .15)''')
    st.dataframe(t3)
    
    st.markdown('''#### Habilidades socioemocionales e I, por receptores de tablet y género ''')
    st.markdown(''' Estos son los resultados, por género, de los resultados totales entre principio/fin, por receptores de tablet. Observamos que los receptores de tablets tuvieron una menor mejora en todos los campos, en especial, las mujeres.''')
    st.dataframe(t4)

    
with sec2:
    st.markdown('''#### Uso del internet (horas) ''')
    st.markdown('''En este cuadro se muestra el promedio de horas que lxs estudiantes le dedican a cada tipo de uso: Ciertos usos aumentan (como aquellos que los que el programa promueve), y otros, disminuyen (redes sociales, youtube)''')
    st.dataframe(t2_1)
    
    st.markdown('''#### Uso del internet (horas), por receptores de tablet''')
    st.markdown('''Observamos que aquellos que recibieron tablet utilizaron el internet, en mayor intensidad que los no receptores, para los propósitos educativos del programa. Sin embargo, otros usos importantes, como estar al tanto, y aprendizaje escolar, no fueron favorecidos por este uso.''')
    st.dataframe(t2_2)
    
    st.markdown('''#### Uso del internet (horas), por género ''')
    st.markdown('''Las mujeres son quienes más utilizaron, con mayor intensidad, el internet para propósitos educativos. ''')
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