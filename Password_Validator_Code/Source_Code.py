# This is the code for password validator which
# can validate how strong the password is


# Instruction function shows all the instruction
# which are needed to be followed to create a
# strong password

def instruction():
    print("\nWelcome to Password Validator\n")
    print("Here are set of instructions which \
you are supposed to follow")
    print("\nPassword length has to be of minimum\
 of 12 character")
    print("Password length has to be of maximum \
of 20 character")
    print("Password string must consist of Characters \
- Upper Case (A-Z)")
    print("Password string must consist of Characters \
- Lower Case (a-z)")
    print("Passowrd string should consist of \
Numbers - (0-9)")
    print("Passowrd string should consist of \
atleast 3 Special Characters.")
    print("Allowed Special Characters are - \
!, @, #, $, %, ^, &, *, (, ), _, -, and ~")
    print("Password string should start with either \
any special character or 2 digit number")
    print("Password string should have to have at least \
3 Upper Case and 3 Lower Case characters")
    print("Password string cannot contain  5 same \
characters or numbers consecutively")
    print("Password string  cannot have the UserName \
into it at any position")
    print("Password string cannot have 3 same special \
charaters consecutively\n")


def input_name():
    user_name = list(input("\nEnter the user name \
to login \n>>"))
    return user_name


def input_pass():
    user_pass = list(input("\nEnter the password to \
to login \n>>"))
    return user_pass


# Function to check the minimum length of password
def check_min_length(user_name, user_pass):
    print("\nChecking minimum length of password\n")
    if (len(user_pass) > 12):
        print("PASSED!!! The minimum length \
is statisfied\n")
        return
    else:
        print("The password should consists \
of minimum 12 characters")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check the maximum length of password
def check_max_length(user_name, user_pass):
    print("\nChecking maximum length of password\n")
    if (len(user_pass) < 20):
        print("PASSED!!! The maximum length \
is statisfied\n")
        return
    else:
        print("The password should consists \
of maximum 20 characters")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check for minimum 3 upper case letter
def check_upper(user_name, user_pass):
    print("\nChecking for minimum 3 \
upper case letters")
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'X', 'Y', 'Z']
    count_u = 0
    for i in user_pass:
        if i in upper:
            count_u = count_u + 1
        else:
            continue
    count_u = count_u + 1
    if count_u > 2:
        print("\nPASSED!!! There are more than 3 \
upper case letters in password")
        return
    else:
        print("\nThere should be minimum 3 \
upper case letters in the password")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check for minimum 3 lower case letter
def check_lower(user_name, user_pass):
    print("\nChecking for minimum 3 \
lower case letters")
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'x', 'y', 'z']
    count_l = 0
    for i in user_pass:
        if i in lower:
            count_l = count_l + 1
        else:
            continue
    count_l = count_l + 1
    if count_l > 2:
        print("\nPASSED!!! There are more than 3 \
lower case letters in password")
        return
    else:
        print("\nThere should be minimum 3 \
lower case letters in the password")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check for numbers in it
def check_num(user_name, user_pass):
    print("\nChecking for numbers")
    num = ['1', '2', '3', '4', '5',
           '6', '7', '8', '9', '0']
    count_n = 0
    for i in user_pass:
        if i in num:
            count_n = count_n + 1
        else:
            continue
    if count_n > 1:
        print("\nPASSED!!! Password consists \
of number")
        return
    else:
        print("\nThere should be numbers\
 in password")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check for minimum 3 special character
def check_special(user_name, user_pass):
    print("\nChecking for minimum 3 \
special character")
    special = ['!', '@', '#', '$', '%', '^', '&',
               '*', '(', ')', '-', '_', '~']
    count_l = 0
    for i in user_pass:
        if i in special:
            count_l = count_l + 1
        else:
            continue
    if count_l > 2:
        print("\nPASSED!!!  There are more than 3 \
special character in password")
        return
    else:
        print("\nThere should be minimum 3 \
special characters in the password")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check first character as number or special character
def check_first(user_name, user_pass):
    print("\nChecking for first number or \
special character")
    special1 = ['!', '@', '#', '$', '%', '^', '&',
                '*', '(', ')', '-', '_', '~']
    num1 = ['1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0']
    if user_pass[0] in special1:
        print("\nPASSED!!! First character is special character")
        return
    elif (user_pass[0] in num1) and (user_pass[1] in num1):
        print("\nPASSED!!! First and second character \
is number")
        return
    else:
        print("\nFirst character should be \
specail character or First and Second character \
should be number")
        user_pass = input_pass()
        main(user_name, user_pass)


# Function to check if there are 5 consecutive
# characters or numbers present
def check_con(user_name, user_pass):
    flag = 0
    for i in range(len(user_pass) - 4):
        if (
        user_pass[i] == user_pass[i + 1] and
        user_pass[i + 1] == user_pass[i + 2] == 
        user_pass[i + 3] == user_pass[i + 4]
        ):
            flag = 1
    if flag == 1:
        print("\nThere are 5 consecutive values")
        user_pass = input_pass()
        main(user_name, user_pass)
    else:
        print("\nPASSED!!! There is no consecutive value")
        return


# Function to check 3 consecutive special character
def check_con_special(user_name, user_pass):
    count = 0
    special1 = ['!', '@', '#', '$', '%', '^', '&',
                '*', '(', ')', '-', '_', '~']
    print("\nChecking for 3 consecutive \
special characters")
    for i in range(len(user_pass) - 2):
        if (
        user_pass[i] in special1 and
        user_pass[i] == user_pass[i + 1] and
        user_pass[i + 1] == user_pass[i + 2]
        ):
            count = 1
    if count == 1:
        print("\nThere are 3 consecutive \
special character")
        user_pass = input_pass()
        main(user_name, user_pass)
    else:
        print("\nPASSED!!! There is no 3 consecutive \
special character")
        return


# Function to check if password consits of username
def check_user(user_name, user_pass):
    print("\nChecking for username \
in password")
    user_name = "".join(user_name)
    user_pass = "".join(user_pass)
    if user_name in user_pass:
        print("\nPassword should'nt consist \
username in it")
        user_pass = input_pass()
        main(user_name, user_pass)
    else:
        print("\nPASSED!!! Password does'nt consist \
of username in it")
        return


# This is the driver function
def main(user_name, user_pass):
    check_min_length(user_name, user_pass)
    check_max_length(user_name, user_pass)
    check_upper(user_name, user_pass)
    check_lower(user_name, user_pass)
    check_num(user_name, user_pass)
    check_special(user_name, user_pass)
    check_first(user_name, user_pass)
    check_con(user_name, user_pass)
    check_con_special(user_name, user_pass)
    check_user(user_name, user_pass)


instruction()
user_name = input_name()
user_pass = input_pass()
main(user_name, user_pass)
