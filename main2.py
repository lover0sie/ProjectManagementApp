# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 21:43:11 2021

@author: Administrator
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sqlite3


#------Coding was done by Nur Adilah Syamim for Python Programming project----#

#-------------------------------Pop Ups---------------------------------------#

class PopUpLogin (QtWidgets.QDialog):
     def __init__(self):
        super(PopUpLogin, self).__init__()
        loadUi("Dialog-Login.ui", self)
        self.resize(600, 200)                
        self.Ok.clicked.connect(self.close)
        
class PopUpSignUp (QtWidgets.QDialog):
     def __init__(self):
        super(PopUpSignUp, self).__init__()
        loadUi("Dialog-Registered.ui", self)
        self.resize(600, 200)
        self.Ok.clicked.connect(self.close)
        
class PopUpLogOut (QtWidgets.QDialog):
     def __init__(self):
        super(PopUpLogOut, self).__init__()
        loadUi("Dialog-Logout.ui", self)
        self.resize(600, 200)
        self.Ok.clicked.connect(self.close)
        
class PopUpCreatedProject (QtWidgets.QDialog):
     def __init__(self):
        super(PopUpCreatedProject, self).__init__()
        loadUi("Dialog-CreatedProject.ui", self)
        self.resize(600, 200)
        self.Ok.clicked.connect(self.close)
        
class PopUpChangeProject(QtWidgets.QDialog):
    def __init__(self):
       super(PopUpChangeProject, self).__init__()
       loadUi("Dialog-UpdatedProject.ui", self)
       self.resize(600, 200)
       self.Ok.clicked.connect(self.close)
       
class PopUpDeleteProject(QtWidgets.QDialog):
    def __init__(self):
       super(PopUpDeleteProject, self).__init__()
       loadUi("Dialog-DeletedProject.ui", self)
       self.resize(600, 200)
       self.Ok.clicked.connect(self.close)
       
class PopUpSetUpMeeting(QtWidgets.QDialog):
    def __init__(self):
       super(PopUpSetUpMeeting, self).__init__()
       loadUi("Dialog-SetUpMeeting.ui", self)
       self.resize(600, 200)
       self.Ok.clicked.connect(self.close)   
         
#---------------------------------End-----------------------------------------#
        
#------------------------Welcome Page Section---------------------------------#

