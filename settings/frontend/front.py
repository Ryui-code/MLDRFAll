import streamlit as st
import requests

st.title('Welcome!')

with st.sidebar:
    model = st.radio('Models', ['Avocado', 'Bank', 'Diabetes', 'House', 'Mushrooms',
                                     'Students', 'Telecom'])

if model == 'House':

    api = 'http://127.0.0.1:8000/house-model/'

    st.title('House Model')

    Neighborhood = st.selectbox(
        'Neighborhood',
        [
            'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor',
            'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes',
            'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 'OldTown', 'SWISU',
            'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker'
        ]
    )

    GrLivArea = st.number_input('GrLivArea', min_value=0.0, step=1.0)
    YearBuilt = st.number_input('YearBuilt', min_value=0.0, step=1.0)
    GarageCars = st.number_input('GarageCars', min_value=0.0, step=1.0)
    TotalBsmtSF = st.number_input('TotalBsmtSF', min_value=0.0, step=1.0)
    FullBath = st.number_input('FullBath', min_value=0.0, step=1.0)
    OverallQual = st.number_input('OverallQual', min_value=0.0, step=1.0)

    house_data = {
        'GrLivArea': GrLivArea,
        'YearBuilt': YearBuilt,
        'GarageCars': GarageCars,
        'TotalBsmtSF': TotalBsmtSF,
        'FullBath': FullBath,
        'OverallQual': OverallQual,
        'Neighborhood': Neighborhood
    }

    if st.button('Predict'):
        try:
            request = requests.post(api, json=house_data, timeout=10)
            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException:
            st.error('Can not connect to the API')

if model == 'Students':

    api = 'http://127.0.0.1:8000/students-model/'

    st.title('Student Performance Prediction')

    gender = st.selectbox('Gender', ['male', 'female'])

    race_ethnicity = st.selectbox(
        'Race / Ethnicity',
        ['group A', 'group B', 'group C', 'group D', 'group E']
    )

    parental_level_of_education = st.selectbox(
        'Parental level of education',
        ["bachelor's degree", 'high school', "master's degree",
         'some college', 'some high school']
    )

    lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])

    test_preparation_course = st.selectbox(
        'Test preparation course',
        ['none', 'completed']
    )

    math_score = st.number_input('Math score', min_value=0, max_value=100, step=1)
    reading_score = st.number_input('Reading score', min_value=0, max_value=100, step=1)

    student_dict = {
        'gender': gender,
        'race_ethnicity': race_ethnicity,
        'parental_level_of_education': parental_level_of_education,
        'lunch': lunch,
        'test_preparation_course': test_preparation_course,
        'math_score': math_score,
        'reading_score': reading_score
    }

    if st.button('Predict'):
        try:
            response = requests.post(api, json=student_dict)
            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted score: {result['predict']}")
            else:
                st.error(f"Error: {response.status_code}")
        except requests.exceptions.RequestException:
            st.error('Cannot connect to the API')

