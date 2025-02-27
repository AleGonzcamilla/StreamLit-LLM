import streamlit as st
import pandas as pd
import numpy as np
from gpt_wrapper import gpt_wrapper_message

st.title('GPT Wrapper')
st.divider()
st.subheader('Interactúa con el modelo GPT-3 de OpenAI')
st.image('https://www.streamlit.io/images/brand/streamlit-mark-color.png')


######
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
#####


prompt = st.text_input('Escribe aquí')

if st.button('Escribe tu mensaje'):
    gpt_wrapper_message(prompt)
    st.success('Respuesta generada')
else:
    st.warning('Envia tu respuesta')