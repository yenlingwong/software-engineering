# from email.headerregistry import Address
import unittest
# from select import select
from urllib import response
from main import app
import requests
from bs4 import BeautifulSoup

#this is the class that holds entire test cases

class CoronaTestCases(unittest.TestCase):
    #Home_Page opens successfully or not
    def test_landing_page(self):
        request=app.test_client(self)
        response= request.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    #LogIn page for agent opens succesfully and accepts data or not
    #to go  in next page    
    
    def test_logagent_page(self):
        request=app.test_client(self)
        response= request.get('/log_agent', content_type='html/text', data=dict(Email="def@abc.com", Password="admin"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Agent LogIn', response.data)

    #LogIn page for hospital opens succesfully and accepts data or not
    #to go  in next page    
    def test_loghosp_page(self):
        request=app.test_client(self)
        response= request.get('/log_hospital', content_type='html/text',data=dict(Email="hos@gmail.com", Password="admin"))
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b'Hospital Login', response.data)

    #LogIn page for place opens succesfully and accepts data or not
    #to go  in next page    
    def test_logplace_page(self):
        request=app.test_client(self)
        response= request.get('/log_place', content_type='html/text', data=dict(Email="ghar@email.com", Password="admin"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place LogIn', response.data)

    #LogIn page for visitor opens succesfully and accepts data or not
    #to go  in next page    
    def test_logvisitor_page(self):
        request=app.test_client(self)
        response= request.get('/log_visitor', content_type='html/text', data=dict(Email="admin@admin.com", Password="admin"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor LogIn', response.data)    

    #Register page for hospital opens succesfully and accepts data or not
    #to go  in next page    
        
    def test_reghosp_page(self):
        request=app.test_client(self)
        response= request.get('/reg_hospital', content_type='html/text', data=dict(email="test@hosp.com", name="testhosp", reg="7823hu3f44",city="yes", address="no"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hospital Signup', response.data)    

    #Register page for Place opens succesfully and accepts data or not
    #to go  in next page    
    def test_regplace_page(self):
        request=app.test_client(self)
        response= request.get('/reg_place', content_type='html/text', data=dict(email="test@place.com", name="testpla", phone="54546756878",city="there", address="here", password="admin"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place Signup', response.data)    

    #Register page for Visitor opens succesfully and accepts data or not
    #to go  in next page    
    def test_regvis_page(self):
        request=app.test_client(self)
        response= request.get('/reg_visitor', content_type='html/text',data=dict(email="test@vis.com", name="testvis", phone="39839839",city="there", address="here", password="admin"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visitor Signup', response.data)


#Ensures that a invalid agent cannot login.
    def test_invalid_agent(self):
        request=app.test_client(self)
        response= request.get('/log_agent', content_type='html/text', data=dict(email="wrong", name="wrong", phone="00001",city="there", address="here", password="wrong"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imprint', response.data)   

#Ensures that a invalid visitor cannot login.
    def test_invalid_user(self):
        request=app.test_client(self)
        response= request.get('/log_visitor', content_type='html/text', data=dict(email="wrong", name="wrong", phone="00001",city="there", address="here", password="wrong"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imprint', response.data)  

#Ensures that a invalid place cannot login.
    def test_invalid_place(self):
        request=app.test_client(self)
        response= request.get('/log_place', content_type='html/text', data=dict(email="wrong", name="wrong", phone="00001",city="there", address="here", password="wrong"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imprint', response.data)  


#Ensures that a invalid hospital cannot login.
    def test_invalid_hospital(self):
        request=app.test_client(self)
        response= request.get('/log_place', content_type='html/text', data=dict(email="wrong", name="wrong", phone="00001",city="there", address="here", password="wrong"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Imprint', response.data)  

  
