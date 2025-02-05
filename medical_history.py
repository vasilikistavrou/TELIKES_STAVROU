from typing import Dict, Optional
from datetime import date, datetime


class PersonalData:
    """
    Represents the personal data of a patient, including basic details, contact information, 
    address, occupation, and emergency contact.
    """
    def __init__(
        self,
        name: str, 
        surname: str, 
        fathers_name: str, 
        mothers_name: str, 
        birthdate: date, 
        social_security_id: str, 
        tel_number: str, 
        email: str, 
        address: Dict[str, str], 
        occupation: str, 
        emergency_contact: Dict[str, str]
    ) -> None:
        """
        Initialize the personal data of a patient.

        Args:
            name (str): Patient's first name.
            surname (str): Patient's last name.
            fathers_name (str): Patient's father's name.
            mothers_name (str): Patient's mother's name.
            birthdate (date): Patient's date of birth.
            social_security_id (str): Patient's social security number.
            tel_number (str): Patient's telephone number.
            email (str): Patient's email address.
            address (dict): Patient's residential address with keys: 'street', 'city', 'state', 'postal_code', 'country'.
            occupation (str): Patient's occupation.
            emergency_contact (dict): Emergency contact information with keys: 'name' and 'tel_number'.
        """
        self.patients_name = name
        self.patients_surname = surname
        self.patients_fathers_name = fathers_name
        self.patients_mothers_name = mothers_name
        self.patients_date_of_birth = self.validate_birthdate(birthdate)
        self.patients_social_security_id = self.validate_social_security_id(social_security_id)
        self.patients_tel_number = self.validate_tel_number(tel_number)
        self.patients_email = self.validate_email(email)
        self.patients_address = self.validate_address(address)
        self.patients_occupation = occupation
        self.patients_emergency_contact = self.validate_emergency_contact(emergency_contact)

    def validate_address(self, address: Dict[str, str]) -> Dict[str, str]:
        """
        Validate the address dictionary.

        Args:
            address (dict): Address with keys: 'street', 'city', 'state', 'postal_code', 'country'.

        Returns:
            dict: Validated address.

        Raises:
            ValueError: If required keys are missing or data is invalid.
        """
        required_keys = {'street', 'city', 'state', 'postal_code', 'country'}
        if not isinstance(address, dict):
            raise ValueError("Address must be a dictionary.")
        if not required_keys.issubset(address.keys()):
            raise ValueError(f"Address must include the keys: {', '.join(required_keys)}.")
        if not all(isinstance(address[key], str) and address[key] for key in required_keys):
            raise ValueError("All address fields must be non-empty strings.")
        return address

    # Rest of the class remains the same...

    def __str__(self) -> str:
        """
        String representation of the personal data.

        Returns:
            str: A readable summary of the patient's personal data.
        """
        address_str = (
            f"{self.patients_address['street']}, {self.patients_address['city']}, "
            f"{self.patients_address['state']} {self.patients_address['postal_code']}, "
            f"{self.patients_address['country']}"
        )
        emergency_contact_str = (
            f"Emergency Contact: {self.patients_emergency_contact['name']} "
            f"({self.patients_emergency_contact['tel_number']})"
        )
        return (
            f"Name: {self.patients_name} {self.patients_surname}, Father's Name: {self.patients_fathers_name}, "
            f"Mother's Name: {self.patients_mothers_name}, Birthdate: {self.patients_date_of_birth}, "
            f"Social Security ID: {self.patients_social_security_id}, Telephone: {self.patients_tel_number}, "
            f"Email: {self.patients_email}, Address: {address_str}, Occupation: {self.patients_occupation}, "
            f"{emergency_contact_str}"
        )


