class Employee:
    def __init__(self, first_name, last_name, emp_number):
        self._first_name=first_name
        self._last_name=last_name
        self._emp_number=emp_number
    #getter
    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name
    @property
    def emp_num(self):
        return self._emp_number

    @first_name.setter
    def first_name(self, newName):
        self._first_name=newName
        
    @last_name.setter
    def last_name(self, newName):
        self._last_name=newName
        
    @emp_num.setter
    def emp_num(self, newEmpNum):
        self._emp_number=newEmpNum
    
