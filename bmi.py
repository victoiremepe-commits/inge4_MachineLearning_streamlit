import streamlit as st
st.title('Welcome to the BMI calculator')

weight = st.number_input('Enter your weight in kg: ')

height = st.radio('Select your height format', ('cms', 'meters', 'feet'))

try:
    if height == 'cms':
        height = st.number_input('cms: ')
        bmi = weight / (height/100)**2
    elif height == 'meters':
        height = st.number_input('meters: ')
        bmi = weight / height**2
    elif height == 'feet':
        height = st.number_input('feet: ')
        bmi = weight / (height/3.28)**2
except :
    print('Zero division error')

if(st.button('Calculate BMI')):
    st.write(f'Your BMI is: {format(round(bmi))}')

    if bmi < 16:
        st.error('You have severely underweight')
    elif bmi >= 16 and bmi < 18.5:
        st.warning('You have underweight')
    elif bmi >= 18.5 and bmi < 25:
        st.info('You have normal weight')
    elif bmi >= 25 and bmi < 30:
        st.warning('You have overweight')
    else:
        st.error('You have obesity')

    st.balloons()






