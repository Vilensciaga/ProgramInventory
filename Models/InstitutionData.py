class InstitutionData:
    def __init__(self, Institution, DegreeLevel, CIP, PSE, SpecializedAdmissions, CreditHours, Implemented, Suspended, Terminated):
        self.Institution = Institution
        self.DegreeLevel = DegreeLevel
        self.CIP = CIP
        self.PSE = PSE
        self.SpecializedAdmissions = SpecializedAdmissions
        self.CreditHours = CreditHours
        self.Implemented = Implemented
        self.Suspended = Suspended
        self.Terminated = Terminated


    def __str__(self):
        return (f"Institution: {self.Institution}, DegreeLevel: {self.DegreeLevel}, "
                f"CIP: {self.CIP}, PSE: {self.PSE}, SpecializedAdmissions: {self.SpecializedAdmissions}, "
                f"CreditHours: {self.CreditHours}, Implemented: {self.Implemented}, "
                f"Suspended: {self.Suspended}, Terminated: {self.Terminated}")



    
