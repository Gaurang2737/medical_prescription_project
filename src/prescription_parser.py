import re

from backend.src.parser_generic import medicaldocparser
class prescriptionparser(medicaldocparser):
    def __init__(self,text):
        medicaldocparser.__init__(self,text)

    def parse(self):
        return {
            "patient_name": self.get_field("patient_name"),
            "patient_address": self.get_field("patient_address"),
            "patient_medicine": self.get_field("patient_medicine"),
            "medicine_directions": self.get_field("medicine_directions"),
            "medicine_refill": self.get_field("medicine_refill")
        }


    def get_field(self,field):
        pattern_field = {
            'patient_name':{'pattern':'Name:(.*)Date','flags':0},
            'patient_address': {'pattern': 'Address:(.*)', 'flags':0},
            'patient_medicine': {'pattern': 'K(.*)Directions:', 'flags':re.DOTALL},
            'medicine_directions': {'pattern': 'Directions:(.*)Refill:', 'flags':re.DOTALL},
            'medicine_refill': {'pattern': 'Refill:(.*)times', 'flags':re.DOTALL},
        }
        pattern_object = pattern_field.get(field)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'],self.text,pattern_object['flags'])
            if len(matches)>0:
                return matches[0].strip()





if __name__ == '__main__':
    documnet_text='''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022 
Address: 9 tennis court, new Russia, DC
Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks  ,
Lialda  take 2 pill everyday for 1 month 
Refill: 2 times

'''
    text_data = prescriptionparser(documnet_text)
    print(text_data.parse())

