#!/usr/bin/env python
# coding: utf-8

# In[3]:


#SCA ASSIGMMENT

#WEEK TWO

#Assignment: Create an example of a class and function and push to github

#Solution
#An example program (of class and function) that updates of student's information 

from collections import namedtuple

Student = namedtuple("Student", ["id", "firstname", "lastname", "age", "department", "email"])

#class
def update_student_info(student, email):
    return student._replace(email = student.email)

#function
if __name__ == "__main__":
    student1 = Student(202001, "Adebowale", "Alex", 23, "Medicine", "email")
    student1 = update_student_info(Student1, "adebowale.lexa@gmail.com")
    
    print ("================================")
    print("Succefully Updated!")
    print ("================================")
    
          
    print("First name:", student1.firstname)
    print("Last name:", student1.lastname)
    print("Age:", student1.age)
    print("Department:", student1.department)                            
    print("Email:", student1.email)


# In[ ]:




