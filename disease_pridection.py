# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:49:43 2022

@author: U.Manishankar
"""

import numpy as np
import pickle



load_model=pickle.load(open('prediction_system.sav','rb'))



def disease_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    #reshapr the array as we prediting vfor one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    #standardize the input data
    #std_data=scaler.transform(input_data_reshaped)
    #print(std_data)
    prediction =load_model.predict(input_data_reshaped)
    result=prediction[0]
    return  result

import streamlit as st
st.set_page_config(layout="wide")

def main():
    
    
    
    st.title("Disease prediction")
    import streamlit.components.v1 as components
    
    components.html(
    """
    
    <!DOCTYPE html>
    <title>Text Example</title>
    <style>
    div.container {
    background-color: transparent;
    }
    div.container p {
    font-family: "Source Sans Pro", sans-serif;
    font-size: 28px;
    font-style: normal;
    font-weight: bold;
    text-decoration: none;
    text-transform: none;
    color: lightblue;
    background-color: #transparent;
    }
    </style>
    
    <div class="container">
    <p>Please check the symptoms you are experiencing from the list below.</p>
    </div>
    """,
    height=100,
    )
    
    
  
    
    
    col1,col2,col3,col4=st.columns(4)
    col1.subheader("A")
    abdominal_pain=int(col1.checkbox("abdominal_pain"))
    abnormal_menstruation=int(col1.checkbox("abnormal_menstruation"))
    acidity=int(col1.checkbox("acidity"))
    acute_liver_failure=int(col1.checkbox("acute_liver_failure"))
    altered_sensorium=int(col1.checkbox("altered_sensorium"))
    anxiety=int(col1.checkbox("anxiety"))
    col1.subheader("B")
    back_pain=int(col1.checkbox("back_pain"))
    belly_pain=int(col1.checkbox("belly_pain"))
    blackheads=int(col1.checkbox("blackheads"))
    blister=int(col1.checkbox("blister"))
    bladder_discomfort=int(col1.checkbox("bladder_discomfort"))
    blood_in_sputum=int(col1.checkbox("blood_in_sputum"))
    bloody_stool=int(col1.checkbox("bloody_stool"))
    blurred_and_distorted_vision=int(col1.checkbox("blurred_and_distorted_vision"))
    breathlessness=int(col1.checkbox("breathlessness"))
    brittle_nails=int(col1.checkbox("brittle_nails"))
    bruising=int(col1.checkbox("bruising"))
    burning_micturition=int(col1.checkbox("burning_micturition"))
    col1.subheader("C")
    constipation=int(col1.checkbox("constipation"))
    chest_pain=int(col1.checkbox("chest_pain"))
    chills=int(col1.checkbox("chills"))
    cold_hands_and_feets=int(col1.checkbox("col1d_hands_and_feets"))
    coma=int(col1.checkbox("coma"))
    congestion=int(col1.checkbox("congestion"))
    continuous_feel_of_urine=int(col1.checkbox("continuous_feel_of_urine"))
    continuous_sneezing=int(col1.checkbox("continuous_sneezing"))
    cough=int(col1.checkbox("cough"))
    cramps=int(col1.checkbox("cramps"))
    col1.subheader("D")
    dehydration=int(col1.checkbox("dehydration"))
    depression=int(col1.checkbox("depression"))
    diarrhoea=int(col1.checkbox("diarrhoea"))
    dischromic_patches=int(col1.checkbox("dischromic_patches"))
    distention_of_abdomen=int(col1.checkbox("distention_of_abdomen"))
    dizziness=int(col1.checkbox("dizziness"))
    drying_and_tingling_lips=int(col1.checkbox("drying_and_tingling_lips"))
    col1.subheader("E")
    enlarged_thyroid=int(col1.checkbox("enlarged_thyroid"))
    excessive_hunger=int(col1.checkbox("excessive_hunger"))
    extra_marital_contacts=int(col1.checkbox("extra_marital_contacts"))
    col1.subheader("F")
    family_history=int(col1.checkbox("family_history"))
    fast_heart_rate=int(col1.checkbox("fast_heart_rate"))
    fatigue=int(col1.checkbox("fatigue"))
    fluid_overload=int(col1.checkbox("fluid_overload"))
    foul_smell_of_urine=int(col1.checkbox("foul_smell_of_urine"))
    col2.subheader("H")
    headache=int(col2.checkbox("headache"))
    high_fever=int(col2.checkbox("high_fever"))
    hip_joint_pain=int(col2.checkbox("hip_joint_pain"))
    history_of_alcohol_consumption=int(col2.checkbox("history_of_alcohol_consumption"))
    col2.subheader("I")
    increased_appetite=int(col2.checkbox("increased_appetite"))
    indigestion=int(col2.checkbox("indigestion"))
    inflammatory_nails=int(col2.checkbox("inflammatory_nails"))
    internal_itching=int(col2.checkbox("internal_itching"))
    irregular_sugar_level=int(col2.checkbox("irregular_sugar_level"))
    irritability=int(col2.checkbox("irritability"))
    irritation_in_anus=int(col2.checkbox("irritation_in_anus"))
    itching=int(col2.checkbox(" itching"))
    col2.subheader("J")
    joint_pain=int(col2.checkbox("joint_pain"))
    col2.subheader("K")
    knee_pain=int(col2.checkbox("knee_pain"))
    lack_of_concentration=int(col2.checkbox("lack_of_concentration"))
    col2.subheader("L")
    lethargy=int(col2.checkbox("lethargy"))
    loss_of_appetite=int(col2.checkbox("loss_of_appetite"))
    loss_of_balance=int(col2.checkbox("loss_of_balance"))
    loss_of_smell=int(col2.checkbox("loss_of_smell"))
    col2.subheader("M")
    malaise=int(col2.checkbox("malaise"))
    mild_fever=int(col2.checkbox("mild_fever"))
    mood_swings=int(col2.checkbox("mood_swings"))
    movement_stiffness=int(col2.checkbox("movement_stiffness"))
    mucoid_sputum=int(col2.checkbox("mucoid_sputum"))
    muscle_pain=int(col2.checkbox("muscle_pain"))
    muscle_wasting=int(col2.checkbox("muscle_wasting"))
    muscle_weakness=int(col2.checkbox("muscle_weakness"))
    col2.subheader("N")
    nausea=int(col2.checkbox("nausea"))
    neck_pain=int(col2.checkbox("neck_pain"))
    nodal_skin_eruptions=int(col2.checkbox("nodal_skin_eruptions"))
    col2.subheader("O")
    obesity=int(col2.checkbox("obesity"))
    col2.subheader("P")
    pain_behind_the_eyes=int(col2.checkbox("pain_behind_the_eyes"))
    pain_during_bowel_movements=int(col2.checkbox("pain_during_bowel_movements"))
    pain_in_anal_region=int(col2.checkbox("pain_in_anal_region"))
    col3.subheader("P")
    painful_walking=int(col3.checkbox("painful_walking"))
    palpitations=int(col3.checkbox("palpitations"))
    passage_of_gases=int(col3.checkbox("passage_of_gases"))
    patches_in_throat=int(col3.checkbox("patches_in_throat"))
    phlegm=int(col3.checkbox("phlegm"))
    polyuria=int(col3.checkbox("polyuria"))
    prominent_veins_on_calf=int(col3.checkbox("prominent_veins_on_calf"))
    puffy_face_and_eyes=int(col3.checkbox("puffy_face_and_eyes"))
    pus_filled_pimples=int(col3.checkbox("pus_filled_pimples"))
    col3.subheader("R")
    receiving_blood_transfusion=int(col3.checkbox("receiving_blood_transfusion"))
    receiving_unsterile_injections=int(col3.checkbox("receiving_unsterile_injections"))
    red_sore_around_nose=int(col3.checkbox("red_sore_around_nose"))
    red_spots_over_body=int(col3.checkbox("red_spots_over_body"))
    redness_of_eyes=int(col3.checkbox("redness_of_eyes"))
    restlessness=int(col3.checkbox("restlessness"))
    runny_nose=int(col3.checkbox("runny_nose"))
    rusty_sputum=int(col3.checkbox("rusty_sputum"))
    col3.subheader("S")
    scurring=int(col3.checkbox("scurring"))
    shivering=int(col3.checkbox("shivering"))
    silver_like_dusting=int(col3.checkbox("silver_like_dusting"))
    sinus_pressure=int(col3.checkbox("sinus_pressure"))
    skin_peeling=int(col3.checkbox("skin_peeling"))
    skin_rash=int(col3.checkbox(" skin_rash"))
    slurred_speech=int(col3.checkbox("slurred_speech"))
    small_dents_in_nails=int(col3.checkbox("small_dents_in_nails"))
    spinning_movements=int(col3.checkbox("spinning_movements"))
    spotting_urination=int(col3.checkbox("spotting_urination"))
    stiff_neck=int(col3.checkbox("stiff_neck"))
    stomach_bleeding=int(col3.checkbox("stomach_bleeding"))
    stomach_pain=int(col3.checkbox("stomach_pain"))
    sunken_eyes=int(col3.checkbox("sunken_eyes"))
    sweating=int(col3.checkbox("sweating"))
    swelled_lymph_nodes=int(col3.checkbox("swelled_lymph_nodes"))
    swelling_joints=int(col3.checkbox("swelling_joints"))
    swollen_blood_vessels=int(col3.checkbox("swollen_blood_vessels"))
    swollen_extremeties=int(col3.checkbox("swollen_extremeties"))
    swollen_legs=int(col3.checkbox("swollen_legs"))
    col4.subheader("T")
    throat_irritation=int(col4.checkbox("throat_irritation"))
    toxic_look_typhos=int(col4.checkbox("toxic_look_typhos"))
    ulcers_on_tongue=int(col4.checkbox("ulcers_on_tongue"))
    col4.subheader("U")
    unsteadiness=int(col4.checkbox("unsteadiness"))
    visual_disturbances=int(col4.checkbox("visual_disturbances"))
    col4.subheader("V")
    vomiting=int(col4.checkbox("vomiting"))
    col4.subheader("W")
    watering_from_eyes=int(col4.checkbox("watering_from_eyes"))
    weakness_in_limbs=int(col4.checkbox("weakness_in_limbs"))
    weakness_of_one_body_side=int(col4.checkbox("weakness_of_one_body_side"))
    weight_gain=int(col4.checkbox("weight_gain"))
    weight_loss=int(col4.checkbox("weight_loss"))
    welling_of_stomach=int(col4.checkbox("welling_of_stomach"))
    col4.subheader("Y")
    yellow_crust_ooze=int(col4.checkbox(" yellow_crust_ooze"))
    yellow_urine=int(col4.checkbox("yellow_urine"))
    yellowing_of_eyes=int(col4.checkbox("yellowing_of_eyes"))
    yellowish_skin=dark_urine=int(col4.checkbox("yellowish_skindark_urine"))
   

     

    
    
    
    
    
    
    
    Diagnosis=''
    
   
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
    st.write("")
    st.write("")  
    st.write("")
    st.write("") 
    
    
    
    l=[                             itching,
                                   skin_rash,
                                  nodal_skin_eruptions,
                                  continuous_sneezing,
                                  shivering,
                                  chills,
                                  joint_pain,
                                  stomach_pain,
                                  acidity,
                                  ulcers_on_tongue,
                                  muscle_wasting,
                                  vomiting,
                                  burning_micturition,
                                  spotting_urination,
                                  fatigue,
                                  weight_gain,
                                  anxiety,
                                  cold_hands_and_feets,
                                  mood_swings,
                                  weight_loss,
                                  restlessness,
                                  lethargy,
                                  patches_in_throat,
                                  irregular_sugar_level,
                                  cough,
                                  high_fever,
                                  sunken_eyes,
                                  breathlessness,
                                  sweating,
                                  dehydration,
                                  indigestion,
                                  headache,
                                  yellowish_skin,dark_urine,
                                  nausea,
                                  loss_of_appetite,
                                  pain_behind_the_eyes,
                                  back_pain,constipation,
                                  abdominal_pain,
                                  diarrhoea,
                                  mild_fever,
                                  yellow_urine,
                                  yellowing_of_eyes,
                                  acute_liver_failure,
                                  fluid_overload,
                                  welling_of_stomach,
                                  swelled_lymph_nodes,
                                  malaise,
                                  blurred_and_distorted_vision,
                                  phlegm,
                                  throat_irritation,
                                  redness_of_eyes,
                                  sinus_pressure,
                                  runny_nose,
                                  congestion,
                                  chest_pain,
                                  weakness_in_limbs,
                                  fast_heart_rate,
                                  pain_during_bowel_movements,
                                  pain_in_anal_region,
                                  bloody_stool,
                                  irritation_in_anus,
                                  neck_pain,
                                  dizziness,
                                  cramps,
                                  bruising,
                                  obesity,
                                  swollen_legs,
                                  swollen_blood_vessels,
                                  puffy_face_and_eyes,
                                  enlarged_thyroid,
                                  brittle_nails,
                                  swollen_extremeties,
                                  excessive_hunger,
                                  extra_marital_contacts,
                                  drying_and_tingling_lips,
                                  slurred_speech,
                                  knee_pain,
                                  hip_joint_pain,
                                  muscle_weakness,
                                  stiff_neck,
                                  swelling_joints,
                                  movement_stiffness,
                                  spinning_movements,
                                  loss_of_balance,
                                  unsteadiness,
                                  weakness_of_one_body_side,
                                  loss_of_smell,
                                  bladder_discomfort,
                                  foul_smell_of_urine,
                                  continuous_feel_of_urine,
                                  passage_of_gases,
                                  internal_itching,
                                  toxic_look_typhos,
                                  depression,
                                  irritability,
                                  muscle_pain,
                                  altered_sensorium,
                                  red_spots_over_body,
                                  belly_pain,
                                  abnormal_menstruation,
                                  dischromic_patches,
                                  watering_from_eyes,
                                  increased_appetite,
                                  polyuria,
                                  family_history,
                                  mucoid_sputum,
                                  rusty_sputum,
                                  lack_of_concentration,
                                  visual_disturbances,
                                  receiving_blood_transfusion,
                                  receiving_unsterile_injections,
                                  coma,
                                  stomach_bleeding,
                                  distention_of_abdomen,
                                  history_of_alcohol_consumption,
                                  fluid_overload,
                                  blood_in_sputum,
                                  prominent_veins_on_calf,
                                  palpitations,
                                  painful_walking,
                                  pus_filled_pimples,
                                  blackheads,
                                  scurring,
                                  skin_peeling,
                                  silver_like_dusting,
                                  small_dents_in_nails,
                                  inflammatory_nails,blister,
                                  red_sore_around_nose]
    setlist=set(l)  
    for element in setlist:
    # counting the frequency of element if it is greater than 1 then print it
        frequency = l.count(element)
        if(frequency > 1):
        # print the element and frequency
            #st.write('element =', element, 'frequency :', frequency)
            if element==0 and (frequency==131 or frequency==130 or  frequency==129 or  frequency==129):
                st.warning("Please select multiple symptoms for accurate prediction")
            
            if element==1 and frequency>=3:
                if st.button("Anticipated illness"):
                    Diagnosis=disease_prediction([itching,
                                                  skin_rash,
                                                  nodal_skin_eruptions,
                                                  continuous_sneezing,
                                                  shivering,
                                                  chills,
                                                  joint_pain,
                                                  stomach_pain,
                                                  acidity,
                                                  ulcers_on_tongue,
                                                  muscle_wasting,
                                                  vomiting,
                                                  burning_micturition,
                                                  spotting_urination,
                                                  fatigue,
                                                  weight_gain,
                                                  anxiety,
                                                  cold_hands_and_feets,
                                                  mood_swings,
                                                  weight_loss,
                                                  restlessness,
                                                  lethargy,
                                                  patches_in_throat,
                                                  irregular_sugar_level,
                                                  cough,
                                                  high_fever,
                                                  sunken_eyes,
                                                  breathlessness,
                                                  sweating,
                                                  dehydration,
                                                  indigestion,
                                                  headache,
                                                  yellowish_skin,dark_urine,
                                                  nausea,
                                                  loss_of_appetite,
                                                  pain_behind_the_eyes,
                                                  back_pain,constipation,
                                                  abdominal_pain,
                                                  diarrhoea,
                                                  mild_fever,
                                                  yellow_urine,
                                                  yellowing_of_eyes,
                                                  acute_liver_failure,
                                                  fluid_overload,
                                                  welling_of_stomach,
                                                  swelled_lymph_nodes,
                                                  malaise,
                                                  blurred_and_distorted_vision,
                                                  phlegm,
                                                  throat_irritation,
                                                  redness_of_eyes,
                                                  sinus_pressure,
                                                  runny_nose,
                                                  congestion,
                                                  chest_pain,
                                                  weakness_in_limbs,
                                                  fast_heart_rate,
                                                  pain_during_bowel_movements,
                                                  pain_in_anal_region,
                                                  bloody_stool,
                                                  irritation_in_anus,
                                                  neck_pain,
                                                  dizziness,
                                                  cramps,
                                                  bruising,
                                                  obesity,
                                                  swollen_legs,
                                                  swollen_blood_vessels,
                                                  puffy_face_and_eyes,
                                                  enlarged_thyroid,
                                                  brittle_nails,
                                                  swollen_extremeties,
                                                  excessive_hunger,
                                                  extra_marital_contacts,
                                                  drying_and_tingling_lips,
                                                  slurred_speech,
                                                  knee_pain,
                                                  hip_joint_pain,
                                                  muscle_weakness,
                                                  stiff_neck,
                                                  swelling_joints,
                                                  movement_stiffness,
                                                  spinning_movements,
                                                  loss_of_balance,
                                                  unsteadiness,
                                                  weakness_of_one_body_side,
                                                  loss_of_smell,
                                                  bladder_discomfort,
                                                  foul_smell_of_urine,
                                                  continuous_feel_of_urine,
                                                  passage_of_gases,
                                                  internal_itching,
                                                  toxic_look_typhos,
                                                  depression,
                                                  irritability,
                                                  muscle_pain,
                                                  altered_sensorium,
                                                  red_spots_over_body,
                                                  belly_pain,
                                                  abnormal_menstruation,
                                                  dischromic_patches,
                                                  watering_from_eyes,
                                                  increased_appetite,
                                                  polyuria,
                                                  family_history,
                                                  mucoid_sputum,
                                                  rusty_sputum,
                                                  lack_of_concentration,
                                                  visual_disturbances,
                                                  receiving_blood_transfusion,
                                                  receiving_unsterile_injections,
                                                  coma,
                                                  stomach_bleeding,
                                                  distention_of_abdomen,
                                                  history_of_alcohol_consumption,
                                                  fluid_overload,
                                                  blood_in_sputum,
                                                  prominent_veins_on_calf,
                                                  palpitations,
                                                  painful_walking,
                                                  pus_filled_pimples,
                                                  blackheads,
                                                  scurring,
                                                  skin_peeling,
                                                  silver_like_dusting,
                                                  small_dents_in_nails,
                                                  inflammatory_nails,blister,
                                                  red_sore_around_nose,
                                                  yellow_crust_ooze])
                    
                    
                    
                    st.success("There are the chances you may have")
                    st.success(Diagnosis)
            else:
                if element==1 and frequency<2:
                    st.warning("Please select multiple symptoms for accurate prediction")
                
           
           
                               

    
        
        
        





if __name__=='__main__':
    main()
    
  