class FamilyHistory:
    """
    Represents a family medical history record with a list of common and additional diseases.
    """
    def __init__(
        self, 
        heart_disease: bool = False, 
        stroke: bool = False, 
        diabetes: bool = False, 
        cancer: bool = False, 
        obesity: bool = False, 
        mental_health_issues: bool = False, 
        high_blood_pressure: bool = False,
        kidney_disease: bool = False, 
        other: list[str] = None
    ) -> None:
        """
        Initialize a family medical history record.

        Args:
            heart_disease (bool): Indicates if heart disease is present.
            stroke (bool): Indicates if stroke is present.
            diabetes (bool): Indicates if diabetes is present.
            cancer (bool): Indicates if cancer is present.
            obesity (bool): Indicates if obesity is present.
            mental_health_issues (bool): Indicates if mental health issues are present.
            high_blood_pressure (bool): Indicates if high blood pressure is present.
            kidney_disease (bool): Indicates if kidney disease is present.
            other (list[str], optional): List of other diseases. Defaults to an empty list.
        """
        self.heart = heart_disease
        self.stroke = stroke
        self.diabetes = diabetes
        self.cancer = cancer
        self.obesity = obesity
        self.mental_health = mental_health_issues
        self.blood = high_blood_pressure
        self.kidney = kidney_disease
        self.other = other if other is not None else []

    def add_disease_into_other_list(self, disease: str) -> None:
        """
        Add a disease to the 'other' list if it is not already present.

        Args:
            disease (str): The name of the disease to add.
        """
        if disease and isinstance(disease, str) and disease not in self.other:
            self.other.append(disease)

    def remove_disease_from_other_list(self, disease: str) -> bool:
        """
        Remove a disease from the 'other' list if present.

        Args:
            disease (str): The name of the disease to remove.

        Returns:
            bool: True if the disease was removed, False otherwise.
        """
        if disease in self.other:
            self.other.remove(disease)
            return True
        return False

    def has_any_disease(self) -> bool:
        """
        Check if any disease is present in the family history.

        Returns:
            bool: True if any disease is present, False otherwise.
        """
        return any([
            self.heart, self.stroke, self.diabetes, self.cancer, 
            self.obesity, self.mental_health, self.blood, self.kidney
        ]) or bool(self.other)

    def clear_all_diseases(self) -> None:
        """
        Clear all diseases from the record, resetting to a blank state.
        """
        self.heart = False
        self.stroke = False
        self.diabetes = False
        self.cancer = False
        self.obesity = False
        self.mental_health = False
        self.blood = False
        self.kidney = False
        self.other.clear()

    def __str__(self) -> str:
        """
        String representation of the family history.

        Returns:
            str: A readable summary of the family history.
        """
        return (
            f"Heart Disease: {self.heart}, Stroke: {self.stroke}, "
            f"Diabetes: {self.diabetes}, Cancer: {self.cancer}, Obesity: {self.obesity}, "
            f"Mental Health Issues: {self.mental_health}, High Blood Pressure: {self.blood}, "
            f"Kidney Disease: {self.kidney}, Other: {', '.join(self.other) or 'None'}"
        )



