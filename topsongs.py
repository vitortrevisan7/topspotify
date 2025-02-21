# Vitor Trevisan Nocente

import streamlit as st

st.header("Que música fazia sucesso quando você nasceu?", divider = "rainbow")
st.write("Escolha o seu mês e ano de nascimento:")

mes = st.select_slider('Mês:',
                       options=[
                           "Janeiro",
                           "Fevereiro",
                           "Março",
                           "Abril",
                           "Maio",
                           "Junho",
                           "Julho",
                           "Agosto",
                           "Setembro",
                           "Outubro",
                           "Novembro",
                           "Dezembro"], value="Janeiro")  # Seleciona mês
ano = st.slider("Ano:", 1960, 2023, 1960) # Seleciona ano

st.write('A música que fazia sucesso em ', mes, 'do ano', ano, 'era:')

file_path = 'songlist.csv'

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    for line in file:
        row = line.strip().split(', ')
        if row[0] == str(ano) and row[1] == mes:
            musica = row[2] + ' - ' + row[3]
            st.subheader(musica) 
            st.write('Link: ', row[4])
