#-----Define Funtions---------------
def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 87:
        return 'You have achieved top grade,  congratulations' 
    elif average >= 86:
        return 'B'
    elif average >= 75:
        return 'C'
    elif average >= 55:
        return 'D',             'You need to work harder next time'
    else:
        return 'F',             'You have failed, better luck next time'
        return 'E'
    

#-----End Funtions---------------



# importing csv module
import csv



# initializing the students list
students = []

# reading csv file
with open('Students.csv', 'r') as file:
        # creating a csv reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader) 
        
        # extracting field names through first row
        for row in reader:
            name, math, science, english = row
            #average = calculate_average([int(math), int(science), int(english)])
            m_grade = assign_grade(int(math))
            s_grade = assign_grade(int(science))
            e_grade = assign_grade(int(english))
            students.append([name, math, m_grade, science, s_grade, english, e_grade])

with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Math_Grade','Science','Science_Grade', 'English', 'English_Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')
    

