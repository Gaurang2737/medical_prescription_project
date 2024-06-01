import pytest
from backend.src.patient_parser import patientdetailparser

@pytest.fixture()
def doc_1_kathy():
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
    return patientdetailparser(document_text)
@pytest.fixture()
def doc_2_jerry():
    document_text='''
   17/12/2020

    Patient Medical Record
    
    Patient Information Birth Date
    
    Jerry Lucas May 2 1998
    
    (279) 920-8204 . Weight:
    
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201 Height:
    
    United States gnt
    170
    
    In Case of Emergency
    eee
    
    Joe Lucas 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone . United States
    Work phone
    
    General Medical History
    
    Chicken Pox (Varicelia): Measles:
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    _ Yes
    
    List any Medical Problems (asthma, seizures, headaches):
    N/A


    '''
    return patientdetailparser(document_text)

def test_get_name(doc_1_kathy,doc_2_jerry):
    assert doc_1_kathy.get_name()=="Kathy Crawford"
    assert doc_2_jerry.get_name()=="Jerry Lucas"

def test_get_number(doc_1_kathy,doc_2_jerry):
    assert doc_1_kathy.get_number()=="(737) 988-0851"
    assert doc_2_jerry.get_number()=="(279) 920-8204"

def test_get_vaccine(doc_1_kathy,doc_2_jerry):
    assert doc_1_kathy.get_vaccine()=="No"
    assert  doc_2_jerry.get_vaccine()=="Yes"

def test_get_disease(doc_1_kathy,doc_2_jerry):
    assert doc_1_kathy.get_disease()=="Migraine"
    assert doc_2_jerry.get_disease()=="N/A"

def test_parser(doc_1_kathy,doc_2_jerry):
    pattern_kathy=doc_1_kathy.parse()
    assert pattern_kathy=={
        "patient_name": "Kathy Crawford",
        "patient_number": "(737) 988-0851",
        "hapatitis_b_vaccine": "No",
        "patient_disease": "Migraine",
    }

    pattern_jerry = doc_2_jerry.parse()
    assert pattern_jerry=={
        "patient_name": "Jerry Lucas",
        "patient_number": "(279) 920-8204",
        "hapatitis_b_vaccine": "Yes",
        "patient_disease": "N/A",
    }

