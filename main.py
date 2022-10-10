import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import geihdanepy as geih

st.markdown(f'<h1 style="color:#0E6655  ;font-size:50px;">{"Proyecto 9"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"En este proyecto se analizará el ingreso de los trabajadores mediante el modelo Random Forest, logrando así obtener un modelo que logre predecir el salario por medio de las siguientes variables:"}</h1>', unsafe_allow_html=True)

df_1 = pd.read_csv('GEIH_ocupados.csv.crdownload')
df_2 = df_1[['P6426','P6510','P6590','P6990','P6430','P6500','INGLABO']]
st.write(df_2.columns)

st.markdown(f'<h1 style="color:#0E6655  ;font-size:35px;">{"Descripción sucinta de las variables"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"Variable dependiente: INGLABO:"}</h1>', unsafe_allow_html=True)
st.write('Constituye los ingresos laborales')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6426:"}</h1>', unsafe_allow_html=True)
st.write('Es el tiempo que lleva trabajando en la misma empresa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6510:"}</h1>', unsafe_allow_html=True)
st.write('Es la variable de ingresos por horas extra del mes pasado. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6590:"}</h1>', unsafe_allow_html=True)
st.write('Indica si el trabajador recibió, además del salario en dinero, alimentos como parte de pago por su trabajo el mes pasado. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6990:"}</h1>', unsafe_allow_html=True)
st.write('Hace referencia a la afiliación del trabajador a una aseguradora de riesgos profesionales. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6430:"}</h1>', unsafe_allow_html=True)
st.write('Indica su posición en el trabajo. Siendo 1: Obrero o empleado de empresa particular, 2: Obrero o empleado del gobierno, 3: Empleado doméstico, 4: Trabajador por cuenta propia, 5: Patrón o empleador, 6: Trabajador familiar sin remuneración, 7: Trabajador sin remuneración en empresas o negocios de otros familiares, 8: Jornalero o peón, 9: otro')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6500:"}</h1>', unsafe_allow_html=True)
st.write('Hace referencia a las ganancias del trabajador en el mes pasado antes de descuentos')

st.markdown(f'<h1 style="color:#0E6655  ;font-size:35px;">{"Gráficas relevantes"}</h1>', unsafe_allow_html=True)
grafica_relevante_1=Image.open('grafica_relevante_1.png')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"La siguiente gráfica indica la importancia de cada variable en la estimación de los ingresos"}</h1>', unsafe_allow_html=True)
st.image(grafica_relevante_1)
grafica_relevante_2=Image.open('grafica_relevante_2.png')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"La siguiente gráfica indica la importancia de cada variable en la estimación de los ingresos, implicando que tan determinantes son al estimar un menor salario o un mayor salario"}</h1>', unsafe_allow_html=True)
st.image(grafica_relevante_2)

st.markdown(f'<h1 style="color:#0E6655  ;font-size:35px;">{"Link al notebook de entrenamiento del modelo"}</h1>', unsafe_allow_html=True)






