class LifestyleAndHabits:
    """
    A class to represent an individual's lifestyle and habits, including smoking,
    alcohol consumption, caffeine intake, exercise routines, dietary habits, and drug use.
    """

    def __init__(self,
                 smoking: bool,
                 smoking_frequency: int = 0,
                 smoking_quit_date: date = None,
                 alcohol_consumption: bool = False,
                 alcohol_frequency: int = 0,
                 alcohol_quit_date: date = None,
                 caffeine_consumption: bool = False,
                 caffeine_frequency: int = 0,
                 caffeine_quit_date: date = None,
                 exercise_habits: bool = False, 
                 exercise_frequency: int = 0, 
                 dietary_habits: list[str] = None,
                 drug_use: bool = False,
                 drug_frequency: int = 0,
                 drug_quit_date: date = None) -> None:
        """
        Initialize the lifestyle and habits instance.

        Args:
            smoking (bool): Indicates if the individual smokes.
            smoking_frequency (int): Frequency of smoking (times per week).
            smoking_quit_date (date): Date when the individual quit smoking.
            alcohol_consumption (bool): Indicates if the individual consumes alcohol.
            alcohol_frequency (int): Frequency of alcohol consumption (times per week).
            alcohol_quit_date (date): Date when the individual quit alcohol.
            caffeine_consumption (bool): Indicates if the individual consumes caffeine.
            caffeine_frequency (int): Frequency of caffeine consumption (times per week).
            caffeine_quit_date (date): Date when the individual quit caffeine.
            exercise_habits (bool): Indicates if the individual exercises regularly.
            exercise_frequency (int): Frequency of exercise (times per week).
            dietary_habits (list[str]): List of dietary habits (e.g., "vegetarian", "low-carb").
            drug_use (bool): Indicates if the individual uses recreational drugs.
            drug_frequency (int): Frequency of drug use (times per week).
            drug_quit_date (date): Date when the individual quit using drugs.
        """
        self.smoking = smoking
        self.smoking_frequency = self._validate_frequency(smoking_frequency)
        self.smoking_quit_date = smoking_quit_date if not smoking else None
        self.alcohol_consumption = alcohol_consumption
        self.alcohol_frequency = self._validate_frequency(alcohol_frequency)
        self.alcohol_quit_date = alcohol_quit_date if not alcohol_consumption else None
        self.caffeine_consumption = caffeine_consumption
        self.caffeine_frequency = self._validate_frequency(caffeine_frequency)
        self.caffeine_quit_date = caffeine_quit_date if not caffeine_consumption else None
        self.exercise_habits = exercise_habits
        self.exercise_frequency = self._validate_frequency(exercise_frequency)
        self.dietary_habits = dietary_habits if dietary_habits is not None else []
        self.drug_use = drug_use
        self.drug_frequency = self._validate_frequency(drug_frequency)
        self.drug_quit_date = drug_quit_date if not drug_use else None

    def _validate_frequency(self, frequency: int) -> int:
        """
        Validate frequency values to ensure they are non-negative integers.
        """
        if not isinstance(frequency, int) or frequency < 0:
            raise ValueError("Frequency must be a non-negative integer.")
        return frequency
    
    def quit_habit(self, habit: str, quit_date: date) -> None:
        """
        Mark a habit as quit and record the quit date.

        Args:
            habit (str): The name of the habit to quit. Accepted values: "smoking", "alcohol", "caffeine", "drug".
            quit_date (date): The date when the habit was quit.

        Raises:
            ValueError: If the habit name is invalid or quit date is in the future.
        """
        if quit_date > date.today():
            raise ValueError("Quit date cannot be in the future.")

        if habit == "smoking" and self.smoking:
            self.smoking = False
            self.smoking_quit_date = quit_date
        elif habit == "alcohol" and self.alcohol_consumption:
            self.alcohol_consumption = False
            self.alcohol_quit_date = quit_date
        elif habit == "caffeine" and self.caffeine_consumption:
            self.caffeine_consumption = False
            self.caffeine_quit_date = quit_date
        elif habit == "drug" and self.drug_use:
            self.drug_use = False
            self.drug_quit_date = quit_date
        else:
            raise ValueError(f"{habit.capitalize()} is not active or invalid habit name.")
        
    def days_since_quit(self, habit: str) -> int:
        """
        Calculate the number of days since the habit was quit.

        Args:
            habit (str): The name of the habit. Accepted values: "smoking", "alcohol", "caffeine", "drug".

        Returns:
            int: Number of days since quit. Returns -1 if the habit is still active or quit date is unknown.
        """
        quit_dates = {
            "smoking": self.smoking_quit_date,
            "alcohol": self.alcohol_quit_date,
            "caffeine": self.caffeine_quit_date,
            "drug": self.drug_quit_date
        }
        quit_date = quit_dates.get(habit)
        if quit_date:
            return (date.today() - quit_date).days
        return -1  # Habit still active or quit date unknown
    
    def add_diet_into_dietary_habits(self, diet: str) -> None:
        """
        Add a diet type into dietary habits.

        Args:
            diet (str): The diet habit to add (e.g., "vegetarian").
        """
        if diet not in self.dietary_habits:
            self.dietary_habits.append(diet)

    def update_habit(self, habit: str, value: bool, frequency: int = 0) -> None:
        """
        Update a specific habit (e.g., smoking, alcohol, drug use).

        Args:
            habit (str): The name of the habit to update. 
                         Accepted values: "smoking", "alcohol", "caffeine", "exercise", "drug".
            value (bool): The new value for the habit (True or False).
            frequency (int, optional): The frequency of the habit. Defaults to 0.
        """
        if habit == "smoking":
            self.smoking = value
            self.smoking_frequency = max(0, frequency)
        elif habit == "alcohol":
            self.alcohol_consumption = value
            self.alcohol_frequency = max(0, frequency)
        elif habit == "caffeine":
            self.caffeine_consumption = value
            self.caffeine_frequency = max(0, frequency)
        elif habit == "exercise":
            self.exercise_habits = value
            self.exercise_frequency = max(0, frequency)
        elif habit == "drug":
            self.drug_use = value
            self.drug_frequency = max(0, frequency)
        else:
            raise ValueError("Invalid habit name. Accepted values are 'smoking', 'alcohol', 'caffeine', 'exercise', 'drug'.")

    def remove_diet_from_dietary_habits(self, diet: str) -> None:
        """
        Remove a diet type from dietary habits.

        Args:
            diet (str): The diet habit to remove (e.g., "vegetarian").
        """
        if diet in self.dietary_habits:
            self.dietary_habits.remove(diet)

    def __str__(self) -> str:
        """
        String representation of the lifestyle and habits.

        Returns:
            str: A formatted string summarizing the individual's lifestyle and habits.
        """
        def quit_info(habit: str, active: bool, frequency: int, quit_date: date) -> str:
            if active:
                return f"{habit.capitalize()}: Yes (Frequency: {frequency} per week)"
            if quit_date:
                days = (date.today() - quit_date).days
                return f"{habit.capitalize()}: Quit {days} days ago"
            return f"{habit.capitalize()}: No (Never engaged or unknown quit date)"
        
        smoking_info = quit_info("Smoking", self.smoking, self.smoking_frequency, self.smoking_quit_date)
        alcohol_info = quit_info("Alcohol consumption", self.alcohol_consumption, self.alcohol_frequency, self.alcohol_quit_date)
        caffeine_info = quit_info("Caffeine consumption", self.caffeine_consumption, self.caffeine_frequency, self.caffeine_quit_date)
        drug_info = quit_info("Drug use", self.drug_use, self.drug_frequency, self.drug_quit_date)
        
        return (
            f"Smoking: {smoking_info}\n"
            f"Alcohol Consumption: {alcohol_info}\n"
            f"Caffeine Consumption: {caffeine_info}\n"
            f"Exercise: {'Yes' if self.exercise_habits else 'No'} (Frequency: {self.exercise_frequency} per week)\n"
            f"Dietary Habits: {', '.join(self.dietary_habits) if self.dietary_habits else 'None'}\n"
            f"Drug Use: {drug_info}"
        )




class Allergies:
    """Class to represent a person’s allergies and manage the list of allergies."""

    def __init__(self, allergies_presence: bool, allergies: list[str] = None) -> None:
        """
        Initializes the Allergies class with the presence of allergies and a list of specific allergies.
        
        Args:
            allergies_presence (bool): Whether the person has allergies.
            allergies (list[str]): A list of allergens, if any.
        """
        self._allergies_presence = allergies_presence  # private attribute
        self._allergies = allergies if allergies else []  # private attribute

    @property
    def allergies_presence(self) -> bool:
        return self._allergies_presence

    @allergies_presence.setter
    def allergies_presence(self, presence: bool) -> None:
        self._allergies_presence = presence

    @property
    def allergies(self) -> list[str]:
        return self._allergies

    def add_allergy(self, allergy: str) -> None:
        """Adds a new allergy to the list of allergies if it's not already present.
        
        Args:
            allergy (str): The name of the allergy to add.
        """
        if allergy not in self._allergies:
            self._allergies.append(allergy)

    def remove_allergy(self, allergy_to_remove: str) -> bool:
        """Removes an allergy from the list of allergies.
        
        Args:
            allergy_to_remove (str): The allergy to remove.
        
        Returns:
            bool: True if the allergy was removed, False if the allergy was not found.
        """
        if allergy_to_remove in self._allergies:
            self._allergies.remove(allergy_to_remove)
            return True
        return False

    def __str__(self) -> str:
        """Returns a string representation of the person's allergies."""
        if not self._allergies:
            return "No known allergies."
        return f"Known allergies: {', '.join(self._allergies)}"

    def has_allergies(self) -> bool:
        """Checks if the person has any allergies listed."""
        return bool(self._allergies)

    @staticmethod
    def is_valid_allergy(allergy: str) -> bool:
        """Checks if the provided allergy name is valid (non-empty string)."""
        return bool(allergy.strip())



