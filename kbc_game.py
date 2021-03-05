question_list = ["How many continents are there?", "What is the capital of India?","NG mei kaun se course padhaya jaata hai?"    # teesra question
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3,4,1]
life_line = 0
i = 0
while i < len(question_list):
    print(question_list[i])
    j = 0
    a = 1
    while j <len(options_list[i]):
        print(a,options_list[i][j])
        a+=1
        j+=1
    if life_line == 0:
        print("you can even use 50:50 life line")
    answer_input = input("enter the option number")
    if answer_input == "50:50":
        if life_line == 0:
            life_line+=1
            if i == 0:
                print("3.seven or 4.eight")
            elif i == 1:
                print("1.Chandigarh or 4.Delhi")
            elif i == 2:
                print("1.software engineering or 2.tourism")
            answer_input_2=int(input("enter no"))
            if answer_input_2 == solution_list[i]: 
                print("yeh!,its correct lets move forward")
            else:
                print("sadly your answer is wrong")
                print("you are out of game")
                break
        else:
            print("you have used your life line alredy")
    else:
        if answer_input == solution_list[i]:
            print("yeh!,its correct lets move forward")
        else:
            print("sadly your answer is wrong")
            print("you are out of game")
            break
    i+=1