class WelcomePage (QtWidgets.QDialog): 
    def __init__(self):
        super(WelcomePage, self).__init__()
        loadUi("WelcomePage.ui", self)                     #load the WelcomePage ui
        self.setWindowTitle("Projert Management App")                    
        self.Login.clicked.connect(self.gotologinpage)     #it will direct to the login page
        self.SignUp.clicked.connect(self.gotosignup)       #it will direct to the signup page
        
    def gotologinpage(self):                           
        registerpage = LoginPage()
        widget.addWidget(registerpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
                    
    def gotosignup(self):                              
        signup = SignupPage()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
#---------------------------------End-----------------------------------------#

#-----------------------------Login Page Section------------------------------#

class LoginPage(QtWidgets.QDialog): 
    def __init__(self):
        super(LoginPage, self).__init__()
        loadUi("loginPage.ui", self)                                   #load the LoginPage ui
        self.Login.clicked.connect(self.loadusers)                     #it will direct to the view projects page
        self.password_box.setEchoMode(QtWidgets.QLineEdit.Password)    #it will make the password appear as dots
        self.Back.clicked.connect(self.gotomainpage)                   #return to the welcome page
       
    def loadusers(self): 
        
        username = self.username_box.text()
        password = self.password_box.text()
        
        #warns the user to fill in every field 
        if len(username)==0 or len(password)==0:                              
            self.error.setText("Please fill in your username or password")
               
            
        else:
            #establish a connection to the database:
            conn = sqlite3.connect("ProjectManagementApp.db")     
            #to execute the queries:               
            cur = conn.cursor() 
            
            query = 'SELECT password FROM users WHERE username=\''+username+"\'" #selecting the password column based on the username
            cur.execute(query) 
            result_pass = cur.fetchone()[0]                                      #information fetched in is in a form of tuple (example: Tuple = (1,2,'a'))
            
            #compare the information fetched from the database with the input password 
            #user is allowed to proceed if the input password is the same as the information fetched from database
            if result_pass == password:                                          
                self.error.setText("")
                
                #a popup will show that the user has sucessfully logged into the system
                popup = PopUpLogin()                                            
                popup.exec()
                
                mainmenu = MainMenuPage()                                      
                widget.addWidget(mainmenu)
                widget.setCurrentIndex(widget.currentIndex()+1)
                
            #error will be shown if password is false  
            else:
                self.error.setText("Password is incorrect")                     
                    
    #returns to the welcome page   
    def gotomainpage(self):                                                     
        mainpage = WelcomePage()
        widget.addWidget(mainpage)
        widget.setCurrentIndex(widget.currentIndex()+1)

#---------------------------------End-----------------------------------------#       
 
#-----------------------------Sign Up Page------------------------------------#
            
class SignupPage(QtWidgets.QDialog): 
    def __init__(self):
        super(SignupPage,self).__init__()
        loadUi("SignUpPage.ui",self)                            #load the SignUpPage ui
        self.SignUp.clicked.connect(self.createaccfunction)     #it will register the details of the new account
        self.Back.clicked.connect(self.gotomainpage)            #it will go back to welcome page 
        
    def createaccfunction(self): 
        
        FirstName = self.firstname_box.text()
        LastName = self.lastname_box.text()
        Username = self.username_box.text()
        Email = self.email_box.text()
        Password = self.password_box.text()
        ConfirmPassword = self.confirmpassword_box.text()
        
        #warns the user to fill in every field
        if len(FirstName)==0 or len(LastName)==0 or len(Username)==0 or len(Email)==0 or len(Password)==0 or len(ConfirmPassword)==0:
            self.error.setText("Please fill in all fields")                      
        
        #warns the user if the passwords do not match
        elif Password!=ConfirmPassword:
            self.error.setText("Passwords do not match")                         
            
        else:
            #establish a connection to the database
            conn = sqlite3.connect("ProjectManagementApp.db")                    
            cur = conn.cursor()                   
            user_info = [FirstName, LastName, Username, Email, Password, ConfirmPassword] 
            cur.execute('INSERT INTO users (firstname, lastname, username, email, password, confirmpassword) VALUES (?,?,?,?,?,?)', user_info)
            conn.commit()
            conn.close()
            self.error.setText("")
            
            #a popup will show to confirm that the user has registered into the system
            popup = PopUpSignUp()                                                
            popup.exec()
            
            homepage = WelcomePage()
            widget.addWidget(homepage)
            widget.setCurrentIndex(widget.currentIndex()+1)
     
    #returns to the welcome page
    def gotomainpage(self): 
        mainpage = WelcomePage()
        widget.addWidget(mainpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
#---------------------------------End-----------------------------------------#

#--------------------------Main Menu Page----------------------------------#
        
class MainMenuPage (QtWidgets.QDialog): 
    def __init__(self):
        super (MainMenuPage,self).__init__()
        loadUi("MainMenuPage.ui",self)                                       #load the MainPage ui                                 
        
        self.create_a_project.clicked.connect(self.createprojects)   #it will direct to create project page
        self.update_project.clicked.connect(self.updateprojects)     #it will direct to update project page
        self.delete_project.clicked.connect(self.deleteprojects)     #it will direct to the delete project page
        self.set_up_meeting.clicked.connect(self.setupmeetings)
        self.logout.clicked.connect(self.gotowelcomepage)            #it will direct back to the welcome page
        
        
        #set the column width (the column number, the width value)
        for x in range(7):
            self.ProjectTable.setColumnWidth(x,200)                                    
            self.ProjectTable.setRowHeight(x,100)
        
        #load data from database list of projects
        self.LoadProjects()     
        
        #load data from database list of meetings
        self.LoadMeetingList()                                                    
        
    def LoadProjects(self):
        #establish a connection to the database
        conn = sqlite3.connect("ProjectManagementApp.db")                           
        cur = conn.cursor()
        #select all information from table with limit 50
        query = "SELECT * FROM projects ORDER BY status DESC"                                   
        self.ProjectTable.setRowCount(30)                                           
        index = 0
        for row in cur.execute(query):
            #display the data (row number, column number, QtWidgets.QTableWidgetItem(name_of_for_loop_variable["Key"])
            self.ProjectTable.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0])) 
            self.ProjectTable.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ProjectTable.setItem(index, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ProjectTable.setItem(index, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ProjectTable.setItem(index, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ProjectTable.setItem(index, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ProjectTable.setItem(index, 6, QtWidgets.QTableWidgetItem(row[6]))
            index = index + 1
            
        self.ProjectTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        
    def LoadMeetingList(self):
        
        meetings = []
        
        
        conn = sqlite3.connect("ProjectManagementApp.db")                           
        cur = conn.cursor()
        query = "SELECT title FROM meetings ORDER BY title ASC" 
        cur.execute(query) 
        meetingsRetrieved = cur.fetchall()
        
        def convertTuple(tup):
            str = ''
            for item in tup:
               str = str + item
            return str
        
        for row in meetingsRetrieved:
            meetingsRetrievedString = convertTuple(row)
            meetings.append(meetingsRetrievedString)
            
            
            
        for meeting in meetings:
            item = QtWidgets.QListWidgetItem(meeting)
            self.Lists.addItem(item)
            
            
    def createprojects(self): 
        formproject = CreateProject()
        widget.addWidget(formproject)
        widget.setCurrentIndex(widget.currentIndex()+1)  
        
    def updateprojects(self):
        changeproject = UpdateProject()
        widget.addWidget(changeproject)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def deleteprojects(self):
        removeproject = DeleteProject()
        widget.addWidget(removeproject)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def setupmeetings(self):
        arrangemeeting = SetUpMeeting()
        widget.addWidget(arrangemeeting)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotowelcomepage(self): 
        #a pop up will show that the user has logged out
        popup = PopUpLogOut()                                                      
        popup.exec()
        
        mainpage = WelcomePage()
        widget.addWidget(mainpage)
        widget.setCurrentIndex(widget.currentIndex()+1) 

#---------------------------------End-----------------------------------------#

#---------------------------Create Project Page-------------------------------#
        
class CreateProject (QtWidgets.QDialog): 
     def __init__(self):
         super(CreateProject,self).__init__()
         loadUi("CreateProjectPage.ui",self)                     #load the CreateProjectPage ui                                     
         self.Back.clicked.connect(self.gotomainmenupage)
         self.Create.clicked.connect(self.registerproject)
    
     #return to the main menu page
     def gotomainmenupage(self):                                               
         mainmenu = MainMenuPage()
         widget.addWidget(mainmenu)
         widget.setCurrentIndex(widget.currentIndex()+1) 
        
     #create a new project and store in database
     def registerproject(self):                                                    
         ProjectName = self.project_name_box.text()
         CompanyName = self.company_name_box.text()
         StartDate = self.start_date_box.text()
         EndDate = self.end_date_box.text()
         TotalBudget = self.total_budget_box.text()
         ActualCost = self.actual_cost_box.text()
         Status = self.status_box.currentText()
         
         #warns the user to fill in all fields
         if len(ProjectName)==0 or len(CompanyName)==0 or len(StartDate)==0 or len(EndDate)==0 or len(TotalBudget)==0 or len(ActualCost)==0 or len(Status)==0:
             self.error.setText("Please fill in all fields")                       
             
         else:
             self.error.setText("")
             #establish a connection with the database and load data to the database
             conn = sqlite3.connect("ProjectManagementApp.db")                     
             cur = conn.cursor()
             project_info = [ProjectName, CompanyName, StartDate, EndDate, TotalBudget, ActualCost, Status] 
             cur.execute('INSERT INTO projects (projectname, companyname, startdate, enddate, totalbudget, actualcost, status) VALUES (?,?,?,?,?,?,?)', project_info)
             conn.commit()
             conn.close()
             
             #a pop up will show to confirm that the user already created a project
             popup = PopUpCreatedProject()                                         
             popup.exec()
             
             #return to the main menu page
             mainmenu = MainMenuPage()
             widget.addWidget(mainmenu)
             widget.setCurrentIndex(widget.currentIndex()+1)
             
#---------------------------------End-----------------------------------------#

#--------------------------------Update Project-------------------------------#

class UpdateProject(QtWidgets.QDialog): 
    def __init__(self):
        super(UpdateProject,self).__init__()
        loadUi("UpdateProjectPage.ui",self)                        #load the UpdateProjectPage ui
        self.Back.clicked.connect(self.gotomainmenupage)                            
        self.Update.clicked.connect(self.changeproject)
        
        #change tuple to string because the data retrieved from database is in a form of tuple
        def convertTuple(tup):
            str = ''
            for item in tup:
                str = str + item
            return str
        
        #connect to database and retrieve the projectname from table projects
        conn = sqlite3.connect("ProjectManagementApp.db")
        cur = conn.cursor()
        query = "SELECT projectname FROM projects"
        cur.execute(query)
        output = cur.fetchall()

        #add projects name to Combo Box
        for row in output:
            str = convertTuple(row)
            self.name_of_project.addItem(str)
            
        #self.name_of_project.setCurrentIndex(-1)
        
    def changeproject(self):
            projectName = self.name_of_project.currentText()
            newCompanyName = self.company_name_box.text()
            newStartDate = self.start_date_box.text()
            newEndDate = self.end_date_box.text()
            newTotalBudget = self.total_budget_box.text()
            newActualCost = self.actual_cost_box.text()
            newStatus = self.status_box.currentText()
            
            
            connection = sqlite3.connect("ProjectManagementApp.db")
            cursor = connection.cursor()
                
                
            if len(newCompanyName)!= 0: 
                updateCompanyName =  'UPDATE projects SET companyname=\''+newCompanyName+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateCompanyName)
                print("Successfully updated Company Name")
                
            elif len(newStartDate)!=0:
                updateStartDate = 'UPDATE projects SET startdate=\''+newStartDate+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateStartDate)
                print("Successfully updated Start Date")

            elif len(newEndDate)!=0:
                updateEndDate = 'UPDATE projects SET enddate=\''+newEndDate+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateEndDate)
                print("Successfully updated End Date")
            
            elif len(newTotalBudget)!=0:
                updateTotalBudget = 'UPDATE projects SET totalbudget=\''+newTotalBudget+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateTotalBudget)
                print("Successfully updated Total Budget")
                
            elif len(newActualCost)!=0:
                updateActualCost = 'UPDATE projects SET actualcost=\''+newActualCost+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateActualCost)
                print("Successfully updated Actual Cost")
                
            elif len(newStatus)!=0:
                updateStatus = 'UPDATE projects SET status =\''+newStatus+'\''' WHERE projectname=\''+projectName+"\'"
                cursor.execute(updateStatus)
                print("Successfully updated Status")
                
            else:
                self.error.setText("Please fill in any of these fields")
                
            connection.commit()
            connection.close()
            
            if len(newCompanyName)!= 0 or len(newStartDate)!=0 or len(newEndDate)!=0 or len(newTotalBudget)!=0 or len(newActualCost)!=0 or len(newStatus)!=0:
                self.error.setText("")
                
                mainmenu = MainMenuPage()
                widget.addWidget(mainmenu)
                widget.setCurrentIndex(widget.currentIndex()+1) 
             
                #a pop up will show to confirm that the user already updated a project
                popup = PopUpChangeProject()                                         
                popup.exec()
       
 
    #return to the main menu page
    def gotomainmenupage(self):                                               
        mainmenu = MainMenuPage()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
