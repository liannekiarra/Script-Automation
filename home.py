import subprocess
from subprocess import call


#Execute code from here

def Home() :
    
    #Introductory message allowing user to choose from the different subgroups of operating system management
    #This function returns an integer from 1-6 
    
    print(" --------------------------- WELCOME TO OPERATING SYSTEM MANAGEMENT ---------------------------")
    print("                                                                                               ")
    print("PLEASE CHOOSE A SUBGROUP")
    print("                                                                                               ")
    print("[1] USER AND GROUP MANAGEMENT")
    print("[2] FILE MANAGEMENT")
    print("[3] RESOURCE MONITORING")
    print("[4] PROCESS MANAGEMENT")
    print("[5] BACKUP AND RECOVERY")
    print("[6] PERFORMANCE REPORTING")
    print("                                                                                                              ")
    
    while True:
        valid = [1,2,3,4,5,6]
        print("Please choose an integer from range 1-6 corresponding to your choice.")
        answer = int(input("Enter the integer: "))
        if answer in valid:
            print(" ")
        else:
            print("Not valid.")
        if answer ==1:
            UserAndGroupManagement()
        if answer ==2:
            FileManagement()
        if answer ==3:
            resourceMonitoring()
        if answer == 4:
            processManagement()
        if answer == 5:
            backupAndRecovery()
        if answer == 6:
            performanceMonitoring()
    print("-------------------------------------------------------------------------------------------------")
    return answer
   
class userAndGroupManagement():
    
    def addUser(self):
        call("./addUser.sh", shell =True)
        
    def deleteUser(self):
        call("./deleteUser.sh", shell = True)
        return
    
    def addGroup(self):
        call("./addGroup.sh", shell = True)
        return
    
    def deleteGroup(self):
        call("./deleteGroup.sh", shell = True)
        return
    
    def addUserToGroup(self):
        call("./addUserToGroup.sh", shell = True)
        return
    
    def removeUserFromGroup(self):
        call("./removeUserFromGroup.sh", shell = True)
        return
    
    def assignGroup(self):
        call("./assignGroup.sh", shell = True)
        return
    
class fileManagement():
    
    def createFile(self):
        call("./createFile.sh", shell = True)

        return
    
    def createFileInPath(self):
        call("./createfileInPath.sh", shell = True)

        return
    
    def deleteFile(self):
        call("./deleteFile.sh", shell = True)

        return
    
    def encryptFile(self):
        call("./encryptFile.sh", shell = True)

        return

class ResourceMonitoring():
    
    def monitorMemory():
        call("./monitorMemory.sh", shell = True)
        
        return
    
    def monitorDisk():
        call("./monitorDisk.sh", shell = True)
        return
    
    def monitorFreeMemory():
        call("./monitorFreeMemory.sh", shell = True)
   

class ProcessManagement():
    
    def sortMemoryUsage(self):
        call("./sortMemoryUsage.sh", shell = True)
        return

    def sortCPUusage(self):
        call("./sortCPUusage.sh", shell = True)
        return
    
    def terminateProcess(self):
        call("./terminateProcess.sh", shell = True)
        return
    
    
class BackupAndRecovery():
    
    def performBackup():
        call("./backup.sh", shell = True)
        
        return   
    
class PerformanceReporting() :
    
    def generatePerformanceReport():
        call("./generatePerformanceReport.sh", shell = True)
        
        return
    
    
       
