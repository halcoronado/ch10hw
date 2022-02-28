import PatientClass as pat

import ProcedureClass as proc

def main():
    patient = pat.Patient(1,"Matt Jones", "123 Main st, Waco TX 76706","254-555-7415", True)
    app1 = proc.Procedure(1,250,"Dr. Irvine", "2/15/2022", "Physical Exam")
    app2 = proc.Procedure(1, 1500, "Dr. Hamilton", "2/15/2022", "MRI")
    app3 = proc.Procedure(2,1200,"Dr. Drey",'2/17/2022',"CT Scan" )

    
    total = 0

    print ("*** Patient Bill ***")
    print("Name:", patient.get_name())
    print("Address:", patient.get_address())
    print ("Phone:", patient.get_phone())
    print()
    print ("Procedure:", app1.get_pro_name())
    print("Date:", app1.get_pro_date())
    print("Practitioner:",app1.get_pract_name())
    print("Charge: $", format(app1.get_charges(),',.2f'))
    print()
    print ("Procedure:", app2.get_pro_name())
    print("Date:", app2.get_pro_date())
    print("Practitioner:", app2.get_pract_name())
    print("Charge: $", format(app2.get_charges(),',.2f'))
    print()
    if patient.get_veteran_status() == True:
        total = (app1.get_charges()+app2.get_charges())
        print ("Total Charges: $", format(total- (total*.4), ',.2f'))
    else:
        print("Total Charges: $", format(app1.get_charges()+app2.get_charges(), ',.2f'))

main()