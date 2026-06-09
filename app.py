# ==============================
# Learner Progress Tracking System
# EDUV12466121@vossie.net
# Date: 02/05/2026
# ==============================

from tkinter import Tk as tk, messagebox

# ==============================
# 1. Learner Management
# ==============================

learners_db = []

def add_new_learners(learner_id, learner, name, age, course=""):
  learner = Learner(learner_id, learner, name, age, course)
  learners_db.append(learner, learner_id, name, age, course)

  learner_id = entering_learner_mark("Enter learner ID: ") 
  print("Adding a new learner...")

  if learners_db(learner, learner_id):
    messagebox.showerror("Duplicate ID", "A learner with this ID already exists.")
    return
  
  name = input("Enter learner name: ").strip()
  age = entering_learner_mark("Enter learner age: ")

  if not check_eligibility(age):
    messagebox.showerror("Invalid Input", "Learner age is not valid.")
    return 
  
  course = input("Enter a course name: ").strip()
  messagebox.showinfo("Success", "Learner added successfully")

def view_learner_details(learner_id):
  learner = search_learner_by_id(learner_id)
  if learner:
    print(learner.display_info())
  else:
    print(f"No learner found with ID: {learner_id}")

def update_learner_details(learner_id):
  learner = search_learner_by_id(learner, learner_id)
  learner_id = entering_learner_mark("Enter learner ID: ")

  name = input("Enter new name: ").strip()
  age = entering_learner_mark("Enter new age: ")
  course = input("Enter new course: ").strip()
  
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

    learner.update_details(name, age, course)
    messagebox.showinfor("Updated", "Updated Successfully!")

def remove_learners(learners, learner_id):
  global learners_db
  learner = search_learner_by_id(learners, learner_id)
  learner_id = entering_learner_mark("Enter learner: ")

  if learner:
    learners_db.remove(learner)
    print(f"Learner {learner_id} remove successfully.")
  else:
    print(f"No learner found with ID: {learner_id}")

  learners.remove(learners)
  messagebox.showinfo("Deleted", "Learner removed successfully!")

# ==============================
# 2. Inheritance
# ==============================

class learner:
  def __init__(self, name, age, course=""):
    self.learner_id = learner
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
    self.__average_mark 
    self.__learner_status 

  def learner_status(self):
    if self.average_mark() >= 50:
      return "Passing"
    return "Failing"

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
  
  def add_mark(self, mark):
    self.__balance += mark
    self.marks.append(mark)
    self.__average_mark >= certificate

# ==============================
# Decision Structures
# ==============================

def check_eligibility(learner_age):
  if learner_age >= 18:
    print("Eligible to study at Eduvos")
  else: 
    print("Not Eligible to study at Eduvos")

def grade_mark(average):
  if average >= 75:
    print("Pass with Distinction")
  elif average >= 50:
    print("Pass")
  else:
    print("Fail")

def certificate(mark):
  if mark >= 50:
    print("Learner qualifies for a certificate")

def show_learner_result(learners):
  learner_id = entering_learner_mark("Enter learner ID: ")
  learner = search_learner_by_id(learners, learner_id)

  if learner is None:
    messagebox.showinfo("Unknown", "Learner not found!")
    return
  
  print(f"\nResult for {learner.name}")
  print(f"Average: {learner.average_mark:.2f}")
  print(f"Performance: {learner.details}")

  if learner.certificate():
    messagebox.showinfo("Result", f"{learner.name} qualifies for a certificate.")
  else: 
    messagebox.showinfo("Result", f"{learner.name} does not qualify for a certificate.")

# ==============================
# 6. Repetition Structures
# ==============================

def recursive_total():
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

def enter_marks(learner):
  learner_id = entering_learner_mark("Enter learner ID: ")
  learner = learners_db(learner, learner_id)
  print("Capturing Marks...")

  if learner is None:
    messagebox.showerror("Not found", "Learner not found")
    return
  
  mark = entering_learner_mark("How many marks do you want to enter?")

  for count in range(mark):
    mark = read_mark(f"Enter mark {count + 1}: ")
    learner.add_mark(mark)

