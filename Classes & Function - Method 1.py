#!/usr/bin/env python
# coding: utf-8

# In[3]:


class students:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# In[4]:


# Create the class
class Person:

    def __init__(self, id, firstname, lastname, email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def updateEmail(self, email):
        self.email = email

# Instantiate the class
user = Person(
    1,
    "Barney",
    "Rubble",
    ""
)

# Print details
print("First name:", user.firstname)
print("Last name:", user.lastname)
print("Email:", user.email)
print("===================")

# Add an email address
user.updateEmail("barney_rubble_123@example.com")

# Print details again
print("First name:", user.firstname)
print("Last name:", user.lastname)
print("Email:", user.email)


# In[50]:


#SCA Assignment

#Week Two

#Assignment: Create an example of a class and function and push to github

#Solution

#Class

class students:

    def __init__(student, id, firstname, lastname, age, department, email):
        student.id = id
        student.firstname = firstname
        student.lastname = lastname
        student.age = age
        student.department = department
        student.email = email
#Function
    def updatestudentinfo(student, age, department, email):
        student.age = age
        student.department = department
        student.email = email

# Instantiate the class
student1 = students(
    202001,
    "Adebowale",
    "Alex", 
    "",
    "",
    ""
)

# Print details
print("First name:", student1.firstname)
print("Last name:", student1.lastname)
print("Age:", student1.age)
print("Department:", student1.department)
print("Email:", student1.email)
print("===================")

# Add age and an email address
student1.updatestudentinfo(23, "Medicine", "adebowale.alex@gmail.com")

# Print details again
print("First name:", student1.firstname)
print("Last name:", student1.lastname)
print("Age:", student1.age)
print("Department:", student1.department)
print("Email:", student1.email)


# In[18]:


class Person(object):
    def __init__(self, id, name, city, account_balance):
        self.id = id
        self.name = name
        self.city = city
        self.account_balance = account_balance

    def adjust_balance(self, offset):
        self.account_balance += offset


if __name__ == "__main__":
    p = Person(123, "bob", "boston", 100.0)
    p.adjust_balance(50.0)
    print("done!: {}".format(p.__dict__))


# In[19]:


from collections import namedtuple

Person = namedtuple("Person", ["id", "name", "city", "account_balance"])


def adjust_balance(person, offset):
    return person._replace(account_balance=person.account_balance + offset)


if __name__ == "__main__":
    p = Person(123, "bob", "boston", 100.0)
    p = adjust_balance(p, 50.0)
    print("done!: {}".format(p))


# In[44]:





# In[ ]:




