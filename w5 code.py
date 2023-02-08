#flashcard example
import random

class Qbank:
    
    def __init__(self):
        #only attribute
        self.qbankdict = {'anatomy' : {}, 'cardiology': {}, 'respiratory':{}}
        self.subset = ['anatomy', 'cardiology', 'respiratory']



    #create function to make the subset
    def addtopic(self, topicadded):
        self.qbankdict.update({topicadded: {}})
        self.subset.append(topicadded)
        
    #behaviour
    def addQ(self, subset, question, answer):
        self.qbankdict[subset][question] = answer
    
    def askQ(self):
        print('Enter the number corresponding to the topic you would like to be questioned on')
       #enumerate allows you to iterate over two items in for loop
        for i, x in enumerate(self.qbankdict):
            print(f"{i+1}. {x}")
            
    
        # print("Which topic do you wish to be questioned on?")
        # print(f"1. anatomy ")
        # print(f"2. cardiology")
        # print(f"3. respiratory")
        # print(f"3. x")
        
        topic_key = self.subset[int(input("Enter the number of your choice: ")) - 1]
        #print(topic_key)
        topic = self.qbankdict[topic_key]
        
        #choose a random index of the subset dictionary
        #print(self.qbankdict[subset])
        question_key = random.choice(list(topic.keys()))
        #print(f"Topic is {topic_key} ")
        #ask the key of the subset
        answer = input(f"{question_key} Enter answer:\n")
        #if val = key value then correct print: 'nice'
        if answer.lower() == topic[question_key].lower():
            print("correct")
        else:
            print(f'not quite. It is {topic[question_key]}')
       
    
#make object
qb = Qbank() 
 
qb.addQ('anatomy', 'what is the innervation of soleus muscle?','tibial nerve')
qb.addQ('anatomy', 'what is action of triceps muscle?','arm extension')

qb.addQ('respiratory', 'If symptoms persist after saba + ics, what is given?','laba')

qb.addQ('cardiology', 'which two drugs first line for HFrEF ?',' bb and acei')

qb.addtopic('rheumatology')
qb.addQ('rheumatology', 'what is the most sensitive test for SLE', 'ana test')

qb.askQ()

#print(qb.qbankdict)
#print(qb.num2subset[2])



#inheritance

import random

class HealthcareProfessional:
    def __init__(self, first_name, last_name, speciality, age, years_of_experience, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality
        self.age = age
        self.years_of_experience = years_of_experience
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary

    def get_email(self):
        return f'{self.first_name}.{self.last_name}@nhs.net'

class Surgeon(HealthcareProfessional):
    def __init__(self, first_name, last_name, age, years_of_experience, salary):
        super().__init__(first_name, last_name, 'surgery', age, years_of_experience, salary)

class Medic(HealthcareProfessional):
    def __init__(self, first_name, last_name, age, years_of_experience, salary):
        super().__init__(first_name, last_name, 'medicine', age, years_of_experience, salary)
        
    def salary_next_year(self):
        new_salary = self.salary * 1.05
        print(new_salary)

class Nurse(HealthcareProfessional):
    def __init__(self, first_name, last_name, age, years_of_experience, salary):
        super().__init__(first_name, last_name, 'nursing', age, years_of_experience, salary)

    def years_until_leaving(self):
        return random.randint(1, 4)

class AHP(HealthcareProfessional):
    def __init__(self, first_name, last_name, age, years_of_experience, salary):
        super().__init__(first_name, last_name, 'AHP', age, years_of_experience, salary)

class Student(HealthcareProfessional):
    def __init__(self, first_name, last_name, age, uni_name):
        super().__init__(first_name, last_name, 'student', age, 0, 0)
        self.uni_name = uni_name
        self.uni_initials = ''.join([name[0].lower() for name in uni_name.split()])

    def get_email(self):
        return f'{self.first_name[0].lower()}{self.last_name[0].lower()}20@{self.uni_initials}.ac.uk'

# Create two surgeons
surgeon1 = Surgeon('John', 'Doe', 45, 10, 80000)
surgeon2 = Surgeon('Jane', 'Smith', 35, 5, 75000)

# Create two medics
medic1 = Medic('Mike', 'Jones', 40, 7, 70000)
medic2 = Medic('Samantha', 'Williams', 30, 3, 65000)

# Create two nurses
nurse1 = Nurse('Sarah', 'Johnson', 35, 8, 60000)
nurse2 = Nurse('Tom', 'Brown', 45, 12, 55000)

# Create two AHPs
ahp1 = AHP('Bob', 'Smith', 32, 8, 60000)
ahp2 = AHP('Caroline', 'Johnson', 28, 5, 55000)

# Create three students
student1 = Student('Alice', 'Williams', 22, 'University of Cambridge')
student2 = Student('David', 'Jones', 20, 'University of Oxford')
student3 = Student('Zebra', 'Jacki', 21, 'Imperial College London')


# Print the email of the first surgeon
print(surgeon1.get_email())

# Print the email of the first student
print(student3.get_email())

#print medic salary next year
medic2.salary_next_year()

# Print the number of years until the second nurse leaves
print(nurse2.years_until_leaving())

# Check if Student is a subclass of HealthcareProfessional
print(issubclass(Student, HealthcareProfessional))  # Output: True

# Check if AHP is a subclass of Surgeon
print(issubclass(AHP, Surgeon))  # Output: False
