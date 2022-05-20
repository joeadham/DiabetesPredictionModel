import streamlit as st
import numpy as np
import pandas as pd 


df = pd.read_csv('diabetes.csv')


def check(text):
        if not text.isnumeric():
            st.warning("please enter integer")
            
            
def calculate(a,b,c,d,e,f):
   if(a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric and e.isnumeric and f.isnumeric):
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

    prediction=RandomForestClassifierModel.predict(np.array([[int(pregnancies),int(Glucose),int(BloodPressure),int(SkinThickness),int(Insulin),int(BMI),int(DiabetesPedigreeFunction),int(Age)]]))
    print(prediction)
    return prediction
   
    
   
    
   
                      
def main():
    # st.title("Females above 21 years old diabetes prediction form")
    html_temp = """
    <div style="background-color:lightblue;padding:10px;border-left:6px dodgerblue">
    <h2 style="color:white;text-align:center;">Females above 21 years old diabetes prediction form </h2>
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
       if calculate(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction ):
           result=predict_diabetes(pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
           if (result == 1) :
               st.warning('You might have Diabeties. Please consult with a Doctor.')
           else:
                st.success("Hurray! You don't have Diabeties. Please consult with Doctor for verification.")
           #Function should be instead of done
       else: 
           st.warning("please check, all inputs must be integers")
     
        # result=predict_note_authentication(age,gender,polyuria,polydipsia,weight,weakness,polyphagia,genital_thrush,visual_blurring,itching,irritability, delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity)
        # if result ==1:
        #     st.warning('You might have Diabeties. Please consult with a Doctor.')
        # else:
        #     st.success("Hurray! You don't have Diabeties. Please consult with Doctor for verification.")

if __name__=='__main__':
    main()


html_temp1 = """
    <div style="background-color:white;padding:10px">
    
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)

#sidebars
st.sidebar.header("Diabeties Predictor Project ")
st.sidebar.text("Team 19")
