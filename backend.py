import json

# Initialize or load data from a JSON file (acting as our database)
data_file = "mental_health_system.json"

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"users": [], "patients": [], "doctors": []}

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Base User class
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def create_account(self):
        return {"name": self.name, "id": self.user_id}

    def check_profile(self):
        return {"name": self.name, "id": self.user_id}

# Patient class
class Patient(User):
    def __init__(self, name, user_id, age, goal):
        super().__init__(name, user_id)
        self.age = age
        self.goal = goal

    def register_problem(self, problem):
        return f"Problem '{problem}' registered for patient {self.name}."

    def follow_up(self):
        return f"Follow-up scheduled for patient {self.name}."

    def consult_doctor(self, doctor):
        return f"Consultation booked with Dr. {doctor.name}."

    def book_therapy_session(self):
        return f"Therapy session booked for patient {self.name}."

    def view_similar_cases(self):
        return f"Similar cases viewed for patient {self.name}."

# Doctor class
class Doctor(User):
    def __init__(self, name, user_id, age_range):
        super().__init__(name, user_id)
        self.age_range = age_range

    def respond_to_patient(self, patient):
        return f"Responded to patient {patient.name}."

    def prescribe_meds(self, patient):
        return f"Medication prescribed to patient {patient.name}."

    def set_sessions(self, patient):
        return f"Sessions set for patient {patient.name}."

    def review_patient_history(self, patient):
        return f"Patient history reviewed for {patient.name}."

    def update_treatment_plan(self, patient):
        return f"Treatment plan updated for {patient.name}."

    def send_notifications(self, patient):
        return f"Notification sent to patient {patient.name}."

# Main program for interaction
def main():
    data = load_data()

    while True:
        print("\n--- Mental Health System ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. View All Users")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            user_id = input("Enter patient ID: ")
            age = input("Enter patient age: ")
            goal = input("Enter patient goal: ")
            patient = Patient(name, user_id, age, goal)
            data["patients"].append(patient.create_account())
            save_data(data)
            print(f"Patient {name} added successfully.")

        elif choice == "2":
            name = input("Enter doctor name: ")
            user_id = input("Enter doctor ID: ")
            age_range = input("Enter age range doctor is responsible for: ")
            doctor = Doctor(name, user_id, age_range)
            data["doctors"].append(doctor.create_account())
            save_data(data)
            print(f"Doctor {name} added successfully.")

        elif choice == "3":
            print("\n--- All Users ---")
            print("Patients:", data["patients"])
            print("Doctors:", data["doctors"])

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