def UserAndGroupManagement():
    print('-------------------- USER AND GROUP MANAGEMENT -----------------------')
    print("                                                                         ")
    print("Select a specific task: ")
    print(" [1] ADD USER - add a user into the linux system (with password) ")
    print(" [2] DELETE USER - delete user from from the linux system")
    print(" [3] ADD GROUP - Create a new group inside the linux system (with GroupID)")
    print(" [4] ADD USER TO GROUP - add user to an existing group")
    print(" [5] REMOVE USER FROM GROUP - remove a  member of an existing group")
    print(" [6] ASSIGN GROUP - Assign ownership of a file/directory ")
    print("                                                                 ")
    print("Please select an integer from range 1-6.")
    answer = int(input("Enter your chosen integer: "))
    valid = [1,2,3,4,5,6]
    if answer in valid:
        print(" ")
    else:
        print("This is an invalid choice.")
        
    session = userAndGroupManagement()
    if answer == 1:
        session.addUser()
    else:
        print(" ")
    if answer  == 2:
        session.deleteUser()
    if answer == 3:
        session.addGroup()
    if answer == 4:
        session.addUserToGroup()
    if answer == 5:
        session.removeUserFromGroup()
    if answer == 6:
        session.assignGroup()

def FileManagement() :
    print("--------------------------- FILE MANAGEMENT -------------------------")
    print("                                                                     ")
    print(" Please select a task below.")
    print("                                                                      ")
    print("[1] CREATE FILE - create a file within current directory")
    print("[2] CREATE FILE IN PATH - create a file not in the current directory")
    print("[3] DELETE FILE - delete a file within current directory")
    print("[4] ENCRYPT FILE - encrypt a file ")
    print("                                                         ")
    print("Select an integer from range 1-4")

    answer = int(input("Enter a valid integer: "))
    valid = [1,2,3,4]
    if answer in valid:
        print(" ")
        session = fileManagement()
    else:
        print("This is not a valid choice.")

    if answer == 1:
        session.createFile()
    if answer == 2:
        session.createFileInPath()
    if answer == 3:
        session.deleteFile()
    if answer == 4:
        session.encryptFile()
    
        

def processManagement():
    print("------------------------ Process Management --------------------------")
    print("                                                                      ")
    print(" Select an option below")
    print("[1] IDENTIFY HIGH CPU CONSUMING PROCESSES - get information about processes that consume above average CPU resources  ")
    print("[2] IDENTIFY HIGH MEMORY CONSUMING PROCESSES - get inforamtion about processes that consume above average memory resources ")
    print("[3] TERMINATE PROCESS - terminate a selected process from PID (process id) ")
    print("                                         ")
    print("Choose an integer from range 1-2")
    
    answer = int(input('Enter chosen integer: '))
    valid = [1,2,3]
    if answer in valid:
        session = ProcessManagement()
    else:
        print("This is not a valid choice/integer.")
        
    if answer == 1:
        session.sortCPUusage()
    if answer ==2:
        session.sortMemoryUsage()
    if answer == 3:
        session.terminateProcess()
    
    
def performanceMonitoring():
    print("----------------- PERFORMANCE MONITORING----------------------")
    print("    ")
    print(" [1] Generate Performance Report - this script generates performance reports of teh linux system and device.")  
    answer= int(input("Press 1 to continue: "))
    if answer == 1:
        session = PerformanceReporting()
        session.generatePerformanceReport(
        )
    else:
        print("This is not a valid answer.")
    

def backupAndRecovery():
    print("---------------------- BACKUP AND RECOVERY ----------------------")
    print("       ")
    print( "[1] PERFORM SYSTEM BACKUP - this functionality performacne a system backup")
    answer = int(input( "PRess 1 to continue: "))
    if answer == 1:
        session = PerformanceReporting()
        session.generatePerformanceReport()
    else:
        print ('This is not a valid answer.')
        
def resourceMonitoring():
    #returns pdf files for user
    print("------------------------- RESOURCE MONITORING ------------------------")
    print(" ")
    print("[1] MONITOR MEMORY - shows Memory statistics")
    print("[2] MONITOR DISK - shows Disk statistics")
    print("[3] MONITOR FREE MEMORY - shows available memory storage")
    answer =int(input("Enter and Integer: "))
    valid = [1,2,3]
    if answer in valid:
        session = ResourceMonitoring()
    else:
        print("This answer is not valid")
    if answer == 1:
        session.monitorCPU()
    if answer == 2:
        session.monitorDisk()
    if answer ==3:
        session.monitorFreeMemory()
        

Home()