#---------------------------------End-----------------------------------------#

#------------------------------Delete Project---------------------------------#

class DeleteProject(QtWidgets.QDialog): 
    def __init__(self):
        super(DeleteProject,self).__init__()
        loadUi("DeleteProjectPage.ui",self)                        #load the DeleteProjectPage ui
        self.Back.clicked.connect(self.gotomainmenupage)                            
        self.Delete.clicked.connect(self.strikeoutproject)
        
        #change tuple to string because the data retrieved from database is in a form of tuple
        def convertTuple(tup):
            str = ''
            for item in tup:
                str = str + item
            return str
        
        #connect to database and retrieve the projectname from table projects
        conn = sqlite3.connect("ProjectManagementApp.db")
        cur = conn.cursor()
        query = "SELECT projectname FROM projects"
        cur.execute(query)
        output = cur.fetchall()

        #add projects name to Combo Box
        for row in output:
            str = convertTuple(row)
            self.projects_name.addItem(str)
        
    #return to the main menu page
    def gotomainmenupage(self):                                               
        mainmenu = MainMenuPage()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    #delete the project
    def strikeoutproject(self):
        projectName = self.projects_name.currentText()
        
            
        conn = sqlite3.connect("ProjectManagementApp.db")
        cur = conn.cursor()
            
        delete = 'DELETE FROM projects WHERE projectname=\''+projectName+"\'"
            
        cur.execute(delete)
        conn.commit()
        conn.close()
            
        #a pop up will show to confirm that the user already deleted a project
        popup = PopUpDeleteProject()                                         
        popup.exec()
        
        mainmenu = MainMenuPage()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
        
        
