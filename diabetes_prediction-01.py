import streamlit as st
import pickle


pickle_in=open("Daibetes_RandomForest.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_output(sex,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level):
    res=classifier.predict([[sex,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
    if(res==1):
        return "There is Diabetes problem"
    else:
        return "There is no Diabetes Problem"

def main():
    st.title("Diabetes Prediction")
    html="""
    <div style='background:'blue'>
    </div>"""
    st.markdown(html,unsafe_allow_html=True)
    sex=st.text_input("Sex[Male=1,Female=0]","Type Here")
    age=st.text_input("Age","Type Here")
    hypertension=st.text_input("Hypertension","Type Here")
    heart_disease=st.text_input("heart_disease","Type Here")
    smoking_history=st.text_input("Smoking_History['former'=1,'current'=2,'not current'=3,'ever'=4,'never'=5,'Otherwise'=0]","Type Here")
    bmi=st.text_input("BMI","Type Here")
    HbA1c_level=st.text_input("HbA1c_level","Type Here")
    blood_glucose_level=st.text_input("blood_glucose_level","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_output(sex,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level)
    st.success('{}'.format(result))

if __name__=='__main__':
    main()