class CurrentMedications:
    """
    A class to represent an individual's current medications.
    """

    def __init__(self, medications: list[str] = None) -> None:
        """
        Initialize the CurrentMedications instance.

        Args:
            medications (list[str]): A list of current medications.
        """
        self.medications = medications if medications is not None else []

    def add_medication(self, medication: str) -> None:
        """
        Add a medication to the list.

        Args:
            medication (str): The medication to add.

        Raises:
            ValueError: If the medication is empty or already in the list.
        """
        if not medication:
            raise ValueError("Medication cannot be empty.")
        if medication in self.medications:
            raise ValueError("Medication already exists in the list.")
        self.medications.append(medication)

    def remove_medication(self, medication: str) -> bool:
        """
        Remove a medication from the list.

        Args:
            medication (str): The medication to remove.

        Returns:
            bool: True if the medication was removed, False if not found.
        """
        if medication in self.medications:
            self.medications.remove(medication)
            return True
        return False

    def __str__(self) -> str:
        return f"Current Medications: {', '.join(self.medications) if self.medications else 'None'}"

class Surgeries:
    """
    A class to represent an individual's surgeries.
    """

    def __init__(self, surgeries: list[str] = None) -> None:
        """
        Initialize the Surgeries instance.

        Args:
            surgeries (list[str]): A list of surgeries.
        """
        self.surgeries = surgeries if surgeries is not None else []

    def add_surgery(self, surgery: str) -> None:
        """
        Add a surgery to the list.

        Args:
            surgery (str): The surgery to add.

        Raises:
            ValueError: If the surgery is empty or already in the list.
        """
        if not surgery:
            raise ValueError("Surgery cannot be empty.")
        if surgery in self.surgeries:
            raise ValueError("Surgery already exists in the list.")
        self.surgeries.append(surgery)

    def remove_surgery(self, surgery: str) -> bool:
        """
        Remove a surgery from the list.

        Args:
            surgery (str): The surgery to remove.

        Returns:
            bool: True if the surgery was removed, False if not found.
        """
        if surgery in self.surgeries:
            self.surgeries.remove(surgery)
            return True
        return False

    def __str__(self) -> str:
        return f"Surgeries: {', '.join(self.surgeries) if self.surgeries else 'None'}"
   



