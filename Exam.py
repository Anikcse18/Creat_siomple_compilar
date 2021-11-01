import os
def iskeyword(x):
    key_word = ["auto","break","case","char","const","continue","default",
							"do","double","else","enum","extern","float","for","goto",
							"if","int","long","register","return","short","signed",
							"sizeof","static","struct","switch","typedef","union",
							"unsigned","void","volatile","while","main"]
    flag = 0
    for i in range(len(key_word)):
        if (key_word[i]==x):
            flag=1
            break
    return flag



def main():
    buffer = []
    operator = ['+','-','*','/','%','=']
    special_charecter = ["(", ")" ,"[","]",",","{","}",";","?","#","$" ]

    my_file = open('program.txt','r')
    file_name = "program.txt"
    operator_array = []
    keyword_array=[]
    variable_array=[]
    special_array = []
    numbers_array = []
    invaild_array = []


    global char

    if os.path.getsize(file_name) == 0:
        print("Error while opening the file")

    else:
        while 1:
            char = my_file.read(1)
            if not char:   #read one charetter
                break

            #checking operatr
            for i in range(len(operator)):
                    if char == operator[i]:  #operator check

                        operator_array.append(char)
                       # operator_array.append(char) #Store all operrator in this array

           #checking special charecter

            for i in range(len(special_charecter)):
               if char == special_charecter[i]:
                   special_array.append(char)

            # checking special charecter with number

            if char.isalnum():
                buffer.append(char)

            elif (char == " " or char == "\n"):

                x = "".join(buffer)

                buffer.clear()
                if iskeyword(x) == 1:
                    keyword_array.append(x)

                else:

                    if x == "":
                        pass
                    else:
                        if x.isnumeric():

                            numbers_array.append(x)
                        else:
                            if x[0].isnumeric():
                                invaild_array.append(x)
                            else:

                                variable_array.append(x)

    keyword_array = list(dict.fromkeys(keyword_array))  # Filtaring Same value

    print("Numbers OF Key Word: ",len(keyword_array),'\n')

    print("|-------------------|")
    print("|      Keyword      |")
    print("|-------------------|")



    for i in keyword_array:
        print("|      ",i,"        ")
        print("|-------------------|")


    print("\n")
    print("\n")

    variable_array = list(dict.fromkeys(variable_array))  # Filtaring Same value

    print("Numbers OF Valid Identifiers: ", len(variable_array), '\n')
    print("|-------------------|")
    print("| Valid Identifiers |")
    print("|-------------------|")



    for i in variable_array:
        print("|      ",i,"        ")
        print("|-------------------|")


    print("\n")
    print("\n")

    operator_array = list(dict.fromkeys(operator_array))  # Filtaring Same value

    print("Numbers of Math Operators: ", len(variable_array), '\n')

    print("|-------------------|")
    print("|   Math Operator   |")
    print("|-------------------|")


    for i in operator_array:
        print("|      ", i, "        ")
        print("|-------------------|")

    print("\n")
    print("\n")
    invaild_array = list(dict.fromkeys(invaild_array))  # Filtaring Same value
    print("Numbers of Invalid Identifiers: ", len(invaild_array), '\n')

    print("|-------------------|")
    print("| Invalid Identifier|")
    print("|-------------------|")




    for i in invaild_array:
        print("|      ", i, "        ")
        print("|-------------------|")

    print("\n")
    print("\n")

    numbers_array = list(dict.fromkeys(numbers_array))   #Filtaring Same value

    print(" Numbers of Number: ", len(numbers_array), '\n')


    print("|-------------------|")
    print("|      Numbers      |")
    print("|-------------------|")

    for i in numbers_array:
        print("|      ", i, "        ")
        print("|-------------------|")




if __name__ == "__main__":
    main()