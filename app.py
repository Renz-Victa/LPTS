# 1. Learner Management

learner_id =
name = 
age = 
course = 
marks = 

add_new_learners
view_learner_details
update_learner_details
remove_learners

# 2. Inheritance

class name:
  def 

class age:
  def

class Learner(Person):
  def 

# 3. Assessment and Marks

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

# 4. Assessment and Marks

qwertyuiop

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


for i in range (1, 6):
  if i == 3:
    continue
  print(i)
  
mark = 1

while mark <= 0:
  print(mark)
  mark += 1

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

def sum():
  print("Calculates the sum of all marks in a learner's marks list")

def number_of_learners():


# 9. Exception Handling

try: 
  test1 = int(input("Enter the mark for test1: "))
  test2 = int(input("Enter the mark for test2: "))
  result = (test1 + test2) // 2
except ValueError:
  print("Please enter a valid number!")
else: 
  print("The Result is:", result) 
finally: 
  print("Tests are finished!")


# 10. Lists

tests = ["test1", "test2", "test3"]
for tests in tests:
  return tests



# 11. GUI Requirement



# 12. Output

