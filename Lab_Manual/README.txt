https://github.com/revacprogramming/python101-VikkiVignesh/blob/91c6f54dc3ebda8bd57120813558d6514c9bdc87/Lab_Manual
Part-A
1a). “LIST1” is a list that contains “N” different SRN of students read using a user defined function with the help of input() function. It is required to add SRN of “M” more students that are to be appended or inserted into “LIST1” at the appropriate place. The program must return the index of the SRN entered by user.

Changed 1.a)

Write an api ( Set of functions) to manage student registration numbers (SRN)

def input_srn():

'''
srn is a string of 6 digits.
takes input from the user and checks if the srn 
has 6 digits and return srn or raises an invalid srn exception.
'''

def append_srn(srnlist,srn):

'''
adds an srn to srn list if the srn is not already present.
srn should be inserted in a sorted lexicographical order.
raises an srn exception if the srn is already present.
'''

def search_srn(srnlist,srn):

'''
will return the index of srn if present or will raise an srn exception
if the srn is not found.
'''

def merge_srn(srnlist1, srnlist2):

'''
merge two srn lists and return the merged list'''
'''
[ ]
  
  
1b).“TUPLE1” and “TUPLE2” are two tuples that contain “N” values of different data types read using the user defined function “READ” with the help of input() function. Elements of “TUPLE1” and “TUPLE2” are to be read one at a time and the “larger” value among them should be placed into “TUPLE3”. Display all tuples.

1.b) Write a function that takes tuple1 and tuple2 and returns tuple3.

def input_tuple(n):
  '''takes n inputs from the user and creates a tuple'''

def compare_elements(tuple1, tuple2):
'''return t3. t3[i] is greater of t1[i] and t2[i]'''

def output_tuples(t1,t2,t3):
'''print three tuples one below another'''

def main():
   n = int(input("Enter size of tuples")
   t1 = input_tuple(n)
   t2 = input_tuple(n)
   t3 = compare_elements(t1,t2)
   output_tuples(t1,t2,t3)

if __name__ == __main__:
  main()
[ ]

2a). SET1 and SET2 are two sets that contain unique integers. SET3 is to be created by taking the union or intersection of SET1 and SET2 using the user defined function Operation(). Perform either union or intersection by reading choice from user. Do not use built in functions union() and intersection() and also the operators "|"and "&".

Expected Output

Enter Set1? 1 3 4 8
Enter Set2? 2 5 7 6
Enter operation (u/n)? u

Set3: 1 2 3 4 5 6 7 8
[1]
# make this code work
def main()
    setu = input_set()
    set1 = input_set()
    set2 = input_set()
    set3 = input_set3()
    operation = get_operation()
    operands = get_operands()
    result = perform_operation(operation,*operands)
    print(result)
    print_report(setu,set1,set2,set3) # members in only s1 and s2, members in only s2,s3, members in only s3,s1, members not in s1,s2,s3 and members in all s1,s2,s3  
2b).The Dictionary "dict1" contains N Elements and each element in dictionary has the operator as the KEY and operand’s as VALUES. Perform the operations on operands using operators stored as keys. Display the results of all operations.

[ ]
def input_data():
   d = _______
   while(True):
     operator = _______
     if(operator == "end"):
       break;
     operand1 = _______
     operand2 = _______
    # complete the code
def evaluate(ed)
  pass # complete the code
def print_ed(ed)
  pass # complete the code

def main():
  ed=input_data()
  evaluate(ed)
  print_ed(ed)
  
3a).A substring “Substr” between index1 and index2 is to be extracted from the given input string “Str1”, which is read using input(). Display the substring “Substr” using a user defined function if available in string “Str1”, otherwise display NULL.

[ ]

3b).A string containing multiple words is to be read from the user one at a time, after reading perform following operations. i) Convert all the strings to uppercase and display

OUTPUT:

  how many words do you want to enter: 3
  Enter next word: ding
  Enter next word: dong
  Enter next word: bell
  DING
  DONG
  BELL
[ ]

4a).Consider the text file, “Std.txt”, with the details of students like SRN, NAME, SEMESTER, SECTION AND AVG_MARKS. Read the file, “Std.txt” and display the details of all the students of 4th Semester “ A” Section who have scored more than 75%.

[ ]

4b).Consider the text file “Emp.txt”, with the details of Employees like EMP_CODE, EMP_NAME, BASIC_SALARY, DA, GROSS_SALARY, NET_SALARY, LIC, PF and TOTAL- DEDUCTIONS. Read EMP_CODE, EMP_NAME, BASIC_SALARY, DA, LIC and PF from the user using input() and compute the following:

i) TOTAL_DEDUCTIONS= (LIC+PF)

ii) GROSS_SALARY= BASIC_SALARY+ DA

iii) NET_SALARY= GROSS_SALARY – TOTAL_DEDUCTIONS.

Write the above data to file for each employee. Read the content of “Emp.txt” and display the details of each employee.

[ ]
# there are lot of interesting design issues.
# should employees class store data in memory or in file.
# Is there a default file name for employees data
# Think and try.
import csv

class employee:
  pass

class employees: 
  pass

def input_employees(e,n):
  for i in n:
    e_+= get_employee()

def main():
  n = int(input("Create how many employee records"))
  e = employees()
  input_employees(e,n)
  print(e)

main()

5a). A “CAR” has the attributes COMPANY_NAME, MODEL, COLOR, MANUFACUTING_YEAR and PRICE. A Class is required to be created for “CAR” to store the above attributes and perform the following operations:

i) Get the details of “CAR” object from user and store into Array of objects

ii) Display the details of “CAR” object based on “COMPANY”, “MODEL” and “PRICE”.

[ ]
class car:
5b).Airline Reservation System contains the attributes of passengers such as NAME, PAN_NO. MOBILE_NO, EMAIL_ID, SOURCE, DESTINATION, SEAT-NO, AIR-FARE and TRAVEL_DATE. A Class is required to be created for “Airlilne” with the above attributes and perform the following operations:

i) Get the details of “Airline” object from user and store into Array of objects

ii) List details of all the passengers who travelled from “Bengaluru to London”.

[ ]

6a).“Arr_1” is an integer array of size M x N. Size and content of the array is to be read using input() by using the user defined function READ_DATA(). It is required to display the

i) Diagonal elements of ”Arr_1”

ii) Elements of mth row ( row no should be entered by user)

iii) Elements of nth column (column no should be entered by user)

[ ]
def get_dimension():
  pass
def read_array(m,n):
  pass

def main():
  m,n=get_dimensions()
  a = read_array(m,n)
  m = int(input("enter mth row"))
  print(________) # print mth row
  n = int(input("enter column to be printed"))
  print(_______) # print nth column
6b).The dictionary “DICT1” contains the pass percentage of each semester of B. Tech in CSE, where, ” Semester” acts as the key and “Pass Percentage” acts as the value. A Python Pandas dataframe is required to be created using the dictionary “DICT1” and display it using a user defined function.

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

[ ]

Part-B (Mini Project: Library Management System)
1.Develop a program to create the class “USER” with the attributes USER_NAME, USER_ID, SCHOOL_NAME, ADDRESS, PHONE_NO, EMAIL_ID, DOB and AGE. The functions add_user(), delete_user(), edit_user(), search_user() should be part of the class. Instantiate “User” class with 10 objects. Read the attributes of each “User” object using input() and store them in the file “User_File.txt”.

2.Develop a program to get the name of the “User” object whose details are to be deleted. Read the “User_File.txt” and delete the “User” object if found. Display the contents of “User_File.txt” after deletion.

3.Develop a program to get the name of the “User” object whose details are to be edited (modified). Edit the details of the user object in the file “User_File.txt” and display the contents after modification.

4.Develop a program to create the class “BOOK” with the attributes TITLE, AUTHOR, PUBLISHER, YEAR, PRICE, SCHOOL_NAME and the functions add_book(), delete_book(), edit_book() and search_book(). Instantiate “Book” class with 10 objects. Read the attributes of each “BOOK” object using input () and store them in the file “Book_File.txt”.

5.Develop a program to get the name of the “BOOK” object whose details are to be deleted. Read the “Book_File.txt” and delete the “BOOK” object whose details match with the data entered. Display the contents of “Book_File.txt” after deletion.

6.Develop a program to get the name of the “BOOK” object whose details are to be edited (modified). Edit the details of the “Book” object in the file “Book_File.txt” and display the contents after modification.

7.Develop a program to create the class “TRANSACTION” with the attributes USER_ID, USER_NAME, AUTHOR, TITLE, EDITION, ISSUE_DATE,DUE_DATE and RETURN_DATE and the functions issue_book(), return_book() and search_book(). Instantiate “Transaction” class with 10 objects. Read the attributes of each “Transaction” object using input() and store them in the file “TransactionFile.txt”. Develop a program to issue the book as requested by the user. Update the attributes in “Transaction _File” and display the contents of file.

8.Develop a program to return the book. Edit the details of the user like USER_ID, USER_NAME, AUTHOR, TITLE, EDITION, ISSUE_DATE, DUE_DATE and RETURN_DATE in “TransactionFile.txt” and display the contents after modification. Compute the fine amount to be paid if return_date is not same as due_date. If both return_date and due_date are same and put zero in fine_amount.

9.Develop a program to search for a book using its “author”. Display the message “available” if search is successful otherwise display the message “not available”.

10.Develop a program to get a list of users by referring to “User_File.txt” and “Transaction_File.txt”.

11.Develop a program to get List of Books in stock by referring to “Book_File.txt” and “Transaction_File.txt”.

12.Develop a program to get List of Books Issued by referring to “User_File”, “Book_File” and “Transaction_File”.

13.Develop a project by integrating User, Books, Transaction and Reports Modules.

[ ]
import shelve
''' https://docs.python.org/3/library/shelve.html '''


def users:
  def __init__(self, filename):
    pass
  def get_user(self, id):
    pass
  def get_users_name(self,name):
    pass
  def update_user( id, u)
    pass
  def add_user(id,u)
    pass
  def print(self):
    pass

class user:
  def __init__(user_name, user_id, school_name, address, phone_no, email_id, dob):
    'pass'
               

class books:
  pass

class book
  pass

class Transaction:
  def __init__()
  def __str__()

class Transactions:
  def __init__(self,filename):
    pass
  def issue_book(self,b,u.due_date)
  def recieve_book(self,b,u)

# how about using pdb as user interface.
# how about using python interpreter as user interface.


