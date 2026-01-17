file =open("sample.txt","w")
file.write("hello i am rajneesh")
file.close()

with open("raj.txt","a") as file:
    file.write("hi i am writing in file")