class Disabilities:
    """
    A class to represent an individual's disabilities.
    """

    def __init__(self, disabilities: list[str] = None) -> None:
        """
        Initialize the Disabilities instance.

        Args:
            disabilities (list[str]): A list of disabilities.
        """
        self.disabilities = disabilities if disabilities is not None else []

    def add_disability(self, disability: str) -> None:
        """
        Add a disability to the list.

        Args:
            disability (str): The disability to add.

        Raises:
            ValueError: If the disability is empty or already in the list.
        """
        if not disability:
            raise ValueError("Disability cannot be empty.")
        if disability in self.disabilities:
            raise ValueError("Disability already exists in the list.")
        self.disabilities.append(disability)

    def remove_disability(self, disability: str) -> bool:
        """
        Remove a disability from the list.

        Args:
            disability (str): The disability to remove.

        Returns:
            bool: True if the disability was removed, False if not found.
        """
        if disability in self.disabilities:
            self.disabilities.remove(disability)
            return True
        return False

    def __str__(self) -> str:
        return f"Disabilities: {', '.join(self.disabilities) if self.disabilities else 'None'}"



class Hospitalizations:
    """
    A class to represent an individual's hospitalizations.
    """

    def __init__(self, hospitalizations: list[str] = None) -> None:
        """
        Initialize the Hospitalizations instance.

        Args:
            hospitalizations (list[str]): A list of hospitalizations.
        """
        self.hospitalizations = hospitalizations if hospitalizations is not None else []

    def add_hospitalization(self, hospitalization: str) -> None:
        """
        Add a hospitalization to the list.

        Args:
            hospitalization (str): The hospitalization to add.

        Raises:
            ValueError: If the hospitalization is empty or already in the list.
        """
        if not hospitalization:
            raise ValueError("Hospitalization cannot be empty.")
        if hospitalization in self.hospitalizations:
            raise ValueError("Hospitalization already exists in the list.")
        self.hospitalizations.append(hospitalization)

    def remove_hospitalization(self, hospitalization: str) -> bool:
        """
        Remove a hospitalization from the list.

        Args:
            hospitalization (str): The hospitalization to remove.

        Returns:
            bool: True if the hospitalization was removed, False if not found.
        """
        if hospitalization in self.hospitalizations:
            self.hospitalizations.remove(hospitalization)
            return True
        return False

    def __str__(self) -> str:
        return f"Hospitalizations: {', '.join(self.hospitalizations) if self.hospitalizations else 'None'}"



class VaccinationRecord:
    """
    A class to represent a patient's vaccination record, storing details about vaccinations.
    """

    def __init__(self, vaccinations: dict[str, str] = None) -> None:
        """
        Initialize the vaccination record.

        Args:
            vaccinations (dict[str, str]): A dictionary where the key is the vaccine name and the value is the date administered.
        """
        self.vaccinations = vaccinations if vaccinations is not None else {}

    def add_vaccination(self, vaccine_name: str, date_administered: str) -> None:
        """
        Add a vaccine to the record.

        Args:
            vaccine_name (str): The name of the vaccine (e.g., "COVID-19", "Influenza").
            date_administered (str): The date the vaccine was administered (e.g., "2023-01-15").
        """
        self.vaccinations[vaccine_name] = date_administered

    def remove_vaccination(self, vaccine_name: str) -> None:
        """
        Remove a vaccine from the record.

        Args:
            vaccine_name (str): The name of the vaccine to remove.
        """
        if vaccine_name in self.vaccinations:
            del self.vaccinations[vaccine_name]
        else:
            raise ValueError(f"No record found for vaccine: {vaccine_name}")

    def __str__(self) -> str:
        """
        String representation of the vaccination record.

        Returns:
            str: A formatted string summarizing the vaccination record.
        """
        if not self.vaccinations:
            return "Vaccination Record: None"
        record = "\n".join([f"{vaccine}: {date}" for vaccine, date in self.vaccinations.items()])
        return f"Vaccination Record:\n{record}"




