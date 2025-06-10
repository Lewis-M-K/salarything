import pickle
import streamlit as st

# Loads the trained model and stores it in the variable model
model = pickle.load(open('../salarything/model.pkl', 'rb'))

# Creates seven columns
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
# Places the title in the middle column thus centering it visually
with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')
with col3:
    st.title("ⴍage")
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')

# Description text centering by creating 3 columns and placing it in the middle column
col7, col8, col9 = st.columns(3)
with col7:
    st.write('')
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)
with col9:
    st.write('')

# Definition of the input options
gen_list = ["Female", "Male"] # Gender selection options
edu_list = ["Bachelor's", "Master's", "PhD"] # Education level options
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"] # Job selection option
job_idx = [0, 1, 10, 11, 20] # Index for each job

gender = st.radio('Pick your gender', gen_list) # Radio button for gender
age = st.slider('Pick your age', 21, 55) # Slider for age selection
# Dropdowns for education level and job title
education = st.selectbox('Pick your education level', edu_list)
job = st.selectbox('Pick your job title', job_list)
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f") # Slider for experience

# Places a clickable button at the center using 5 columns
col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write('')
with col11:
    st.write('')
with col12:
    predict_btn = st.button('Predict Salary')
with col13:
    st.write('')
with col14:
    st.write('')

# Actions when the button is clicked
if(predict_btn):
    inp1 = int(age) # Converts
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5]
    salary = model.predict([X])
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")
    with col17:
        st.write('')

