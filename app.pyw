from tkinter import *
import csv
import pandas as pd

screen = Tk()
screen.geometry("500x500")
screen.title("CSC212 Form")

score_list = []

def eda(): 
    '''
    Calculate the maximum, minimum and average score to a csv file
    '''
    calc = pd.read_csv('score_sheet.csv')
    maximum_score = calc.Score.max()
    average = calc.Score.mean()
    minimum_score = calc.Score.min()
    row_of_max_score = calc[calc['Score']== maximum_score]
    
    with open("eda.csv","w",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow(["Max_Score", "Min_Score", "Mean_Score"])
        writer.writerow([maximum_score, minimum_score, average])
    '''
    Get the best student from the maximum score and send to a csv file
    '''
    row_of_max_score.to_csv('best_student.csv', index=False)
    
    
def get_info(): 
    '''
    get the student input details from the GUI
    '''
    first_name_info = firstname.get()
    last_name_info = lastname.get()
    matric_number_info = matric_number.get()
    score_info = score.get()
    score_list.append(score_info)

    student = {
        'firstName' : first_name_info,
        'lastName' : last_name_info,
        'matric': matric_number_info,
        'score': score_info
    }
    
    return student 

with open("score_sheet.csv","w",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow(["Firstname", "Lastname", "Matric", "Score"])
File.close()
    
def student_info():
    '''
    Send the details gotten from the gui to a csv file
    '''
    student_detail = get_info()
    print(f"Firstname: {student_detail['firstName']} \nLastname: {student_detail['lastName']} \nMatric Number: {student_detail['matric']} \nScore: {student_detail['score']} \n ")
    
  
    with open("score_sheet.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow([student_detail['firstName'], student_detail['lastName'], student_detail['matric'], student_detail['score']])
    File.close()
    
           
    print(f"{str(student_detail['matric'])} has been recorded successfully")
    
    eda()
    

def stats():
    
    lists = get_info()
    
    '''
    get the scores of those that passed and send to a csv file
    '''
    if lists["score"] < 40:   
        with open("failed.csv","a",newline="\n") as File:
            writer = csv.writer(File)
            writer.writerow([lists["firstName"], lists["lastName"], lists["matric"], lists["score"]])
        File.close()
        
    '''
    get the scores of those that failed and send to a csv file
    '''
    if lists["score"] > 40: 
        with open("passed.csv","a",newline="\n") as File:
            writer = csv.writer(File)
            writer.writerow([lists["firstName"], lists["lastName"], lists["matric"], lists["score"]])
        File.close()


#GUI

heading = Label(text="CSC Form", bg="grey", width="1000", height="2")
heading.pack()

first_name_label = Label(text = "Firstname")
first_name_label.place(x = 10, y = 50)
last_name_label = Label(text = "Lastname")
last_name_label.place(x = 10, y = 120)
matric_number_label = Label(text = "Matric Number")
matric_number_label.place(x = 10, y = 190)
score_label = Label(text = "Score")
score_label.place(x = 10, y = 260)


firstname = StringVar()
lastname = StringVar()
matric_number = IntVar()
score = IntVar()

firstname_entry = Entry(textvariable = firstname, width = 50)
firstname_entry.place(x = 10, y = 80)
lastname_entry = Entry(textvariable = lastname, width = 50)
lastname_entry.place(x = 10, y = 150)
matric_number_entry = Entry(textvariable = matric_number, width = 50)
matric_number_entry.place(x = 10, y = 220)
score_entry = Entry(textvariable = score)
score_entry.place(x = 10, y = 290)

submit = Button(screen, text = "Submit", width = "15", height = "1", command = lambda: [student_info(), eda(), stats()])
submit.place(x = 10, y = 330)


screen.mainloop()