#--------------------------------End------------------------------------------#

#----------------------------Set Up Meeting-----------------------------------#


class SetUpMeeting(QtWidgets.QDialog): 
    def __init__(self):
        super(SetUpMeeting,self).__init__()
        loadUi("SetUpMeetingPage.ui",self)                        #load the SetUpMeetingPage ui
        self.Back.clicked.connect(self.gotomainmenupage)
        self.Save.clicked.connect(self.savemeeting)
        self.Calendar.selectionChanged.connect(self.calendarDateChanged)
        
    #return to the main menu page
    def gotomainmenupage(self):                                               
        mainmenu = MainMenuPage()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
       
    #save meeting to database
    def savemeeting(self):
        Title = self.title_box.text()
        OrganizedBy = self.organized_by_box.text()
        Date = self.date_box.text()
        StartTime = self.start_time_box.text()
        EndTime = self.end_time_box.text()
        
        if len(Title)==0 or len(OrganizedBy)==0 or len(Date)==0 or len(StartTime)==0 or len(EndTime)==0 :
            self.error.setText("Please fill in all fields")
        
        else:
            self.error.setText("")
            conn = sqlite3.connect("ProjectManagementApp.db")                     
            cur = conn.cursor()
            meeting_info = [Title, OrganizedBy, Date, StartTime, EndTime] 
            cur.execute('INSERT INTO meetings (title, organizedby, date, starttime, endtime) VALUES (?,?,?,?,?)', meeting_info)
            conn.commit()
            conn.close()
            
            popup = PopUpSetUpMeeting()                                         
            popup.exec()
            
            mainmenu = MainMenuPage()
            widget.addWidget(mainmenu)
            widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def calendarDateChanged(self):
         dateSelected = self.Calendar.selectedDate().toPyDate()
         self.date_box.setText(dateSelected.strftime("%Y-%m-%d"))
         
         
#--------------------------------End------------------------------------------#



#-----------------------------Main Page---------------------------------------#


app = QtWidgets.QApplication(sys.argv)
mainwindow = WelcomePage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(1201) 
widget.setFixedHeight(801)
widget.show()
app.exec()

#---------------------------------End-----------------------------------------#      
        
        