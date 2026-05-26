# ==============================
# Learner Progress Tracking System
# ==============================

# ==============================
# 1. Learner Management
# ==============================

class learner_id:
  pass
class name:
  pass 
class age: 
  pass
class course: 
  pass
class marks:
  pass 

learners_db = []

def add_new_learners(learner_id, name, age):
  print(f"Learner '{name} added successfully.")
def view_learner_details(learner_id):
  learner = search_learner_by_id(learner_id)
  if learner:
    print(learner)
  else:
    print(f"No learner found with ID: {learner_id}")
def update_learner_details(learner_id):
  learner = search_learner_by_id(learner_id)
  if learner:
    if name:
      learner.set_name(name)
    if age:
      learner.set.age(age)
    print(f"Learner {learner_id} updated successfully.")
  else:
    print(f"No learner found with ID: {learner_id}")
def remove_learners(learner_id):
  global learners_db


# 2. Inheritance

class learner:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    def greet(self):
      print(f"Hello!, {self.name}!")

class Learner(Person):
  def __init__(self, name, age, learner_id):
    super().__init__(name, age)
    self.learner_id = learner_id

  def display_info(self):
    print(f"Student ID: {self.learner_id} | Name: {self.name} | Age: {self.age}")

# 3. Encapsulation

class Person:
    def __init__(self, name):
      self.name = name

# 4. Assessment and Marks

class AverageMark:
  def __init__(average_mark, balance):
    average_mark.__learner = balance
  
  def display(average_mark, amount):
    average_mark.__learner += amount

  def get_balance(average_mark):
    return average_mark.__learner
  
mark = AverageMark(50)

mark.display(500)

print(mark.get_balance())

# Decision Structures

learner_age = 18

if learner_age >= 18:
  print("Eligible to study at Eduvos")
else: 
  print("Not Eligible to study at Eduvos")

mark = 50

if mark >= 75:
  print("Distinction")
elif score >= 60:
  print("Grade B")
elif score >= 50:
  print("Grade C")
else:
  print("Fail")

mark = 50

if mark >= 50:
  print("Learner qualifies for a certificate")

# 6. Repetition Structures

for i in range(1, 9):
  if i == 10:
    break
  print(i)


for i in range(1, 6):
  if i == 3:
    continue
  print(i)
  
mark = 1

while mark <= 0:
  print(mark)
  mark += 1

for subject in learner:
  print(subject, learner(subject))

# 7. Functions

def add_learner(name):
  print("Adding a learner", name)

def enter_marks():
  print("Entering marks")

def calculate_average(test1, test2):
  total = (test1 + test2) // 2
  return total

average = calculate_average(50, 60)
print("Total Average:", average)

def display_learner_summary():
  print("Displaying learner summaries")

def search_learner_by_id():
  print("Searching a learner by ID")

def predictive():
  if mark >= 50
  bool = True
else:
bool = False

# 8. Recursion

def recursive_sum(marks):
  if len(marks) == 0
  return 0
  count = len(people)
  print("Number of people in the system:")


# 9. Exception Handling

try: 
  test1 = int(input("Enter the mark for test1: "))
  test2 = int(input("Enter the mark for test2: "))
  result = (test1 + test2) // 2
  if mark < 0 or mark > 100:
    print("Invalid mark: must be between 0 and 100")
except ValueError:
  print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot be divided by zero")
else: 
  print("The Result is:", result) 
finally: 
  print("Tests are finished!")

print("1. Add Student")
print("2. View Students")
print("3. Exit")
  
choice = input("Select an option: ")
  
if choice == "1":
    print("Adding student...")
elif choice == "2":
    print("Viewing students...")
elif choice == "3":
    print("Exiting...")
else: 
    print("Menu selection error: Invalid option chosen")

# 10. Lists

tests = ["test1", "test2", "test3"]
for tests in tests:
  return tests

learner = {
  "name": "John",
  "Mathematics": "80",
  "Programming": "85",
  "English": "90"
}

learners = [
  {"name": "John", "mark": 80},
  {"name": "Sarah", "mark": 65},
  {"name": "Mike", "mark": 50},
]

for learner in learners:
  print(learner["name"], learner["mark"])

learners = ["John", "Sarah", "Mike"]
  
  pass = list(filter(is_pass, learners))
print(pass)

if 80 in learner:
  print("Found")
else: print("Not Found")

for l in learner:
  if l > 50:
    print(l)

# 11. GUI Requirement



# 12. Output

