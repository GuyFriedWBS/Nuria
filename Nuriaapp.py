import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline

#Loading data
# training2
url = "https://drive.google.com/file/d/19-xEfVfvART7dM5OgR5yVcrH8KPZ5AaR/view?usp=drive_link"
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
training2 = pd.read_csv(path)
training2 = training2.drop(["Unnamed: 133"],axis=1)
training2.drop_duplicates(inplace=True)

#splitting the data
x = training2.drop('prognosis',axis=1)
y = training2['prognosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=101)

#creating a model
# Define the model with specific hyperparameters
model = RandomForestClassifier(
    ccp_alpha=0.0,
    max_depth=None,
    min_samples_leaf=1,
    n_estimators=100,
    random_state=42
)

# Train the model
model2 = model.fit(x_train, y_train)

# Load the model
#saved_model = pickle.load(open('guymodel.sav', 'rb'))

# Assuming 'values' is defined somewhere in your code
columns = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
           'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
           'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain',
           'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
           'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever',
           'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
           'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
           'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
           'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
           'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
           'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion',
           'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements',
           'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness',
           'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels',
           'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
           'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech',
           'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
           'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
           'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
           'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
           'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
           'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes',
           'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum',
           'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
           'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
           'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum',
           'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples',
           'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
           'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

# Create selectboxes for each feature
selected_symptoms = st.multiselect("Select a symptom", columns)

# Create a DataFrame with one row of zeros
df_user = pd.DataFrame([[0] * len(columns)], columns=columns)

# Update the DataFrame based on selected symptoms
for symptom in selected_symptoms:
    if symptom in df_user.columns:
        df_user.loc[0, symptom] = 1

# Display the updated DataFrame
df_user

# Make a prediction
prediction = model2.predict(df_user)

# Display the prediction
st.write("The predicted probability of the disease is:", prediction)
