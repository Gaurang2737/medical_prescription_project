from backend.src.prescription_parser import prescriptionparser
import pytest

@pytest.fixture()
def doc_1_marta():
    document_text = '''
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
    return prescriptionparser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
    Dr John >mith, M.D

    2 Non-Important street,
    New York, Phone (900)-323- ~2222
    Name:  Virat Kohli Date: 2/05/2022
    Address: 2 cricket blvd, New Delhi
    | Omeprazole 40 mg
    Directions: Use two tablets daily for three months
    Refill: 3 times
    '''
    return prescriptionparser(document_text)

@pytest.fixture()
def doc_3_empty():
    return prescriptionparser("")

def test_get_name(doc_1_marta,doc_2_virat,doc_3_empty):
    assert doc_1_marta.get_field("patient_name") == "Marta Sharapova"
    assert doc_2_virat.get_field("patient_name") == "Virat Kohli"
    assert doc_3_empty.get_field("patient_name") == None

def test_get_address(doc_1_marta,doc_2_virat,doc_3_empty):
    assert doc_1_marta.get_field("patient_address") == "9 tennis court, new Russia, DC"
    assert doc_2_virat.get_field("patient_address") == "2 cricket blvd, New Delhi"
    assert doc_3_empty.get_field("patient_address") == None

def test_get_medicine(doc_1_marta,doc_2_virat):
    assert doc_1_marta.get_field("patient_medicine") == '''Prednisone 20 mg
    Lialda 2.4 gram'''
    assert doc_2_virat.get_field("patient_medicine") == '''| Omeprazole 40 mg'''

def test_get_directions(doc_1_marta,doc_2_virat):
    assert doc_1_marta.get_field("medicine_directions") == '''Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks  ,
    Lialda  take 2 pill everyday for 1 month'''
    assert  doc_2_virat.get_field("medicine_directions") == "Use two tablets daily for three months"

def test_get_refill(doc_1_marta,doc_2_virat):
    assert doc_1_marta.get_field("medicine_refill") == "2"
    assert doc_2_virat.get_field("medicine_refill") == "3"

def test_parse(doc_1_marta,doc_2_virat,doc_3_empty):
    record_marta = doc_1_marta.parse()
    assert record_marta["patient_name"] == "Marta Sharapova"
    assert record_marta["patient_address"] == "9 tennis court, new Russia, DC"
    assert record_marta["patient_medicine"] == '''Prednisone 20 mg
    Lialda 2.4 gram'''
    assert record_marta["medicine_directions"] == '''Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks  ,
    Lialda  take 2 pill everyday for 1 month'''
    assert record_marta["medicine_refill"] == "2"

    record_virat = doc_2_virat.parse()
    assert record_virat=={
        "patient_name":"Virat Kohli",
        "patient_address":"2 cricket blvd, New Delhi",
        "patient_medicine":"| Omeprazole 40 mg",
        "medicine_directions":"Use two tablets daily for three months",
        "medicine_refill":"3"
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        "patient_name": None,
        "patient_address": None,
        "patient_medicine": None,
        "medicine_directions": None,
        "medicine_refill": None
    }