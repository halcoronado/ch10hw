##Write a class named Patient that has the following 
# attributes - ID, 
# #name, address, phone, veteran_status (True or False). 
# The Patient class’s __init__ 
# #method should accept an argument for each attribute. 
# The Patient class should have accessor methods only 
# for each attribute.

class Patient:

    def __init__(self, patientID, name, address, phone, veteran_status):
        self.__patientID = patientID
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status
    
    def get_patientID (self):
        return self.__patientID
    def get_name (self):
        return self.__name
    def get_address (self):
        return self.__address
    def get_phone (self):
        return self.__phone
    def get_veteran_status(self):
        return self.__veteran_status

