from rest_framework import views, status, viewsets
import os
import joblib
from django.conf import settings
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class LoginView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

class LogoutView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (1).pkl')
model_1 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (1).pkl')
scaler_1 = joblib.load(scaler_path)

neighborhoods = [
    'Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor',
    'Edwards', 'Gilbert', 'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes',
    'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt', 'OldTown', 'SWISU',
    'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker'
]

class HouseAPIView(views.APIView):

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_neighborhood = data.get('Neighborhood')
            neighborhood1or_0 = [1 if new_neighborhood == i else 0 for i in neighborhoods]

            features = [data['GrLivArea'],
                        data['YearBuilt'],
                        data['GarageCars'],
                        data['TotalBsmtSF'],
                        data['FullBath'],
                        data['OverallQual'],
                        ] + neighborhood1or_0
            scaled_data = scaler_1.transform([features])
            predict = model_1.predict(scaled_data)[0]
            house = serializer.save(predicted_price=round(predict))
            return Response({'data': HouseSerializer(house).data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (3).pkl')
model_3 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (3).pkl')
scaler_3 = joblib.load(scaler_path)

class DiabetesAPIView(views.APIView):

    def post(self, request):
        serializer = DiabetesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = list(data.values())

            scaled_data = scaler_3.transform([features])
            predict = model_3.predict(scaled_data)[0]
            prob = model_3.predict_proba(scaled_data)[0][1]

            diabetes_data = serializer.save(
                predict=bool(predict),
                probability=float(prob)
            )

            return Response(
                {'data': DiabetesSerializer(diabetes_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (2).pkl')
model_2 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (2).pkl')
scaler_2 = joblib.load(scaler_path)

education_list = ['Bachelor', 'Doctorate', 'High School', 'Master']
home_ownership_list = ['OTHER', 'OWN', 'RENT']
loan_intent_list = ['EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE']

def build_features_bank(data):
    numeric = [
        data['person_age'],
        data['person_income'],
        data['person_emp_exp'],
        data['loan_amnt'],
        data['loan_int_rate'],
        data['loan_percent_income'],
        data['cb_person_cred_hist_length'],
        data['credit_score'],
    ]

    gender = [1 if data['person_gender'] == 'male' else 0]

    education = [1 if data['person_education'] == i else 0 for i in education_list]

    home_ownership = [1 if data['person_home_ownership'] == i else 0 for i in home_ownership_list]

    loan_intent = [1 if data['loan_intent'] == i else 0 for i in loan_intent_list]

    prev_default = [1 if data['previous_loan_defaults_on_file'] == 'Yes' else 0]

    return numeric + gender + education + home_ownership + loan_intent + prev_default

class BankAPIView(views.APIView):

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = build_features_bank(data)

            scaled_data = scaler_2.transform([features])
            predict = model_2.predict(scaled_data)[0]
            prob = model_2.predict_proba(scaled_data)[0][1]

            bank_data = serializer.save(
                predict=int(predict),
                probability=float(prob)
            )

            return Response(
                {'data': BankSerializer(bank_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (6).pkl')
model_6 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (6).pkl')
scaler_6 = joblib.load(scaler_path)

tree_path = os.path.join(settings.BASE_DIR, 'pkl/tree_model.pkl')
tree = joblib.load(tree_path)

cap_shape_list = ["c", "f", "k", "s", "x"]
cap_surface_list = ["g", "s", "y"]
cap_color_list = ["c", "e", "g", "n", "p", "r", "u", "w", "y"]
odor_list = ["c", "f", "l", "m", "n", "p", "s", "y"]
gill_color_list = ["e", "g", "h", "k", "n", "o", "p", "r", "u", "w", "y"]
stalk_root_list = ["c", "e", "r"]
stalk_surface_list = ['k', 's', 'y']
stalk_color_list = ["c", "e", "g", "n", "o", "p", "w", "y"]
veil_color_list = ["o", "w", "y"]
ring_number_list = ['o', 't']
ring_type_list = ['f', 'l', 'n', 'p']
spore_print_color_list = ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y']
population_list = ['c', 'n', 's', 'v', 'y']
habitat_list = ['g', 'l', 'm', 'p', 'u', 'w']

def build_features_mushrooms(data):
    cap_shape = [
        1 if data['cap_shape'] == i else 0 for i in cap_shape_list
    ]

    cap_surface = [
        1 if data['cap_surface'] == i else 0 for i in cap_surface_list
    ]

    cap_color = [
        1 if data['cap_color'] == i else 0 for i in cap_color_list
    ]

    bruises = [1 if data['bruises'] == "t" else 0]

    odor = [
        1 if data['odor'] == i else 0 for i in odor_list
    ]

    gill_attachment = [1 if data['gill_attachment'] == "f" else 0]

    gill_spacing = [1 if data['gill_spacing'] == "w" else 0]

    gill_size = [1 if data['gill_size'] == "n" else 0]

    gill_color = [
        1 if data['gill_color'] == i else 0 for i in gill_color_list
    ]

    stalk_shape = [1 if data['stalk_shape'] == "t" else 0]

    stalk_root = [
        1 if data['stalk_root'] == i else 0 for i in stalk_root_list
    ]

    stalk_surface_above = [
        1 if data['stalk_surface_above_ring'] == i else 0 for i in stalk_surface_list
    ]

    stalk_surface_below = [
        1 if data['stalk_surface_below_ring'] == i else 0 for i in stalk_surface_list
    ]

    stalk_color_above = [
        1 if data['stalk_color_above_ring'] == i else 0 for i in stalk_color_list
    ]

    stalk_color_below = [
        1 if data['stalk_color_below_ring'] == i else 0 for i in stalk_color_list
    ]

    veil_color = [
        1 if data['veil_color'] == i else 0 for i in veil_color_list
    ]

    ring_number = [
        1 if data['ring_number'] == i else 0 for i in ring_number_list
    ]

    ring_type = [
        1 if data['ring_type'] == i else 0 for i in ring_type_list
    ]

    spore_print = [
        1 if data['spore_print_color'] == i else 0 for i in spore_print_color_list
    ]

    population = [
        1 if data['population'] == i else 0 for i in population_list
    ]

    habitat = [
        1 if data['habitat'] == i else 0 for i in habitat_list
    ]

    return (cap_shape + cap_surface + cap_color + bruises + odor + gill_attachment +
            gill_spacing + gill_size + gill_color + stalk_shape + stalk_root +
            stalk_surface_above + stalk_surface_below + stalk_color_above +
            stalk_color_below + veil_color + ring_number + ring_type +
            spore_print + population + habitat)

class MushroomLogisticAPIView(views.APIView):

    def post(self, request):
        serializer = MushroomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = build_features_mushrooms(data)
            scaled_data = scaler_6.transform([features])

            predict = model_6.predict(scaled_data)[0]
            prob = model_6.predict_proba(scaled_data)[0][1]

            mushroom_data = serializer.save(
                poisonous=bool(predict),
                probability=float(prob)
            )

            return Response(
                {'data': MushroomSerializer(mushroom_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MushroomTreeAPIView(views.APIView):

    def post(self, request):
        serializer = MushroomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = build_features_mushrooms(data)

            predict = tree.predict([features])[0]
            prob = tree.predict_proba([features])[0][1]

            mushroom_data = serializer.save(
                poisonous=bool(predict),
                probability=float(prob)
            )

            return Response(
                {'data': MushroomSerializer(mushroom_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (5).pkl')
model_5 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (5).pkl')
scaler_5 = joblib.load(scaler_path)

color_list = ['dark green', 'green', 'purple']

class AvocadoAPIView(views.APIView):

    def post(self, request):
        serializer = AvocadoSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            color = data.get('color_category')
            color1or_0 = [1 if color == i else 0 for i in color_list]

            features = (
                [data['firmness'],
                 data['hue'],
                 data['saturation'],
                 data['brightness'],
                 data['sound_db'],
                 data['weight_g'],
                 data['size_cm3']
                 ] + color1or_0
            )

            scaled_data = scaler_5.transform([features])
            predict = model_5.predict(scaled_data)[0]
            prob = model_5.predict_proba(scaled_data)[0][1]

            avocado_data = serializer.save(
                predict=predict,
                probability=float(prob)
            )

            return Response(
                {'data': AvocadoSerializer(avocado_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (7).pkl')
model_7 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (7).pkl')
scaler_7 = joblib.load(scaler_path)

MultipleLines_list = ['No phone service', 'Yes']
InternetService_list = ['Fiber optic', 'No']
OnlineSecurity_list = ['No internet service', 'Yes']
OnlineBackup_list = ['No internet service', 'Yes']
DeviceProtection_list = ['No internet service', 'Yes']
TechSupport_list = ['No internet service', 'Yes']
StreamingTV_list = ['No internet service', 'Yes']
StreamingMovies_list = ['No internet service', 'Yes']
Contract_list = ['One year', 'Two year']
PaymentMethod_list = ['Credit card (automatic)', 'Electronic check', 'Mailed check']

def build_features(data):

    numeric = [
        data['SeniorCitizen'],
        data['tenure'],
        data['MonthlyCharges'],
        data['TotalCharges']
    ]

    gender = [1 if data['gender'] == 'male' else 0]

    partner = [1 if data['Partner'] == 'Yes' else 0]

    dependents = [1 if data['Dependents'] == 'Yes' else 0]

    phone_service = [1 if data['PhoneService'] == 'Yes' else 0]

    multiple_lines = [1 if data['MultipleLines'] == i else 0 for i in MultipleLines_list]

    internet_service = [1 if data['InternetService'] == i else 0 for i in InternetService_list]

    online_security = [1 if data['OnlineSecurity'] == i else 0 for i in OnlineSecurity_list]

    online_backup = [1 if data['OnlineBackup'] == i else 0 for i in OnlineBackup_list]

    device_protection = [1 if data['DeviceProtection'] == i else 0 for i in DeviceProtection_list]

    tech_support = [1 if data['TechSupport'] == i else 0 for i in TechSupport_list]

    streaming_tv = [1 if data['StreamingTV'] == i else 0 for i in StreamingTV_list]

    streaming_movies = [1 if data['StreamingMovies'] == i else 0 for i in StreamingMovies_list]

    contract = [1 if data['Contract'] == i else 0 for i in Contract_list]

    paper_less_billing = [1 if data['PaperlessBilling'] == 'Yes' else 0]

    payment_method = [1 if data['PaymentMethod'] == i else 0 for i in PaymentMethod_list]

    return (numeric + gender + partner + dependents + phone_service + multiple_lines +
            internet_service + online_security + online_backup + device_protection +
            tech_support + streaming_tv + streaming_movies + contract + paper_less_billing + payment_method)

class TelecomAPIView(views.APIView):

    def post(self, request):
        serializer = TelecomSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            features = build_features(data)

            scaled_data = scaler_7.transform([features])
            predict = model_7.predict(scaled_data)[0]
            prob = model_7.predict_proba(scaled_data)[0][1]

            telecom_data = serializer.save(
                churn=bool(predict),
                probability=float(prob)
            )

            return Response(
                {'data': TelecomSerializer(telecom_data).data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


model_path = os.path.join(settings.BASE_DIR, 'pkl/model (4).pkl')
model_4 = joblib.load(model_path)

scaler_path = os.path.join(settings.BASE_DIR, 'pkl/scaler (4).pkl')
scaler_4 = joblib.load(scaler_path)

race_list = ['group B', 'group C', 'group D', 'group E']
parental_list = ["bachelor's degree", 'high school', "master's degree", 'some college', 'some high school']

class StudentsAPIView(views.APIView):

    def post(self, request):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            gender = data.get('gender')
            gender1or_0 = [1 if gender == 'male' else 0]

            race = data.get('race_ethnicity')
            race1or_0 = [1 if race == i else 0 for i in race_list]

            parental = data.get('parental_level_of_education')
            parental1or_0 = [1 if parental == i else 0 for i in parental_list]

            lunch = data.get('lunch')
            lunch1or_0 = [1 if lunch == 'standard' else 0]

            test = data.get('test_preparation_course')
            test1or_0 = [1 if test == 'none' else 0]

            features = (
                    [data['math_score'], data['reading_score']] +
                    gender1or_0 +
                    race1or_0 +
                    parental1or_0 +
                    lunch1or_0 +
                    test1or_0
            )

            scaled_data = scaler_4.transform([features])
            predict = model_4.predict(scaled_data)[0]
            student = serializer.save(predict=predict)
            return Response({'data': StudentsSerializer(student).data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)