if model == 'Bank':

    api = 'http://127.0.0.1:8000/bank-model/'

    st.title('Bank Project')

    person_age = st.number_input('Age', min_value=18.0, max_value=100.0, step=1.0)

    person_income = st.number_input('Person income', min_value=0.0, step=1000.0)

    person_emp_exp = st.number_input('Experience', min_value=0.0, step=1.0)

    loan_amnt = st.number_input('Loan amount score', min_value=0.0, step=100.0)

    loan_int_rate = st.number_input('Loan intent rate', min_value=0.0, step=1.0)

    loan_percent_income = st.number_input('Loan percent income', min_value=0.0, step=500.0)

    cb_person_cred_hist_length = st.number_input('Credit history length', min_value=0.0, step=1.0)

    credit_score = st.number_input('Credit score', min_value=0.0, step=10.0)

    person_gender = st.selectbox('Gender', ['Male', 'Female'])

    person_education = st.selectbox('Education', ['Bachelor', 'Doctorate', 'High School', 'Master', 'Associate'])

    person_home_ownership = st.selectbox('Home Ownership', ['OTHER', 'OWN', 'RENT', 'MORTGAGE'])

    loan_intent = st.selectbox('Loan intent',
                               ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE', 'DEBTCONSOLIDATION'])

    previous_loan_defaults_on_file = st.selectbox('Default', ['Yes', 'No'])

    bank_data = {
        'person_age': person_age,
        'person_income': person_income,
        'person_emp_exp': person_emp_exp,
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_percent_income': loan_percent_income,
        'cb_person_cred_hist_length': cb_person_cred_hist_length,
        'credit_score': credit_score,
        'person_gender': person_gender,
        'person_education': person_education,
        'person_home_ownership': person_home_ownership,
        'loan_intent': loan_intent,
        'previous_loan_defaults_on_file': previous_loan_defaults_on_file
    }

    if st.button('Check'):
        try:
            request = requests.post(api, json=bank_data, timeout=10)
            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException as e:
            st.error(f'Can not connect to the API')

if model == 'Diabetes':

    api = 'http://127.0.0.1:8000/diabetes-model/'

    st.title('Diabetes Model')

    Pregnancies = st.number_input('Pregnancies', min_value=0.0, step=1.0)

    Glucose = st.number_input('Glucose', min_value=0.0, step=1.0)

    BloodPressure = st.number_input('BloodPressure', min_value=0.0, step=1.0)

    SkinThickness = st.number_input('SkinThickness', min_value=0.0, step=1.0)

    Insulin = st.number_input('Insulin', min_value=0.0, step=1.0)

    BMI = st.number_input('BMI', min_value=0.0, step=0.1)

    DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, step=0.01)

    Age = st.number_input('Age', min_value=0.0, step=1.0)

    diabetes_dict = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }

    if st.button('Check'):
        try:
            request = requests.post(api, json=diabetes_dict)
            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException:
            st.error('Can not connect to the api')

if model == 'Avocado':

    api = 'http://127.0.0.1:8000/avocado-model/'

    st.title('Avocado Model')

    firmness = st.number_input('Firmness', min_value=0.0, step=1.0)

    hue = st.number_input('Hue', min_value=0.0, step=1.0)

    saturation = st.number_input('Saturation', min_value=0.0, step=1.0)

    brightness = st.number_input('Brightness', min_value=0.0, step=1.0)

    color_category = st.selectbox('Color category', ['black', 'green', 'dark green', 'purple'])

    sound_db = st.number_input('Sound db', min_value=0.0, step=1.0)

    weight_g = st.number_input('Weight g', min_value=0.0, step=10.0)

    size_cm3 = st.number_input('Size cm3', min_value=0.0, step=10.0)

    avocado_dict = {
        'firmness': firmness,
        'hue': hue,
        'saturation': saturation,
        'brightness': brightness,
        'color_category': color_category,
        'sound_db': sound_db,
        'weight_g': weight_g,
        'size_cm3': size_cm3
    }

    if st.button('Check'):
        try:
            request = requests.post(api, json=avocado_dict)
            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException as e:
            st.error('Can not connect to the api')

