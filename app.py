import database as db

def c_add_internship():
    iname = input("Internship name:")
    company = input("Company name:")
    i_year = int(input("Conducted year:"))
    db.add_internship(iname, company, i_year)

def c_view_all_internships():
    db.view_all_internships()
    
def c_search_internship_by_name():
    name = input("Enter the name to search:")
    db.search_internship_by_name(name)

def c_change_status_internship():
    id = int(input("Enter the ID: "))
    status = input("Enter the status:")
    db.change_status_internship(id,status)

def c_delete_internship():
    i_id = int(input("Enter the ID: "))
    db.delete_internship(i_id)

# Student oprations
def c_add_student():
    usn = int(input("Enter the usn: "))
    name = input("Enter the name: ")
    sem = int(input("Enter the sem: "))
    placed = int(input("Enter 1 for placed if not 0 "))
    db.add_student(usn,name,sem,placed)

def c_view_all_student():
    db.view_all_students()

def c_search_student_by_name():
    name = input("Enter the name: ")
    db.search_student(name)

def c_update_student():
    usn = int(input("Enter the usn: "))
    print("1.Name 2.Sem 3.Placed ")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        name = input("Enter the name: ")
        db.update_student(usn,'name',name)
    elif ch == 2:
        sem = int(input("Enter the sem: "))
        db.update_student(usn,'sem',sem)
    elif ch == 3:
        placed = int(input("Enter 1 for placed if not 0 "))
        db.update_student(usn,'placed',placed)
    else:
        print("Enter choice from 1 - 3")


def c_delete_student():
    usn = int(input("Enter the usn: "))
    db.delete_student(usn)

# Registrations and summary reports 
def c_reg_stu_internship():
    usn = int(input("Enter the student usn: "))
    iid = int(input("Enter the internship ID: "))
    db.reg_student_internship(usn,iid)

def c_update_stu_intership_status():
    usn = int(input("Enter the usn: "))
    status = int(input("Enter the 1 for completed and 0 for not yet: "))
    db.update_stu_intership_status(usn,status)

def c_display_reg_stud():
    db.view_all_reg_student()

def c_company_ws_count():
    db.company_ws_count()

def c_student_ws_count():
    db.student_ws_count()

def c_ws_student_reports():
    db.ws_student_reports()




while True:
    try:
        print("1. Add Internship 2.Student 3.Reports 4.Exit")
        mch = int(input("Enter you choice:"))
        
        if mch == 1:
            while True:
                try:
                    print("*"*50)
                    print("Internship programms conducted at MITE by Companies")
                    print("1.Add 2.View All 3.Search 4.Update 5.Delete 6.Main Menu")
                    print("*"*50)
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        c_add_internship()
                    elif ch == 2:
                        c_view_all_internships()
                    elif ch == 3:
                        c_search_internship_by_name()
                    elif ch == 4:
                        c_change_status_internship()
                    elif ch == 5:
                        c_delete_internship()
                    elif ch == 6:
                        break
                    else:
                        raise Exception()
                except Exception as e:
                    print("Please provide valid input 1 - 6")
        elif mch == 2:
            while True:
                try:
                    print("*"*50)
                    print("Add Students to Internship programms")
                    print("1.Add 2.View All 3.Search 4.Update 5.Delete 6.Main Menu")
                    print("*"*50)
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        c_add_student()
                    elif ch == 2:
                        c_view_all_student()
                    elif ch == 3:
                        c_search_student_by_name()
                    elif ch == 4:
                        c_update_student()
                    elif ch == 5:
                        c_delete_student()
                    elif ch == 6:
                        break
                    else:
                        raise Exception()
                except Exception as e:
                    print("Please provide valid input 1 - 6")
        elif mch == 3:
                while True:
                    try:
                        print("*"*50)
                        print("Internship programms conducted at MITE Reports")
                        print("1.Register Student 2.Display Registered Student 3.Update Status 4.Company ws count 5.Student ws count 6.Studen_ws_name_company_year 7.Main Menu")
                        ch = int(input("Enter your choice:"))
                        if ch == 1:
                            c_reg_stu_internship()
                        elif ch == 2:
                            c_display_reg_stud()
                        elif ch == 3:
                            c_update_stu_intership_status()                       
                        if ch == 4:
                            c_company_ws_count()
                        elif ch == 5:
                            c_student_ws_count()
                        elif ch == 6:
                            c_ws_student_reports()
                        elif ch == 7:
                            break
                        else:
                            raise Exception()
                    except Exception as e:
                        print(e)
                        print("Please provide valid input 1 - 4")
        elif mch == 4:
            print("Thank you programming is going to terminate.....")
            exit()
        else:
            raise Exception()
    except Exception as e:
        print("Enter valid input (1 to 3) only...")