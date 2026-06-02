# ==============================
# Learner Progress Tracking System
# ==============================

import tkinter as tk
from tkinter import messagebox
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

def add_new_learners(learner_id, name, age, course=""):
  learner = Learner(learner_id, name, age, course)
  learners_db.append(learner)
  print(f"Learner '{name} added successfully.")

def search_learner_by_id(learner_id):
  for learner in learners_db:
    if learner.learner_id == learner_id:
      return learner

def view_learner_details(learner_id):
  learner = search_learner_by_id(learner_id)
  if learner:
    print(learner.display_info())
  else:
    print(f"No learner found with ID: {learner_id}")

def update_learner_details(learner_id):
  learner = search_learner_by_id(learner_id)
  if learner:
    if name:
      learner.set_name(name)
    if age:
      learner.set.age(age)
    if subject:
      learner.set.subject(subject)
    print(f"Learner {learner_id} updated successfully.")
  else:
    print(f"No learner found with ID: {learner_id}")

def remove_learners(learner_id):
  global learners_db
  learner = search_learner_by_id(learner_id)

  if learner:
    learners_db.remove(learner)
    print(f"Learner {learner_id} remove successfully.")
  else:
    print(f"No learner found with ID: {learner_id}")

# ==============================
# 2. Inheritance
# ==============================

class learner:
  def __init__(self, name, age, course=""):
    self.learner_id = learner_id
    self.name = name
    self.age = age
    self.course = course
    self.marks = []

    if __name__ == "__main__":
      show_menu()

    def greet(self):
      print(f"Hello!, {self.name}!")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Learner(Person):
  def __init__(self, name, age, learner_id, course=""):
    super().__init__(name, age)
    self.learner_id = learner_id
    self.course = course
    self.marks = []

  def learner_status(self):
    if self.average_mark() >= 50:
      return "Passing"
    return "Failing"

  def display_info(self):
    print (
      f"ID: {self.learner_id}"
      f"Name: {self.name}"
      f"Age: {self.age}"
      f"Subject: {self.subject}"
      f"Average Mark: {self.average_mark():.2f}"
      f"Status: {self.learner_status()}"
    )

# ==============================
# 3. Encapsulation
# ==============================

class Person:
    def __init__(self, name):
      self.__name = name

    def average_mark(self):
      return self.__average_mark
    
    def learner_status(self):
      return self.__learner_status

# ==============================
# 4. Assessment and Marks
# ==============================

class AverageMark:
  def __init__(self):
    self.__balance = 0
  
  def display(self):
    print("Current balance:", self.__balance)

  def get_balance(self):
    return self.__balance
  
  def add_mark(self, amount):
    self.__balance += amount

# ==============================
# Decision Structures
# ==============================

def check_eligibility(learner_age):
  if learner_age >= 18:
    print("Eligible to study at Eduvos")
  else: 
    print("Not Eligible to study at Eduvos")

def grade_mark(mark):
  if mark >= 75:
    print("Pass with Distinction")
  elif mark >= 50:
    print("Pass")
  else:
    print("Fail")

def check_certificates(mark):
  if mark >= 50:
    print("Learner qualifies for a certificate")

# ==============================
# 6. Repetition Structures
# ==============================

def demo_loops():
  for i in range(1, 9):
    if i == 10:
      break
  print(i)

print("---")

for i in range(1, 6):
  if i == 3:
    continue
  print(i)

print("---")
  
mark = 1

while mark <= 0:
  print(mark)
  mark += 1

print("---")

learner = Learner()

for subject, mark in learner.items():
  print(subject, mark)

# ==============================
# 7. Functions
# ==============================

def add_learner(name):
  print("Adding a learner:", name)

def enter_marks():
  print("Entering marks")

def calculate_average(test1, test2):
  total = (test1 + test2) / 2
  return total

average = calculate_average(50, 60)
print("Total Average:", average)

def display_learner_summary():
  print("Displaying learner summaries")
  for l in learners_db:
    print(l)

def search_learner_by_id(learner_id):
  print("Searching a learner by ID")

def predictive(mark):
  return mark >= 50

# ==============================
# 8. Recursion
# ==============================

def recursive_sum(marks):
  if len(marks) == 0:
    return 0
  return marks[0]

def count_learners(learner_list):
  if len(learner_list) == 0:
    return 0
  count = 1 + count_learners(learner_list[1:])
  print(f"Number of learners counted so far: {count}")
  return count

# ==============================
# 9. Exception Handling
# ==============================

def get_average_mark():
  try: 
    test1 = int(input("Enter the mark for test1: "))
    test2 = int(input("Enter the mark for test2: "))

    if not (0 <= test1 <= 100) or not(0 <= test2 <= 100):
      raise ValueError("Invalid mark: must be between 0 and 100")
  
    result = (test1 + test2) / 2
    return result

  except ValueError as e: 
    print(e)

def entering_learner_mark():
  try: 
    test1 = int(input("Enter the mark for test1: "))
    test2 = int(input("Enter the mark for test2: "))

    result = (test1 + test2) / 2

  except ValueError as e:
    print("Please enter a valid number! ({e})")
  except ZeroDivisionError:
    print("Cannot be divided by zero")
  else: 
    print("The Result is:", result) 
  finally: 
    print("Tests are finished!")

def show_menu():
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

# ==============================
# 10. Lists
# ==============================

def demo_lists():
  tests = ["test1", "test2", "test3"]

  for tests in tests:
    print(tests)

student = {
  "name": "John",
  "Mathematics": "80",
  "Programming": "85",
  "English": "90"
}

students = [
  {"name": "John", "mark": 80},
  {"name": "Sarah", "mark": 65},
  {"name": "Mike", "mark": 50},
]

for student_record in students:
  print(student_record["name"], student_record["mark"])

students = ["John", "Sarah", "Mike"]
  
def is_passing(mark):
  return mark >= 50

passing_students = list(filter(lambda student: is_passing(student["mark"]), students))
print("Passing students:", passing_students)

if 80 in student:
  print("Found")
else: print("Not Found")

for score in student.items():
  if score > 50:
    print(subject, score)

# ==============================
# 11. GUI Requirement
# ==============================

root = tk.Tk()
root.withdraw()

def gui_feedback():
  response = messagebox.askyesno("Confirm", "Do you want to delete this learner?")
  print(response)

  response = messagebox.askokcancel("Save", "Do you want to save changes?")
  print(response)

def gui_messages():
  response = messagebox.askyesno("Confirm", "Do you want to undo changes?")
  print(response)

  response = messagebox.showerror("Confirm", "Invalid Input")
  print(response)

  response = messagebox.showinfo("Confirm", f"Learner has {mark}")
  print(response)

  response = messagebox.showwarning("Confirm", "Are you sure you want to exit")

entry = tk.Entry(root)
entry.pack()

root.mainloop()