if model == 'Mushrooms':

    api_log = 'http://127.0.0.1:8000/mushrooms-tree/'
    api_tree = 'http://127.0.0.1:8000/mushrooms-logistic/'

    st.title('Mushroom Model')

    cap_shape = st.selectbox('Cap shape', ["c", "f", "k", "s", "x"])
    cap_surface = st.selectbox('Cap surface', ["g", "s", "y"])
    cap_color = st.selectbox('Cap color', ["c", "e", "g", "n", "p", "r", "u", "w", "y"])
    bruises = st.selectbox('Bruises', ["t", "f"])
    odor = st.selectbox('Odor', ["c", "f", "l", "m", "n", "p", "s", "y"])
    gill_attachment = st.selectbox('Gill attachment', ["f", "a"])
    gill_spacing = st.selectbox('Gill spacing', ["w", "c"])
    gill_size = st.selectbox('Gill size', ["n", "b"])
    gill_color = st.selectbox('Gill color', ["e", "g", "h", "k", "n", "o", "p", "r", "u", "w", "y"])
    stalk_shape = st.selectbox('Stalk shape', ["t", "e"])
    stalk_root = st.selectbox('Stalk root', ["c", "e", "r"])
    stalk_surface_above_ring = st.selectbox('Stalk surface above ring', ['k', 's', 'y'])
    stalk_surface_below_ring = st.selectbox('Stalk surface below ring', ['k', 's', 'y'])
    stalk_color_above_ring = st.selectbox('Stalk color above ring', ["c", "e", "g", "n", "o", "p", "w", "y"])
    stalk_color_below_ring = st.selectbox('Stalk color below ring', ["c", "e", "g", "n", "o", "p", "w", "y"])
    veil_color = st.selectbox('Veil color', ["o", "w", "y"])
    ring_number = st.selectbox('Ring number', ['o', 't'])
    ring_type = st.selectbox('Ring type', ['f', 'l', 'n', 'p'])
    spore_print_color = st.selectbox('Spore print color', ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y'])
    population = st.selectbox('Population', ['c', 'n', 's', 'v', 'y'])
    habitat = st.selectbox('Habitat', ['g', 'l', 'm', 'p', 'u', 'w'])

    model_type = st.selectbox('Model', ['logistic', 'tree'])

    mushroom_dict = {
        'cap_shape': cap_shape,
        'cap_surface': cap_surface,
        'cap_color': cap_color,
        'bruises': bruises,
        'odor': odor,
        'gill_attachment': gill_attachment,
        'gill_spacing': gill_spacing,
        'gill_size': gill_size,
        'gill_color': gill_color,
        'stalk_shape': stalk_shape,
        'stalk_root': stalk_root,
        'stalk_surface_above_ring': stalk_surface_above_ring,
        'stalk_surface_below_ring': stalk_surface_below_ring,
        'stalk_color_above_ring': stalk_color_above_ring,
        'stalk_color_below_ring': stalk_color_below_ring,
        'veil_color': veil_color,
        'ring_number': ring_number,
        'ring_type': ring_type,
        'spore_print_color': spore_print_color,
        'population': population,
        'habitat': habitat
    }

    if st.button('Check'):
        try:
            url = api_log if model_type == 'logistic' else api_tree
            request = requests.post(url, json=mushroom_dict)

            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException:
            st.error('Can not connect to the api')

if model == 'Telecom':

    api = 'http://127.0.0.1:8000/telecom-model/'

    st.title('Telecom Churn Model')

    gender = st.selectbox('Gender', ['male', 'female'])
    SeniorCitizen = st.number_input('SeniorCitizen', min_value=0, step=1)
    Partner = st.selectbox('Partner', ['Yes', 'No'])
    Dependents = st.selectbox('Dependents', ['Yes', 'No'])
    tenure = st.number_input('Tenure', min_value=0, step=1)
    PhoneService = st.selectbox('PhoneService', ['Yes', 'No'])
    MultipleLines = st.selectbox('MultipleLines', ['No phone service', 'No', 'Yes'])
    InternetService = st.selectbox('InternetService', ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.selectbox('OnlineSecurity', ['No', 'Yes', 'No internet service'])
    OnlineBackup = st.selectbox('OnlineBackup', ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.selectbox('DeviceProtection', ['No', 'Yes', 'No internet service'])
    TechSupport = st.selectbox('TechSupport', ['No', 'Yes', 'No internet service'])
    StreamingTV = st.selectbox('StreamingTV', ['No', 'Yes', 'No internet service'])
    StreamingMovies = st.selectbox('StreamingMovies', ['No', 'Yes', 'No internet service'])
    Contract = st.selectbox('Contract', ['Month-to-month', 'One year', 'Two year'])
    PaperlessBilling = st.selectbox('PaperlessBilling', ['Yes', 'No'])
    PaymentMethod = st.selectbox(
        'PaymentMethod',
        ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    )
    MonthlyCharges = st.number_input('MonthlyCharges', min_value=0.0, step=1.0)
    TotalCharges = st.number_input('TotalCharges', min_value=0.0, step=1.0)

    telecom_dict = {
        'gender': gender,
        'SeniorCitizen': SeniorCitizen,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    if st.button('Check'):
        try:
            request = requests.post(api, json=telecom_dict)
            if request.status_code == 200:
                result = request.json()
                st.json(result)
            else:
                st.error(f'Error: {request.status_code}')
        except requests.exceptions.RequestException:
            st.error('Can not connect to the api')