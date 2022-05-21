import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image


df = pd.read_csv('diabetes.csv')


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False



def check(text):
        if not (( text.isnumeric() or is_float(text) ) ):
            st.error("Please fill this field with numerical value")
            
        
        
def check1(text):
        if not (( text.isnumeric() or is_float(text) ) and float(text)>0):
            return False
        else :
            return True
           
                 
def check2(a,b,c,d,e,f):
   if(check1(a) and check1(b) and check1 (c) and check1(d)and check1(e)and check1(f)):
        return True
   else:
       return False
   
    
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for col in cols:
    df[col].replace(0,np.NaN,inplace=True)
    
# We can fill in NaN values with a median according to the target
for col in df.columns:
    df.loc[(df["Outcome"]==0) & (df[col].isnull()),col] = df[df["Outcome"]==0][col].median()
    df.loc[(df["Outcome"]==1) & (df[col].isnull()),col] = df[df["Outcome"]==1][col].median()
   
from sklearn.model_selection import train_test_split
X = df [['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]
Y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=44, shuffle =True)



from sklearn.ensemble import RandomForestClassifier
RandomForestClassifierModel = RandomForestClassifier(n_estimators=70,max_depth=5,random_state=33) 
RandomForestClassifierModel.fit(X_train, y_train)


def predict_diabetes(pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction, Age):

    prediction=RandomForestClassifierModel.predict(np.array([[int(float(pregnancies)),int(float(Glucose)),int(float(BloodPressure)),int(float(SkinThickness)),int(float(Insulin)),int(float(BMI)),int(float(DiabetesPedigreeFunction)),int(float(Age))]]))
    print(prediction)
    return prediction
   
    
   
    
   
                      
def main():
    # st.title("Females above 21 years old diabetes prediction form")
    html_temp = """
    <div style="background-color:#ACCFE2 ;padding:10px;border-left:100px dodgerblue">
    <h2 style="color#:1874CD;text-align:center;font-family: Times New Roman ;">Females above 21 years old diabetes prediction form </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader("Please fill the following fields")
    
    pregnancies= st.number_input("pregnancies",min_value=0)
    Age= st.number_input("Age",min_value=21)
    
    Glucose =st.text_input("Glucose concentration",0)
    check(Glucose)
    BloodPressure=st.text_input("Blood Pressure (mm Hg)",0)
    check(BloodPressure)
    SkinThickness=st.text_input("Triceps Skin Fold Thickness",0)
    check(SkinThickness)
    Insulin=st.text_input("2 Hour serum insulin level",0)
    check(Insulin)
    BMI=st.text_input("BMI",0)
    check(BMI)
    DiabetesPedigreeFunction=st.text_input("Diabetes pedigree function",0)
    check(DiabetesPedigreeFunction)
    
   

    
    if st.button("Submit"):
       if check2(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction ):
           result=predict_diabetes(pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
           if (result == 1) :
               st.warning('You might have Diabeties. Please consult a Doctor.')
           else:
                st.success("Hurray! You don't have Diabeties. Please consult a Doctor for verification.")
          
       else: 
           st.error("Please fill the fields with the correct values")
     
    
    github = '[GitHub repository](https://github.com/joeadham/DiabetesPredictionModel)'
    st.markdown(github, unsafe_allow_html=True)
   
if __name__=='__main__':
    main()


html_temp1 = """
    <div style="background-color:white;padding:10px">
    
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)


page_bg_img = '''

'''

st.markdown(page_bg_img, unsafe_allow_html=True)
#sidebars
st.sidebar.header("Diabeties Predictor Project ")
image = Image.open('diabetess2.jpg')

st.sidebar.image(image)

st.sidebar.markdown("Using python and the dataset provided on [Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)\
                    we created a random forest machine learning model that predicts\
                    if a female above the age of 20 has\
                diabetes with 90% accuracy.")
                
st.sidebar.markdown("Made by Cairo university systems and biomedical engineering students, for the biostatistics course.\
                    Team 20, 2024 batch.")