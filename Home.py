import streamlit as st

st.set_page_config(page_title='NORTE :)', page_icon='src/img/sat.png', layout='wide')

# st.title('Bem-vindo a demonstração da biblioteca Streamlit para a criação de paineis de dados interativos!', ali)
st.markdown("<h1 style='text-align: left; color: white;'>Bem-vindo a demonstração da biblioteca Streamlit <br/> para a criação de paineis de dados interativos!</h1>",
            unsafe_allow_html=True)

st.divider()

st.markdown("<h2 style='text-align: left; color: white;'>Possibilidades da Biblioteca</h2>",
            unsafe_allow_html=True)

col1, col2 = st.columns(2, gap='medium')

with col1:
    equation = st.text_area(
        'Podemos criar áreas de texto para compilar fórmulas, entrada de texto e muitos afins.'
        'Caso queira testar, basta alterar o texto abaixo e pressionar Cntrl + Enter na caixa de texto que o texto será compilado!',
        'e^{i\pi} + 1 = 0'
    )


with col2:
    st.latex(equation)

st.divider()

st.subheader('Caso queira colocar alguma métrica e afins. É possível coletar respostas de API (previsão do tempo, bolsa de valores e afins)')

st.text('Aqui n tem nada de requisição, mas fica a demonstração visual :)')

col3, col4, col5 = st.columns(3)
col3.metric("Temperature", "70 °F", "1.2 °F")
col4.metric("Wind", "9 mph", "-8%")
col5.metric("Humidity", "86%", "4%")

st.divider()

col6, col7 = st.columns(2)



with col6:

    st.subheader('Exemplo de markdown')

    st.divider()

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

with col7:

    st.subheader('Demonstração de Código')

    st.empty()

    code = '''def greetings():
        print('Aoba, bão?')'''
    st.code(code, language='python')

    st.empty()

    code_cpp = '''#include <iostream>
#include <cmath>

int main() {
    // Oia que bunito 
    double result = std::exp(std::complex<double>(0, M_PI)) + 1;

    // Coisa boa
    std::cout << "e^(i*pi) + 1 = " << result << std::endl;

    return 0;
}'''
    st.code(code_cpp, language='cpp')
