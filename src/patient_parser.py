import re
from backend.src.parser_generic import medicaldocparser

class patientdetailparser(medicaldocparser):
    def __init__(self,text):
        medicaldocparser.__init__(self,text)

    def parse(self):
        return{
            "patient_name":self.get_name(),
            "patient_number":self.get_number(),
            "hapatitis_b_vaccine":self.get_vaccine(),
            "patient_disease":self.get_disease(),
        }
    def get_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name=''
        if matches:
            name = self.name_noise_remove(matches[0])
        return name


    def name_noise_remove(self,name):
        name = name.replace('Birth Date', '').strip()
        pattern = '((Jan|February|March|April|May|June|July|August|Septemper|October|November|December) [\d ]+)'
        date_matches = re.findall(pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_number(self):
        pattern = 'Patient Information.*?(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        return matches[0].strip()

    def get_vaccine(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        return matches[0].strip()

    def get_disease(self):
        pattern = 'List any Medical Problems \(asthma, seizures, headaches\):(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        return matches[0].strip()


if __name__ == "__main__":
    document_text='''
    17/12/2020

    Patient Medical Record
    
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 ‘
    United States Height:
    190
    In Casc of Emergency
    corEmergency a
    a
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    _
    ce ee re RY St I, NT Teal
    a
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE
    Have you had the Hepatitis B vaccination?
    No
    List any Medical Problems (asthma, seizures, headaches):
    Migraine
    '''
    data = patientdetailparser(document_text)
    print(data.parse())

