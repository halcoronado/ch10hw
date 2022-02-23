##write a class named Procedure that represents a 
# medical procedure that has been performed on a patient. 
# The Procedure class should have the following attributes - 
# Name of the procedure, Date of the procedure, Name of the practitioner who performed the procedure,
#  Charges for the procedure and patient ID. 
# The Procedure class’s __init__ method should accept an argument for each attribute. 
# The Procedure class should have accessor methods only for each attribute.


class Procedure:

    def __init__(self,patientID,charges,pract_name,pro_date,pro_name):
        self.__procedurename = pro_name
        self.__pro_date = pro_date
        self.__practitioner = pract_name
        self.__charges = charges 
        self.__patientID = patientID
    
    def get_pro_name(self):
        return self.__procedurename
    
    def get_pro_date(self):
        return self.__pro_date
    def get_pract_name (self):
        return self.__practitioner
    def get_charges(self):
        return self.__charges
    