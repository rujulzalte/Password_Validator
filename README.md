# Password_Validator
This is a code which can be used to validate if the entered password is strong password or not.

## Getting Started
Password validator is a code which can used to validate the strength of the mentioned password. Whole program is based on functions where various functions are defined to validate different test cases.

## Introduction
This project was build so that whenever a password is set it shouldn't be prone to any kind of attacks. To prevent it from vulnerability the password should be strong enough so that it doesn't  gets hacked. There are some basic validation criteria which can asure that the password mentioned is strong or not. Based on that the code is developed.

## Requirements
To run the code you are supposed to have [python](https://www.python.org/downloads/) installed in your device (IDE recomended).

* Version greater than **3.6.x**
* You also need [**CSV Library**](https://stackoverflow.com/questions/41061824/install-csv-package-in-pycharm)

## Instructions
The code validates the given password on certain instructions which are mentioned here
* Password length has to be of minimum of 12 character
* Password length has to be of maximum of 20 character
* Password string must consist of minimum 3 characters - Upper Case (A-Z)
* Password string must consist of minimum 3 characters - Lower Case (a-z)
* Passowrd string should consist minimum 3 of Numbers - (0-9)
* Passowrd string should consist of atleast 3 Special Characters.
    - Allowed Special Characters are - !, @, #, $, %, ^, &, *, (, ), _, -, and ~
* Password string should start with either any special character or 2 digit number
* Password string cannot contain  5 same characters or numbers consecutively
* Password string cannot have 3 same special charaters consecutively
* Password string cannot have the UserName into it at any position
* Password string cannot be the [commonly used password](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords#SplashData)

## How to Run
- To run the code you need to run the [source code](https://github.com/rujulzalte/Password_Validator/blob/main/Password_Validator_Code/Source_Code.py) file which is present.
- You need to make a copy of the [CSV file](https://github.com/rujulzalte/Password_Validator/blob/main/Password_Validator_Code/Common_password.csv) in your device.
- After creating copy in the device copy the file location of the CSV file in your device and paste the location in source code at **line 269** 

## Details of Source Code 
_This code is a basic implementation of [functions](https://www.w3schools.com/python/python_functions.asp) and_
_[external modules](https://www.w3schools.com/python/python_modules.asp), with [conditional statement](https://www.w3schools.com/python/python_conditions.asp).
Here I have used the [CSV Module](https://docs.python.org/3/library/csv.html#:~:text=The%20csv%20module%20implements%20classes,CSV%20format%20used%20by%20Excel.)_
_,it is a module which is used to operate a comma sperated file. Through that module we can do various opreations using the file._
  
## Function Description
There are various function used to implement the code and this functions are used to validate different conditions of the password.
In every user name and the password entered by the user is passed so that the function can compare over the given condition.
- **main()** : This is the main driver function through which all the function call takes place and the whole code is driven through it.
- **input_user()** : Input user function is used to take the user name from the user, which he/she would be mentioning while login.
- **input_pass()** : This function is used to take the password against which the user wants to be get validated. 
- **check_min_length()** : This is the first validation function where the length of the password is checked and it continues its validation only if the password length is more than 11 characters.
- **check_max_length()** : Here the function validates the password length again but the validation is statified only if the length is less than 20 characters.
- **check_upper()** : This function is used to validate the password and checks if the password consists of atleast 3 upper case characters.
- **check_lower()** : This function is used to validate the password and checks if the password consists of atleast 3 lower case characters.
- **check_num()** : This function is used to validate the password and checks if the password consists of atleast 3 numerical values.
- **check_special()** : Check_special function checks if the password contains minimum 3 special character in the string.
- **check_first()** : The function is used to check the inital characters of the string and validates if the first character is specail character or the first two character are numerical value.
- **check_con()** : This function checks if there are any 5 consecutive value in the password string.
- **check_con_special()** : This function checks if there are any 3 consecutive specail character in the password string.
- **check_user()** : This function is used to check if the password string given contains user name mentioned in it.
- **check_common()** : It is a function which is used to check if the password string is among the [most commonly used passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords#SplashData).


## More Resources

* [Learing python](https://www.w3schools.com/python/)
* [Installtion of python](https://www.python.org/downloads/)
* [Python coding questions](https://www.programiz.com/python-programming/examples)




###### [Created By : Rujul Zalte](https://www.linkedin.com/in/rujulzalte/)
###### [Software Engineer - Consultadd](https://consultadd.com/)