messagebox.showinfo("System Message", "Successful!")

def calculate_average(marks):
  if not marks:
    return 0.0
  return recursive_total(marks)/len(marks)

average = calculate_average(50, 60)
print("Total Average:", average)

def display_learner_summary(learner):
  print("Displaying learner summaries...")
  print("\nLearner Summary")
  print(f"Learner ID: {learner.learner_id}")
  print(f"Name: {learner.name}")
  print(f"Age: {learner.age}")
  print(f"Marks: {learner.mark}")
  print(f"Average: {learner.average_mark:.2f}")
  print(f"Results: {learner.status}")

def search_learner_by_id(learners, learner_id):
  print("\nSearching learner...")
  learner_id = entering_learner_mark("Enter learner ID: ")
  learner = search_learner_by_id(learners, learner_id)
  for learner in learners:
    if learner.learner_id == learner_id:
      display_learner_summary(learner)
      return learner
  return None

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

def read_mark(prompt="Enter the mark: ", minimum=0, maximum=100):
  try: 
    mark = float(input(prompt))
    if mark < minimum or mark > maximum:
      raise ValueError("Invalid mark: must be between 0 and 100")
    return mark

  except ValueError as e: 
    print(e)

def entering_learner_mark(prompt):
  try: 
    value = int(input(prompt))
    if value <= 0:
      raise ValueError("Value must be greater than zero")
    return value

  except ValueError as e:
    print("Please enter a valid number! ({e})")
  except ZeroDivisionError:
    print("Cannot be divided by zero")
  else: 
    print("The Result is:", result) 
  finally: 
    print("Tests are finished!")


def show_menu():
  print("\n Learner Progress Tracking System (LPTS) ")
  print("1. Add Learner")
  print("2. View all Learners")
  print("3. Enter marks")
  print("4. Search learner")
  print("5. Update learner")
  print("6. Remove learner")
  print("7. Show learner results")
  print("8. Exit")
  
choice = input("Select an option: ")
  
if choice == "1":
    print("Adding student...")
elif choice == "2":
    print("Viewing students...")
elif choice == "3":
    print("Exiting...")
else: 
    print("Menu selection error: Invalid option chosen")

def view_learners(learners):
  if not learners:
    messagebox.showinfo("No learners", "There are no learners showing")
    return
  
  for learner in learners:
    display_learner_summary(learner)

# ==============================
# 10. Lists
# ==============================

def demo_lists():
  for tests in tests:
    print(tests)

for student_record in learner:
  print(student_record["name"], student_record["mark"])
  
def is_passing(mark):
  return mark >= 50

passing_students = list(filter(lambda learner: is_passing(learner["mark"]), learner))
print("Passing students:", passing_students)

if 80 in learner:
  print("Found")
else: print("Not Found")

for score in learner.items():
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

def main():
  learners = []

  while True:
    show_menu()

    try: 
      choice = int(input("Enter your choice: "))
    except ValueError: 
      messagebox.showerror("Error", "Please enter a valid number!")
    continue
  
    if choice == 1:
      add_new_learners(learners)
    elif chocie == 2:
      enter_marks(learners)
    elif choice == 3:
      view_learners(learners)
    elif choice == 4:
      search_learner_by_id(learners)
    elif choice == 5:
      update_learner_details(learners)
    elif choice == 6:
      remove_learners(learners)
    elif choice == 7:
      show_learner_result(learners)
    elif choice == 8:
      if messagebox.askyesno("Exit", "Are you sure want to exit?"):
        print("Thank You For Coming!")
        break
    else:
      messagebox.showerror("Error", "Please choocse an option from 1 to 8.")
     
if __name__ == "__main__":
  main()