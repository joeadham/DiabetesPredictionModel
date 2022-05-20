import streamlit as st

def check(text):
        if not text.isnumeric():
            st.warning("please enter integer")
            
            
def calculate(a,b,c,d,e,f):
   if(a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric and e.isnumeric and f.isnumeric):
       return True
   else:
       return False
                      
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
       if calculate(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction):
           st.success("DONE")
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