class WomansHealthRecord:


    def __init__(self, 
                 is_pregnant: bool = False, 
                 past_pregnancies: int = 0, 
                 miscarriages: int = 0, 
                 abortions: int = 0, 
                 other_issues: list[str] = None) -> None:

        self.is_pregnant = is_pregnant
        self.past_pregnancies = max(0, past_pregnancies)
        self.miscarriages = max(0, miscarriages)
        self.abortions = max(0, abortions)
        self.other_issues = other_issues if other_issues is not None else []
        self._validate_counts()

    def _validate_counts(self) -> None:

        if self.miscarriages + self.abortions > self.past_pregnancies:
            raise ValueError(
                "The sum of miscarriages and abortions cannot exceed the total number of past pregnancies."
            )

    def complete_pregnancy(self, successful: bool = True) -> None:

        if not self.is_pregnant:
            raise ValueError("Cannot complete a pregnancy because the woman is not currently pregnant.")

        self.is_pregnant = False
        if successful:
            self.past_pregnancies += 1
        else:
            self.miscarriages += 1
        self._validate_counts()

    def add_other_issue(self, issue: str) -> None:
 
        if issue not in self.other_issues:
            self.other_issues.append(issue)

    def remove_other_issue(self, issue: str) -> None:

        if issue in self.other_issues:
            self.other_issues.remove(issue)
        else:
            raise ValueError(f"Issue '{issue}' not found in the list of other issues.")

    def __str__(self) -> str:

        return (
            f"Currently Pregnant: {'Yes' if self.is_pregnant else 'No'}\n"
            f"Past Pregnancies: {self.past_pregnancies}\n"
            f"Miscarriages: {self.miscarriages}\n"
            f"Abortions: {self.abortions}\n"
            f"Other Health Issues: {', '.join(self.other_issues) if self.other_issues else 'None'}"
        )




class MenstrualCycleRecord:


    def __init__(self, 
                 last_period_date: str = None, 
                 cycle_length: int = 28, 
                 flow_pattern: dict[str, int] = None, 
                 symptoms: list[str] = None, 
                 health_issues: list[str] = None, 
                 period_history: list[str] = None) -> None:

        self.last_period_date = last_period_date
        self.cycle_length = max(21, min(35, cycle_length)) 
        self.flow_pattern = flow_pattern if flow_pattern is not None else {"Normal": 5}  
        self.symptoms = symptoms if symptoms is not None else []
        self.health_issues = health_issues if health_issues is not None else []
        self.period_history = period_history if period_history is not None else []
        if self.last_period_date:
            self.period_history.append(self.last_period_date)

    def add_symptom(self, symptom: str) -> None:

        if symptom not in self.symptoms:
            self.symptoms.append(symptom)

    def remove_symptom(self, symptom: str) -> None:

        if symptom in self.symptoms:
            self.symptoms.remove(symptom)
        else:
            raise ValueError(f"Symptom '{symptom}' not found in the list.")

    def add_health_issue(self, issue: str) -> None:

        if issue not in self.health_issues:
            self.health_issues.append(issue)

    def remove_health_issue(self, issue: str) -> None:

        if issue in self.health_issues:
            self.health_issues.remove(issue)
        else:
            raise ValueError(f"Health issue '{issue}' not found in the list.")

    def predict_next_period(self) -> str:

        if not self.last_period_date:
            raise ValueError("Last period date is not set. Cannot predict the next period.")
        from datetime import datetime, timedelta
        last_period = datetime.strptime(self.last_period_date, "%Y-%m-%d")
        next_period = last_period + timedelta(days=self.cycle_length)
        return next_period.strftime("%Y-%m-%d")

    def add_period_date(self, date: str) -> None:

        from datetime import datetime
        datetime.strptime(date, "%Y-%m-%d")  
        self.last_period_date = date
        self.period_history.append(date)

    def calculate_average_cycle_length(self) -> int:

        if len(self.period_history) < 2:
            raise ValueError("Not enough period history to calculate average cycle length.")
        from datetime import datetime
        differences = [
            (datetime.strptime(self.period_history[i], "%Y-%m-%d") - 
             datetime.strptime(self.period_history[i - 1], "%Y-%m-%d")).days
            for i in range(1, len(self.period_history))
        ]
        return sum(differences) // len(differences)

    def __str__(self) -> str:

        flow_summary = ", ".join([f"{key}: {value} days" for key, value in self.flow_pattern.items()])
        return (
            f"Last Period Date: {self.last_period_date or 'Not recorded'}\n"
            f"Cycle Length: {self.cycle_length} days\n"
            f"Flow Pattern: {flow_summary}\n"
            f"Symptoms: {', '.join(self.symptoms) if self.symptoms else 'None'}\n"
            f"Health Issues: {', '.join(self.health_issues) if self.health_issues else 'None'}\n"
            f"Period History: {', '.join(self.period_history) if self.period_history else 'None'}"
        )



