from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.registered_date}'

class Telecom(models.Model):
    gender = models.CharField(max_length=64)
    SeniorCitizen = models.IntegerField()
    Partner = models.CharField(max_length=64)
    Dependents = models.CharField(max_length=64)
    tenure = models.IntegerField()
    PhoneService = models.CharField(max_length=64)
    MultipleLines = models.CharField(max_length=64)
    InternetService = models.CharField(max_length=64)
    OnlineSecurity = models.CharField(max_length=64)
    OnlineBackup = models.CharField(max_length=64)
    DeviceProtection = models.CharField(max_length=64)
    TechSupport = models.CharField(max_length=64)
    StreamingTV = models.CharField(max_length=64)
    StreamingMovies = models.CharField(max_length=64)
    Contract = models.CharField(max_length=64)
    PaperlessBilling = models.CharField(max_length=64)
    PaymentMethod = models.CharField(max_length=64)
    MonthlyCharges = models.FloatField()
    TotalCharges = models.FloatField()
    churn = models.BooleanField(null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.churn}%'

class Students(models.Model):
    gender = models.CharField(max_length=64)
    race_ethnicity = models.CharField(max_length=64)
    parental_level_of_education = models.CharField(max_length=64)
    lunch = models.CharField(max_length=64)
    test_preparation_course = models.CharField(max_length=64)
    math_score = models.IntegerField()
    reading_score = models.IntegerField()
    predict = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.predict}%'

class Avocado(models.Model):
    firmness = models.FloatField()
    hue = models.IntegerField()
    saturation = models.IntegerField()
    brightness = models.IntegerField()
    sound_db = models.IntegerField()
    weight_g = models.IntegerField()
    size_cm3 = models.IntegerField()
    color_category = models.CharField(max_length=64)
    predict = models.CharField(null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.predict}%'

class Mushroom(models.Model):
    cap_shape = models.CharField(max_length=64)
    cap_surface = models.CharField(max_length=64)
    cap_color = models.CharField(max_length=64)
    bruises = models.CharField(max_length=64)
    odor = models.CharField(max_length=64)
    gill_attachment = models.CharField(max_length=64)
    gill_spacing = models.CharField(max_length=64)
    gill_size = models.CharField(max_length=64)
    gill_color = models.CharField(max_length=64)
    stalk_shape = models.CharField(max_length=64)
    stalk_root = models.CharField(max_length=64)
    stalk_surface_above_ring = models.CharField(max_length=64)
    stalk_surface_below_ring = models.CharField(max_length=64)
    stalk_color_above_ring = models.CharField(max_length=64)
    stalk_color_below_ring = models.CharField(max_length=64)
    veil_color = models.CharField(max_length=64)
    ring_number = models.CharField(max_length=64)
    ring_type = models.CharField(max_length=64)
    spore_print_color = models.CharField(max_length=64)
    population = models.CharField(max_length=64)
    habitat = models.CharField(max_length=64)
    poisonous = models.BooleanField(null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.poisonous}%'

class Bank(models.Model):
    person_age = models.IntegerField()
    person_income = models.IntegerField()
    person_emp_exp = models.IntegerField()
    loan_amnt = models.IntegerField()
    loan_int_rate = models.IntegerField()
    loan_percent_income = models.IntegerField()
    cb_person_cred_hist_length = models.IntegerField()
    credit_score = models.IntegerField()
    person_gender = models.CharField(max_length=64)
    person_education = models.CharField(max_length=64)
    person_home_ownership = models.CharField(max_length=64)
    loan_intent = models.CharField(max_length=64)
    previous_loan_defaults_on_file = models.CharField(max_length=64)
    predict = models.FloatField(null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.predict}%'

class Diabetes(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    predict = models.BooleanField(null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.predict}%'

class House(models.Model):
    GrLivArea = models.IntegerField()
    YearBuilt = models.IntegerField()
    GarageCars = models.IntegerField()
    TotalBsmtSF = models.IntegerField()
    FullBath = models.IntegerField()
    OverallQual = models.IntegerField()
    Neighborhood = models.CharField(max_length=64)
    predicted_price = models.FloatField(null=True, blank=True)