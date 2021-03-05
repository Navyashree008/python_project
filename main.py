def check_userid(name):
    f = open("userdetail.json","r")
    f1 = f.read()
    if name in f1:
        print("name alredy exist")
        signupWaala()
    else:
        print("valid user name")

def check_login_info(name, password):
    import json
    with open("userdetail.json","r") as f:
        f1 = json.load(f)
    for i in f1["user"]:
        if i["name"]== name and i["password"]==password:
            # return "logged in successfully"
            return "my name is :" + i["name"]+ "bio:" + i["profile"]["description"] + "dob:" + i["profile"]["dob"] + "my hobbies are:" + i["profile"]["hobbies"] + "gender:" + i["profile"]["gender"]
    return "invalid user details"

# to check whether a valid password or not:-
def valid_password(password,check_password):
    if '@'in password or '#' in password:
        i = 48
        while i <= 57:
            num = chr(i)
            if num in password:
                # break
                if password == check_password:
                    return "your password is set correct ,we can move further "
            i+=1
        else:
            print("the password should contain number also")
            signupWaala()
                

    else:
        print("the password should contain at least one special charecter")
        signupWaala()
        
# # input to dictionary


def dictionary(name,password,profile):
    info_dict = {}
    info_dict['name'] = name
    info_dict['password'] = password
    info_dict['profile'] = profile
    return info_dict 

# import json

def signupWaala():
        #  sign up information will be asked here:
    name = input("enter your name:")
    check_userid(name)
    password = input("enter the password:")
    check_password = input("enter the password once again:")
    valid_password(password,check_password)
    print("congrats",name,"you are signed in successfully")
    description = input("enter the description")
    dob = input("enter your date of birth")
    hobbies = input("mention your hobbies")
    gender = input("enter the gender")
    profile = {}
    profile['description'] = description
    profile['dob'] =dob
    profile['hobbies'] = hobbies
    profile['gender'] = gender
    info = dictionary(name,password,profile)
    import json
    with open("userdetail.json","r") as f:
        main_dict = json.load(f)
    main_dict['user'].append(info)
    with open("userdetail.json","w") as f:
        json.dump(main_dict,f,indent= 3)
    print("signup processess is done")

def login():
    name = input("enter your name:")
    password = input("enter the password:")
    print(check_login_info(name,password))
    # with open("userdetail.json","r") as f:
    #     main_dict = json.load(f)
    # info_list = main_dict['user']
    # i = 0
    # while i < len(info_list):
    #     if name in info_list[i]:
    #         print(info_list[i])
    #     i+=1
user_wish = input("enter whether you want to login or signup")
if user_wish == "signup":
    signupWaala()
else:
    login()
    