class MedicalHistory:
    """
    Comprehensive Medical History class including personal data, medical history, 
    family history, lifestyle, allergies, medications, surgeries, disabilities, 
    hospitalizations, vaccination record, woman's health records, and menstrual cycle records.
    
    """

    def __init__(
        self,
        personal_data: PersonalData,
        family_history: FamilyHistory,
        lifestyle_and_habits: LifestyleAndHabits,
        allergies: Allergies,
        current_medications: CurrentMedications,
        surgeries: Surgeries,
        disabilities: Disabilities,
        hospitalizations: Hospitalizations,
        vaccination_record: VaccinationRecord,
        womans_health_record: Optional[WomansHealthRecord] = None,
        menstrual_cycle_record: Optional[MenstrualCycleRecord] = None
    ) -> None:
        """
        Initialize a comprehensive Medical History object.
        """
        self.personal_data = personal_data
        self.family_history = family_history
        self.lifestyle_and_habits = lifestyle_and_habits
        self.allergies = allergies
        self.current_medications = current_medications
        self.surgeries = surgeries
        self.disabilities = disabilities
        self.hospitalizations = hospitalizations
        self.vaccination_record = vaccination_record
        self.womans_health_record = womans_health_record
        self.menstrual_cycle_record = menstrual_cycle_record

    def __str__(self) -> str:
        """
        String representation of the Medical History.
        """
        womans_health_str = (
            f"Woman's Health Record:\n{self.womans_health_record}\n\n"
            if self.womans_health_record
            else "Woman's Health Record: Not Applicable\n\n"
        )
        menstrual_cycle_str = (
            f"Menstrual Cycle Record:\n{self.menstrual_cycle_record}\n\n"
            if self.menstrual_cycle_record
            else "Menstrual Cycle Record: Not Applicable\n\n"
        )
        return (
            f"Personal Data:\n{self.personal_data}\n\n"
            f"Family History:\n{self.family_history}\n\n"
            f"Lifestyle and Habits:\n{self.lifestyle_and_habits}\n\n"
            f"Allergies:\n{self.allergies}\n\n"
            f"Current Medications:\n{self.current_medications}\n\n"
            f"Surgeries:\n{self.surgeries}\n\n"
            f"Disabilities:\n{self.disabilities}\n\n"
            f"Hospitalizations:\n{self.hospitalizations}\n\n"
            f"Vaccination Record:\n{self.vaccination_record}\n\n"
            f"{womans_health_str}"
            f"{menstrual_cycle_str}"
        )


class Patient:
    def __init__(self, patient_id: str, name: str, password: str, medical_history: MedicalHistory) -> None:
        self.patient_id = patient_id
        self.name = name
        self.password = password
        self._medical_history = medical_history

    def check_password(self, password: str) -> bool:
        return self.password == password

    def get_medical_history(self, password: str) -> str:
        if self.check_password(password):
            return str(self._medical_history)
        else:
            raise ValueError("Incorrect password.")

class AuthenticationSystem:
    def __init__(self) -> None:
        self.patients = {}

    def register_patient(self, patient: Patient) -> None:
        self.patients[patient.patient_id] = patient

    def login(self, patient_id: str, password: str) -> str:
        if patient_id in self.patients:
            patient = self.patients[patient_id]
            return patient.get_medical_history(password)
        else:
            raise ValueError("Patient not found.")

