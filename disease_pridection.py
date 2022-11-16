# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:49:43 2022

@author: 91996
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
    
    col1,col2,col3,col4=st.columns(4)
    
    
    itching =int(col1.checkbox("itching"))
    skin_rash=int(col1.checkbox("skin_rash"))
    nodal_skin_eruptions=int(col1.checkbox("nodal_skin_eruptions"))
    continuous_sneezing=int(col1.checkbox("continuous_sneezing"))
    shivering=int(col1.checkbox("shivering"))
    chills=int(col1.checkbox("chills"))
    joint_pain=int(col1.checkbox("joint_pain"))
    stomach_pain=int(col1.checkbox("stomach_pain"))
    acidity=int(col1.checkbox("acidity"))
    ulcers_on_tongue=int(col1.checkbox("ulcers_on_tongue"))
    muscle_wasting=int(col1.checkbox("muscle_wasting"))
    vomiting=int(col1.checkbox("vomiting"))
    burning_micturition=int(col1.checkbox("burning_micturition"))
    spotting_urination=int(col1.checkbox("spotting_urination"))
    fatigue=int(col1.checkbox("fatigue"))
    weight_gain=int(col1.checkbox("weight_gain"))
    anxiety=int(col1.checkbox("anxiety"))
    cold_hands_and_feets=int(col1.checkbox("cold_hands_and_feets"))
    mood_swings=int(col1.checkbox("mood_swings"))
    weight_loss=int(col1.checkbox("weight_los"))
    restlessness=int(col1.checkbox("restlessness"))
    lethargy=int(col1.checkbox("lethargy"))
    patches_in_throat=int(col1.checkbox("patches_in_throa"))
    irregular_sugar_level=int(col1.checkbox("irregular_sugar_level"))
    cough=int(col1.checkbox("cough"))
    high_fever=int(col2.checkbox("high_fever"))
    sunken_eyes=int(col2.checkbox("sunken_eyes"))
    breathlessness=int(col2.checkbox("breathlessness"))
    sweating=int(col2.checkbox("sweating"))
    dehydration=int(col2.checkbox("dehydration"))
    indigestion=int(col2.checkbox("indigestion"))
    headache=int(col2.checkbox("headache"))
    yellowish_skin=int(col2.checkbox(" yellowish_skin"))
    dark_urine=int(col2.checkbox("dark_urine"))
    nausea=int(col2.checkbox("nausea"))
    loss_of_appetite=int(col2.checkbox("loss_of_appetite"))
    pain_behind_the_eyes=int(col2.checkbox("pain_behind_the_eyes"))
    back_pain=int(col2.checkbox("back_pain"))
    constipation=int(col2.checkbox("constipation"))
    abdominal_pain=int(col2.checkbox("abdominal_pain"))
    diarrhoea=int(col2.checkbox("diarrhoea"))
    mild_fever=int(col2.checkbox("mild_fever"))
    yellow_urine=int(col2.checkbox("yellow_urine"))
    yellowing_of_eyes=int(col2.checkbox("yellowing_of_eyes"))
    acute_liver_failure=int(col2.checkbox("acute_liver_failure"))
    fluid_overload=int(col2.checkbox("fluid_overload"))
    welling_of_stomach=int(col2.checkbox("welling_of_stomach"))
    swelled_lymph_nodes=int(col2.checkbox("swelled_lymph_nodes"))
    malaise=int(col2.checkbox("malaise"))
    blurred_and_distorted_vision=int(col2.checkbox("blurred_and_distorted_vision"))
    phlegm=int(col3.checkbox("phlegm"))
    throat_irritation=int(col3.checkbox("throat_irritation"))
    redness_of_eyes=int(col3.checkbox("redness_of_eyes"))
    sinus_pressure=int(col3.checkbox("sinus_pressure"))
    runny_nose=int(col3.checkbox("runny_nose"))
    congestion=int(col3.checkbox("congestion"))
    chest_pain=int(col3.checkbox("chest_pain"))
    weakness_in_limbs=int(col3.checkbox("weakness_in_limbs"))
    fast_heart_rate=int(col3.checkbox("fast_heart_rate"))
    pain_during_bowel_movements=int(col3.checkbox("pain_during_bowel_movements"))
    pain_in_anal_region=int(col3.checkbox("pain_in_anal_region"))
    bloody_stool=int(col3.checkbox("bloody_stool"))
    irritation_in_anus=int(col3.checkbox("irritation_in_anus"))
    neck_pain=int(col3.checkbox("neck_pain"))
    dizziness=int(col3.checkbox("dizziness"))
    cramps=int(col3.checkbox("cramps"))
    bruising=int(col3.checkbox("bruising"))
    obesity=int(col3.checkbox("obesity"))
    swollen_legs=int(col3.checkbox("swollen_legs"))
    swollen_blood_vessels=int(col3.checkbox("swollen_blood_vessels"))
    puffy_face_and_eyes=int(col3.checkbox("puffy_face_and_eyes"))
    enlarged_thyroid=int(col3.checkbox("enlarged_thyroid"))
    brittle_nails=int(col3.checkbox("brittle_nails"))
    swollen_extremeties=int(col3.checkbox("swollen_extremeties"))
    excessive_hunger=int(col3.checkbox("excessive_hunger"))
    extra_marital_contacts=int(col4.checkbox("extra_marital_contacts"))
    drying_and_tingling_lips=int(col4.checkbox("drying_and_tingling_lips"))
    slurred_speech=int(col4.checkbox("slurred_speech"))
    knee_pain=int(col4.checkbox("knee_pain"))
    hip_joint_pain=int(col4.checkbox("hip_joint_pain"))
    muscle_weakness=int(col4.checkbox("muscle_weakness"))
    stiff_neck=int(col4.checkbox("stiff_neck"))
    swelling_joints=int(col4.checkbox("swelling_joints"))
    movement_stiffness=int(col4.checkbox("movement_stiffness"))
    spinning_movements=int(col4.checkbox("spinning_movements"))
    loss_of_balance=int(col4.checkbox("loss_of_balance"))
    unsteadiness=int(col4.checkbox("unsteadiness"))
    weakness_of_one_body_side=int(col4.checkbox("weakness_of_one_body_side"))
    loss_of_smell=int(col4.checkbox("loss_of_smell"))
    bladder_discomfort=int(col4.checkbox("bladder_discomfort"))
    foul_smell_of_urine=int(col4.checkbox("foul_smell_of_urine"))
    continuous_feel_of_urine=int(col4.checkbox("continuous_feel_of_urine"))
    passage_of_gases=int(col4.checkbox("passage_of_gases"))
    internal_itching=int(col4.checkbox("internal_itching"))
    toxic_look_typhos=int(col4.checkbox("toxic_look_typhos"))
    depression=int(col4.checkbox("depression"))
    irritability=int(col4.checkbox("irritability"))
    muscle_pain=int(col4.checkbox("muscle_pain"))
    altered_sensorium=int(col4.checkbox("altered_sensorium"))
    red_spots_over_body=int(col4.checkbox("red_spots_over_body"))
    belly_pain=int(col1.checkbox("belly_pain"))
    abnormal_menstruation=int(col1.checkbox("abnormal_menstruation"))
    dischromic_patches=int(col1.checkbox("dischromic_patches"))
    watering_from_eyes=int(col1.checkbox("watering_from_eyes"))
    increased_appetite=int(col1.checkbox("increased_appetite"))
    polyuria=int(col1.checkbox("polyuria"))
    family_history=int(col1.checkbox("family_history"))
    mucoid_sputum=int(col1.checkbox("mucoid_sputum"))
    rusty_sputum=int(col1.checkbox("rusty_sputum"))
    lack_of_concentration=int(col1.checkbox("lack_of_concentration"))
    visual_disturbances=int(col2.checkbox("visual_disturbances"))
    receiving_blood_transfusion=int(col2.checkbox("receiving_blood_transfusion"))
    receiving_unsterile_injections=int(col2.checkbox("receiving_unsterile_injections"))
    coma=int(col2.checkbox("coma"))
    stomach_bleeding=int(col2.checkbox("stomach_bleeding"))
    distention_of_abdomen=int(col2.checkbox("distention_of_abdomen"))
    history_of_alcohol_consumption=int(col2.checkbox("history_of_alcohol_consumption"))
    fluid_overload=int(col2.checkbox("fluid_over_load"))
    blood_in_sputum=int(col2.checkbox("blood_in_sputum"))
    prominent_veins_on_calf=int(col2.checkbox("prominent_veins_on_calf"))
    palpitations=int(col3.checkbox("palpitations"))
    painful_walking=int(col3.checkbox("painful_walking"))
    pus_filled_pimples=int(col3.checkbox("pus_filled_pimples"))
    blackheads=int(col3.checkbox("blackheads"))
    scurring=int(col3.checkbox("scurring"))
    skin_peeling=int(col3.checkbox("skin_peeling"))
    silver_like_dusting=int(col3.checkbox("silver_like_dusting"))
    small_dents_in_nails=int(col3.checkbox("small_dents_in_nails"))
    inflammatory_nails=int(col3.checkbox("inflammatory_nails"))
    blister=int(col3.checkbox("blister"))
    red_sore_around_nose=int(col4.checkbox("red_sore_around_nose"))
    yellow_crust_ooze=int(col4.checkbox("yellow_crust_ooze"))
    
    
    
    Diagnosis=''
    
   
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
        
    if st.button("Result"):
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
        
        
        
        
        st.success(Diagnosis)
        
        
        





if __name__=='__main__':
    main()
    
  
