#!/usr/bin/env python3.8
import threading as th
import time

class boss():
    def __init__(self):
        self.myManagers = []
        self.name = "\033[0;31mBoss\033[0m"#red font
        self.importantList = [] #THIS ONE LIST could changed by everyone
        print(self.name + " init")

    def run(self):#spread work to manager
        self.importantList.append(paper(self.name))
        self.importantList.append(paper(self.name))

        for i in range(0, 2):
           self.myManagers.append(Manager(self.importantList, i))
           self.myManagers[-1].start()

    def printImportantList(self):
        summarList = " List: (by " + self.name + ")\n"
        for entry in self.importantList:
            summarList = summarList + "   " + entry.name + "\n"
        print(summarList)


class Manager(th.Thread):
#class Manager():
    def __init__(self, importantList, id):
        th.Thread.__init__(self)
        self.importantList = importantList
        self.id = str(id)
        self.name = "\033[0;33mManager[" + self.id + "]\033[0m"#yellow font
        self.myEmployees = []
        print(self.name + " init")

#    def start(self):
#        self.run()

    def run(self):
        self.importantList.append(paper(self.name))
        self.importantList.append(paper(self.name))
        self.importantList.append(paper(self.name))

        for i in range(0, 5):
            self.myEmployees.append(Employee(self.importantList, self.id + "." + str(i)))
            self.myEmployees[-1].start()


class Employee(th.Thread):
#class Employee():
    def __init__(self, importantList, id):
        th.Thread.__init__(self)
        self.importantList = importantList
        self.id = id
        self.name = "\033[0;32mEmployee[" + str(self.id) + "]\033[0m"#green font
        print(self.name + " init")

#    def start(self):
#        self.run()

    def run(self):
        for i in range(0, 5):
            self.importantList.append(paper(self.name))


class paper():
    def __init__(self, caller):
        self.name = "by " + caller
        print(caller + " added a Paper")

if __name__ == "__main__":

    CEO = boss()
    CEO.run()
    time.sleep(2)
    """
        ### Threading example
        to make sure the employees and manager had done their jobs
        When this script ends, all containing threads are terminated,
        regardless of whether the tasks have been processed.
        Either one implements a runner variable that is set one down with each completed task. At the end there is then something like
        while(variable > 0):
            s.th()
        To disable threading, the following lines should be left out or uncommented commented out code lines 
        Comment out (write a # at the beginning of the line):
        - Line 27
        - Line 30
        - Line 50
        - Line 53

        Comment (remove # at the beginning of the line):
        - Line 28
        - Line 37
        - Line 38
        - Line 51
        - Line 59
        - Line 60

        There are certainly more elegant solutions to this problem, but I can't think of them right now.
    """
    CEO.printImportantList()